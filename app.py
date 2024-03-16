import asyncio
import base64
import threading
import dash, cv2
from dash import html
from quart import Quart, websocket
from keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import mediapipe as mp
import numpy as np
import string


from utils import mediapipe_detection, extract_keypoints, draw_styled_landmarks

mp_holistic = mp.solutions.holistic # Holistic model

# Actions that we try to detect
actions = np.array(list(string.ascii_uppercase))

# Label mapping
label_map = {label:num for num, label in enumerate(actions)}

model = Sequential()
model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(30, 126)))
model.add(LSTM(128, return_sequences=True, activation='relu'))
model.add(LSTM(64, return_sequences=False, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(actions.shape[0], activation='softmax'))
model.load_weights('action_26L.h5')

####


class VideoCamera(object):
    def __init__(self, video_path):
        self.video = cv2.VideoCapture(video_path)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        _, jpeg = cv2.imencode('.jpg', image)
        return image, jpeg.tobytes()

# Setup small Quart server for streaming via websocket.
server = Quart(__name__)
# Add delay (in seconds) if CPU usage is too high
delay_between_frames = 0.05

@server.websocket("/stream")
async def stream():
    sequence = []
    threshold = 0.5

    camera = VideoCamera(0)  # zero means webcam
    pred = 'NO'
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        while True:
            if delay_between_frames is not None:
                await asyncio.sleep(delay_between_frames)  # add delay if CPU usage is too high
            real_image, frame = camera.get_frame()

            # Make a detection and check if there is a hand on the image
            image, results = mediapipe_detection(real_image, holistic)
            if results.left_hand_landmarks or results.right_hand_landmarks:
                
                # draw landmarks on image
                draw_styled_landmarks(image, results)
                _, jpeg = cv2.imencode('.jpg', image)
                
                # Extract hand key point 
                keypoints = extract_keypoints(results)
                # Add keypoints to a sequence 
                sequence.append(keypoints)
                # Get last 30 sequences (last 30 frames)
                sequence = sequence[-30:]
                
                # if there are enough frames, make a prediction and get the letter 
                # that has a greater probability than the threshold
                if len(sequence) == 30:
                    res = model.predict(np.expand_dims(sequence, axis=0))[0]
                    if res[np.argmax(res)] > threshold: 
                        pred = actions[np.argmax(res)]
                
                frame = jpeg.tobytes()
            
            # Returns the prediction and the image separated by || and spit it in front to get both
            await websocket.send(f"{pred}||data:image/jpeg;base64, {base64.b64encode(frame).decode()}")
            
app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=['https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css']
)

app.layout = html.Div(
    children=[dash.page_container]
)

if __name__ == '__main__':
    # Run dash on a thread
    threading.Thread(target=app.run_server).start()
    server.run()