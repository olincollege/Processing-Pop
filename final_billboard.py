"""
Web scrape through the Billboard website to find the Billboard Hot hundred
playlist for each year from 1958 to 2021. To do so, we use an externally
downloaded python library called 'billboard' that interacts with the Billboard
API.
"""

# Imports the required libraries.
import billboard
import pandas as pd
import datetime

"""
Return the Billboard Hot Hundred playlists for each year within the specified
start and end years.

Loop through the first day of June for each year of the specified time
period, and extract the list of Billboard Hot Hundred songs on that date. This
list is extracted by using the python library 'billboard'. All the various list
of Hot Hundred songs for each year are then returned as one big dataframe.

Args:
    year_start: An integer between 1958 and 2021 that contains the starting
    year of the time period for which the Billboard Hot 100 charts are queried.

    year_end: An integer between 1958 and 2021 that must be greater than or
    equal to year_start that contains the ending year of the time period for
    which the Billboard Hot 100 charts are queried.

Returns:
    A pandas dataframe containing columns with the Date, Song, and Artist for
    every Billboard Hot 100 Song on June 1st of the years specified.

"""
def hot_100_data(year_start, year_end):


    all_hot_100 = pd.DataFrame(columns=["Date", "Song", "Artist"])

    for year in range(year_start, year_end + 1, 1):
        current_date = datetime.date(year, 6, 1)
        current_chart = \
        billboard.ChartData("hot-100", date=current_date).entries
        for song in current_chart:
            all_hot_100 = all_hot_100.append({"Date": current_date, \
            "Song": song.title, "Artist": song.artist}, ignore_index=True)

    return all_hot_100
