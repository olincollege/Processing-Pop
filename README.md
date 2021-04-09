# Popus-Songus
## Processing Pop History
A computational essay on tracking the history of multiple different musical features over the last 60 years.
We used a Billboard scraper in addition to Spotify's API to obtain over 6000 Songs and Spotify's algorithmically determined [features](https://developer.spotify.com/documentation/web-api/reference/#category-tracks). With that data, we visualized the change in these features.

## Dependencies
Our project uses the following libraries:
* Pandas
* Datetime
* Requests
* Pytest
* TQDM
* Billboard.py
* Plotly

To install these libraries, use the following code in your terminal emulator:
```
pip install pandas datetime requests pytest tqdm billboard.py plotly
```
## Necessary Changes
We have provided our dataset as a CSV which you can load without any changes to the jupyter notebook. However, if you would like to generate the data from scratch (not recommended as it takes quite long and Spotify occasionally fails), you can use the following directions:

### Sign up for API token
Spotify requires that you sign in with a client and secret ID. Follow the instructions here: https://developer.spotify.com/dashboard/login to obtain a client and secret ID.

### Create id files
Create a file named client_id.txt and paste your client ID in with a new line directly after. Create a file named secret_id.txt and do the same with your secret ID.

### Uncomment Code
In the Jupyter notebook, uncomment the code following these headings:
* What is popular music?
* What are musical features?
* Finding the song in Spotify

In addition, to use the data you have generated, comment out the lines under "Finding Averages" which the comments tell you to.


## Using Jupyter Notebooks (Important)
Some elements do not work in Jupyter Labs:
* TQDM
* Plotly

Please run in VSCode or if necessary Jupyter Notebooks
Warning: Ignore TQDM errors in Jupyter Notebooks, TQDM only works in VSCode.


## Plotting
We used Plotly (in particular, plotly express) to graph our data. Because we stored our data in Dataframes, no further processing is required past our averaging functions run in the Jupyter Notebook.
**Resource for generating similar line plots to ours:**
https://plotly.com/python/line-charts/
**Resource for generating a similar bar graph:**
https://plotly.com/python/bar-charts/



## Project Creators:

Vedaant Kuchhal and Benji Pugh

*Olin College Software Design Spring 2021*
