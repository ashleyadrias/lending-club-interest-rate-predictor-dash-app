# import dash
# import dash_bootstrap_components as dbc
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output
# from joblib import load
# from app import app
# import pandas as pd

# pipeline = load('assets/pipeline.joblib')

# column1 = dbc.Col(
#     [
#         dcc.Markdown(
#             """
        
#             ## Evaluation


#             """, className='mb-5'
#         ),
#         dcc.Markdown('#### Age'),
#         dcc.Slider(
#             id='Age',
#             min=19, 
#             max=41, 
#             step=5, 
#             value=41, 
#             marks={n: str(n) for n in range(19,41,20)},
#             className='mb-5',  
#         ),
#         dcc.Markdown('#### Position'), 
#         dcc.Dropdown(
#             id='Position',
#             options = [
#                 {'label': 'PG', 'value': 'PG'}, 
#                 {'label': 'SF', 'value': 'SF'}, 
#                 {'label': 'PF', 'value': 'PF'}, 
#                 {'label': 'SG', 'value': 'SG'}, 
#                 {'label': 'C', 'value': 'C'}, 
#             ],
#             value = 'PG',

#         ),
#     ],
#     md=4,
# )

# column2 = dbc.Col(
#     [
#         html.H2('Expected Lifespan', className='mb-5'), 
#         html.Div(id='prediction-content', className='lead')
#     ]
# )

# layout = dbc.Row([column1, column2])


# @app.callback(
#     Output('prediction-content', 'children'),
#     [Input('Age', 'value'), Input('Position', 'value')],
# )
# def predict(Age, Position):
#     df = pd.DataFrame(
#         columns=['Age', 'Position'], 
#         data=[[Age, Position]]
#     )
#     y_pred = pipeline.predict(df)[0]
#     return f'${y_pred:.0f} salary'

