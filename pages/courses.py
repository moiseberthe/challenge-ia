import dash
from dash import html

dash.register_page(__name__)

layout = html.Div(
    className='',
    children=[
        html.Div(className='left-body', children=[
            html.Div(className='left-head', children=[
                html.Div(className='left-bar-content', children=[
                    html.Div(className='logo', children=[
                        html.H1('Quatrosigno')
                    ])
                ]),
                html.Div(className='nar-bar', children=[
                    html.Ul(className='nav-ul', children=[
                        html.Li(children=[
                            html.Button(className='nav-item w-100', children=[
                                html.Img(className='nav-ico', src='https://d35aaqx5ub95lt.cloudfront.net/vendor/784035717e2ff1d448c0f6cc4efc89fb.svg', alt=''),
                                html.Span('Mes cours')
                            ])
                        ]),
                        html.Li(children=[
                            html.A(className='nav-item w-100', href="/help", children=[
                                html.Img(className='nav-ico', src='https://simg-ssl.duolingo.com/avatars/981300147/78FYzQ0V0W/xlarge', alt=''),
                                html.Span('Alphabet')
                            ])
                        ])
                    ])
                ])
            ])
        ]),
        html.Div(className='right-body', children=[
            html.Div(className='content', children=[
                html.Div(className='middle-body', children=[
                    html.H1("Bonjour", className="hello-msg"),
                    html.Div(className='chapiters', children=[
                        html.Div(className='chapiter', children=[
                            html.Div(className='chapiter-left', children=[
                                html.H3('Chapitre 1'),
                                html.Div(className='chapiter-status finished', children=[
                                    html.Div(className='status-ico', children=[
                                        html.I(className='fa-solid fa-circle-check')
                                    ]),
                                    html.Div(className='status-title', children=[
                                        'Terminé !!'
                                    ])
                                ])
                            ]),
                            html.Div(className='chapiter-right', children=[
                                html.A('Commencer', href="/cours1", className='btn-start-chapiter')
                            ])
                        ]),
                        html.Div(className='chapiter', children=[
                            html.Div(className='chapiter-left', children=[
                                html.H3('Chapitre 2'),
                                html.Div(className='chapiter-status locked', children=[
                                    html.Div(className='status-ico', children=[
                                        html.I(className='fa-solid fa-lock')
                                    ]),
                                    html.Div(className='status-title', children=[
                                        'Verrouillé !!'
                                    ])
                                ])
                            ]),
                            html.Div(className='chapiter-right', children=[
                                html.A('Commencer', href="/cours3", className='btn-start-chapiter')
                            ])
                        ])
                    ])
                ]),
                html.Div(className='very-right-body', children=[
                    html.Div(className='cards', children=[
                        html.Div(className='card', children=[
                            html.Ul(className='nav-ul', children=[
                                html.Li(children=[
                                    html.Button(className='nav-item w-100', children=[
                                        html.Img(className='nav-ico', src='https://d35aaqx5ub95lt.cloudfront.net/vendor/7ef36bae3f9d68fc763d3451b5167836.svg', alt=''),
                                        html.Div(className='score', children=[
                                            html.Div(className='score-title', children=[
                                                'Score'
                                            ]),
                                            html.Div(className='score-number', children=[
                                                '23'
                                            ])
                                        ])
                                    ])
                                ]),
                                html.Li(children=[
                                    html.Button(className='nav-item w-100', children=[
                                        html.Img(className='nav-ico', src='https://d35aaqx5ub95lt.cloudfront.net/vendor/5187f6694476a769d4a4e28149867e3e.svg', alt=''),
                                        html.Div(className='score', children=[
                                            html.Div(className='score-title', children=[
                                                'Lettres apprises'
                                            ]),
                                            html.Div(className='score-number', children=[
                                                '23'
                                            ])
                                        ])
                                    ])
                                ]),
                            ])
                        ])
                    ])
                ])
            ])
        ])
    ]
)