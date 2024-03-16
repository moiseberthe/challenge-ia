const N_STEPS = 5

document.addEventListener("DOMContentLoaded", () => {
    setTimeout(() => {
        // select continues bouton 
        const nexter = document.querySelector('.btn-continue.nexter');
        document.querySelector('.step').classList.add('active')
        
        const letter = document.querySelector('.step.active .write-line .btn-letter');
        if (!!letter) {
            letter.classList.add('current');
        }

        if (!!nexter) {
            nexter.addEventListener("click", (event) => {
                const steps = document.querySelector('.steps');
                const progress_bar = document.querySelector('.progress-bar');
                let left = parseInt(steps.style.left);

                if(!left) {
                    left = 0;
                    steps.style.left = 0;
                }

                if (left > -(100 * (N_STEPS - 1))) {
                    nexter.classList.add('disabled');
                    const all_steps = document.querySelectorAll('.step');
                    
                    all_steps.forEach(element => {
                        element.classList.remove('active');
                    });
                    steps.style.left = (left - 100)+"%";
                    
                    const progress_level = (-1 * (left - 100) / 100);
                    document.querySelector('#question-'+progress_level).classList.add('active');

                    const letters = document.querySelector('.step.active .write-line .btn-letter');
                    if (!!letters) {
                        letters.classList.add('current');
                    }

                    progress_bar.style.width = ((100 / N_STEPS) * progress_level)+"%";
                }
            });
        }

    }, 2000);
});