import pandas as pd
import datetime
import plotly.graph_objs as go

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`
def cleandata():
    """
    
    """
    
    
    
    

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """
    listings = pd.read_csv("data/listings.csv")
    
    graph_one = []    
    graph_one.append(
      go.Histogram(
      x = listings['host_since'].apply(lambda x: (datetime.datetime.today() - pd.to_datetime(x)).days/365)
      )
    )

    layout_one = dict(title = 'Years of hosting experience',
                )

    
    graph_two = []

    graph_two.append(
      go.Scatter(
      x = listings['review_scores_value'],
      y = listings['price'],
      mode='markers')
    )

    layout_two = dict(title = 'Scatter plot of review scores and prices',
                xaxis = dict(title = 'review score'),
                yaxis = dict(title = 'price'),
                )

    
    top_10_neighborhoods = listings.groupby('neighbourhood_cleansed').count()['id'].sort_values(ascending=False)[:10]
    graph_three = []
    graph_three.append(
      go.Bar(
      x = list(top_10_neighborhoods.index),
      y = list(top_10_neighborhoods)
      )
    )

    layout_three = dict(title = 'Neighborhood with the most listings',
                xaxis = dict(title = 'neighborhood'),
                yaxis = dict(title = 'numbers of listings')
                       )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))

    return figures