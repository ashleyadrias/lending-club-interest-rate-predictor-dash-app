import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [  
        (
            html.Img(src='assets/profile_photo.png', style= {'width': '100%', 'display': 'inline-block'}, alt="Responsive image", className='mb-4')          
        ),
        
    ]
)

column2 = dbc.Col(
    [   
       # (
       #      html.Img(src='assets/lambdaLogo.png', style= {'width': '50%', 'display': 'inline-block'}, alt="Responsive image", className='mb-4')          
       #  ),
        dcc.Markdown(
            """ 
            ### Ashley Adrias      
            #### Data Scientist & Engineer
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

layout = dbc.Row([column1,column2])