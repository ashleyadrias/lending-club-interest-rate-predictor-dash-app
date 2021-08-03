import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
from app import app
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            #### Describe a movie you would like to watch: 
            """,style={'width': '90%', 'display': 'inline-block'}, className='mb-4'
        ),
        dcc.Textarea(id='tokens',placeholder='Example: High School Vampire Drama',style={'height':100,'width': '90%', 'display': 'inline-block'},value='',className='mb-4'),
        dcc.Markdown(
            """
        
            #### My Movie Recommendations: 
            """,style={'width': '90%', 'display': 'inline-block'}, className='mb-4'
        ),
        html.Div(id='prediction-content', className='lead'),
        html.Div(id='prediction-content2', className='lead'),
        html.Div(id='prediction-content3', className='lead'),
        html.Div(id='prediction-content4', className='lead'),
        html.Div(id='prediction-content5', className='lead'),
        html.Img(src='assets/hp.jpg',style={'width': '90%', 'display': 'inline-block'}, className='img-fluid'),
        # dbc.FormText("Type something in the box above"),
               
        # for _ in ALLOWED_TYPES
    ],style={'display': 'inline-block'}
    # md=7,
)

column2 = dbc.Col(
    [   #et tu auras une recette selon les ingrédients que tu as

        # html.H2('Sandwich Recommender Marmiton', className='mb-5'), 
        # html.Div(id='prediction-content', className='lead'),
        # dcc.Link(id='url', href='', children="Lien De La Recette ICI!!!", target="_blank"),
        
        # dcc.Link(dbc.Button('Clique ICI pour voir la recette !!!', color='warning'), id='url', href='', target="_blank"),


        # html.A(html.Img(src='assets/Netflix_people.jpeg', className='img-fluid'), href="http://www.google.com/search?q='prediction-content',
        # html.Img(src='assets/Sandwich2.jpeg', className='img-fluid')
    ]
)

layout = dbc.Row([column1])


@app.callback([
    Output('prediction-content', 'children'),
    Output('prediction-content2', 'children'),
    Output('prediction-content3', 'children'),
    Output('prediction-content4', 'children'),
    Output('prediction-content5', 'children'),
    ], 
    [Input('tokens','value')]
)


def predict(tokens):
    df = pd.read_csv('./notebooks/netflix_titles.csv')
    df = df[(df['type'] == 'Movie') & (df['country'] == 'United States')]
    df = df.reset_index(drop=True)

    tfidf = pickle.load(open("./notebooks/vect_01.pkl", "rb"))
    nn = pickle.load(open("./notebooks/knn_01.pkl", "rb"))

   # Transform
    request = pd.Series(tokens)
    request_sparse = tfidf.transform(request)

    # Send to df
    request_tfidf = pd.DataFrame(request_sparse.todense())

    # Return a list of indexes
    # top5 = nn.kneighbors([request_tfidf][0], n_neighbors=5)[1][0].tolist()
    results = nn.kneighbors([request_tfidf][0], n_neighbors=5)
    
    # Send recomendations to DataFrame
    # recommendations_df = df.iloc[top5]
    
    # string = str(recommendations_df['url1'])
    indexes = results[1]

    # result1 = "{}: {}\n".format(df['Strain'][indexes[0][0]],df['Description'][indexes[0][0]])
    # result2 = "{}: {}".format(df['Strain'][indexes[0][1]],df['Description'][indexes[0][1]])

    result1 = "{}".format(df['title'][indexes[0][0]])
    result2 = "{}".format(df['title'][indexes[0][1]])
    result3 = "{}".format(df['title'][indexes[0][2]])
    result4 = "{}".format(df['title'][indexes[0][3]])
    result5 = "{}".format(df['title'][indexes[0][4]])
    # result2 = "{}".format(df['Strain'][indexes[0][1]])

    return result1,result2,result3,result4,result5