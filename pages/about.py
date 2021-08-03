import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
import pickle
from app import app
import pandas as pd
import numpy as np
import sklearn


pipeline = load('notebooks/pipeline.joblib')

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions


            """, className='mb-5'
        ),
        dcc.Markdown('#### Annual Income'),
        dcc.Slider(
            id='annual_inc',
            min=20000, 
            max=200000, 
            step=5, 
            value=220000, 
            marks={n: str(n) for n in range(20000,220000,20000)},
            className='mb-5', 
        ),
        dcc.Markdown('#### Credit Score'),
        dcc.Slider(
            id='fico_range_low',
            min=650, 
            max=850, 
            step=5, 
            value=900, 
            marks={n: str(n) for n in range(650,900,50)},
            className='mb-5',
        ),
        dcc.Markdown('#### Loan Amount'),
        dcc.Slider(
            id='loan_amnt',
            min=5000, 
            max=40000, 
            step=5, 
            value=45000, 
            marks={n: str(n) for n in range(5000,45000,5000)},
            className='mb-5',           
        ),
        dcc.Markdown('#### Loan Purpose'), 
        dcc.Dropdown(
            id='purpose',
            options = [
                {'label': 'debt_consolidation', 'value': 'debt_consolidation'}, 
                {'label': 'credit_card', 'value': 'credit_card'}, 
                {'label': 'home_improvement', 'value': 'home_improvement'}, 
                {'label': 'other', 'value': 'other'}, 
                {'label': 'car', 'value': 'car'}, 
                {'label': 'major_purchase', 'value': 'major_purchase'}, 
                {'label': 'educational', 'value': 'educational'}, 
                {'label': 'vacation', 'value': 'vacation'}, 
                {'label': 'moving', 'value': 'moving'},
                {'label': 'medical', 'value': 'medical'},
                {'label': 'house', 'value': 'house'},
                {'label': 'wedding', 'value': 'wedding'}, 
                {'label': 'small_business', 'value': 'small_business'}, 
                {'label': 'renewable_energy', 'value': 'renewable_energy'}, 
            ],
            value = 'debt_consolidation',
            className='mb-5',

        ),
        dcc.Markdown('#### term'), 
        dcc.Dropdown(
            id='term',
            options = [
                {'label': '36 months', 'value': '36 months'}, 
                {'label': '60 months', 'value': '60 months'},
            ],
            value = '36 months',
            className='mb-5',

        ),
        dcc.Markdown('#### Revolving Credit Debt(%)'),
        dcc.Slider(
            id='revol_util',
            min=0, 
            max=100, 
            step=5, 
            value=100, 
            marks={n: str(n) for n in range(0,110,10)},
            className='mb-5',

        ),
        dcc.Markdown('#### Debt-to-Income(%)'),
        dcc.Slider(
            id='dti',
            min=0, 
            max=100, 
            step=5, 
            value=100, 
            marks={n: str(n) for n in range(0,110,10)},
            className='mb-5',

        ),
        
    ],
    md=7,
)

column2 = dbc.Col(
    [
        html.H2('Expected Interest', className='mb-5'), 
        html.Div(id='prediction-content', className='lead'),
        html.Img(src='assets/calculator_money.jpeg', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2])


@app.callback(
    Output('prediction-content', 'children'),
    [Input('fico_range_low', 'value'), Input('term', 'value'),Input('dti', 'value'),Input('revol_util', 'value'),Input('annual_inc', 'value'),Input('loan_amnt', 'value'),Input('purpose', 'value')],
)
def predict(fico_range_low, term, dti, revol_util, annual_inc,loan_amnt,purpose):
    df = pd.DataFrame(
        columns=["fico_range_low", 'term', 'dti', 'revol_util', 'annual_inc', 'loan_amnt', 'purpose'], 
        data=[[fico_range_low, term, dti, revol_util, annual_inc,loan_amnt,purpose]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'{y_pred:.2f}% Interest Rate'

#Check data types: f"{fico_range_low} {type(fico_range_low)}, {term} {type(term)}, {dti}{type(dti)}, {revol_util}{type(revol_util)}, {annual_inc}{type(annual_inc)},{loan_amnt}{type(loan_amnt)},{purpose}{type(purpose)}"





column3 = dbc.Col(
    [  
        (
            html.Img(src='assets/profile_photo.png', style= {'width': '100%', 'display': 'inline-block'}, alt="Responsive image", className='mb-4')          
        ),
        # dcc.Markdown(
        #     """ 
        #     #### Maxime Vacher-Materno       
        #     #### Data Scientist 
        #     """,
        # className='mb-4'),
    ]
)

column4 = dbc.Col(
    [   
       # (
       #      html.Img(src='assets/lambdaLogo.png', style= {'width': '50%', 'display': 'inline-block'}, alt="Responsive image", className='mb-4')          
       #  ),
        dcc.Markdown(
            """ 
            ### Ashley Adrias      
            #### Data Scientist & Mechanical Engineer
            ##### Languages: Python, Javascript
            ##### Web Dev: HTML, Django, Dash, Flask
            ##### Database: SQL, RDS, Redshift
            ##### Machine Learning, Neural Networks, NLP and Statistics
            ##### Cloud: AWS, Elasticsearch, S3, EC2
            ##### Dashboarding: Dash Plotly, Tableau, Quicksight
            """,
        className='mb-4'),
    ]
)

layout = dbc.Row([column3,column4])