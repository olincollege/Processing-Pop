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

Loop through the first day of the January for each year of the specified time
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
    A pandas dataframe where each column contains the Billboard Hot Hundred
    chart for a particular date (in this case, the first day of each month in
    the specified time period).

"""
def hot_100_data(year_start, year_end):

    # Declare an empty dictionary that will store all the data.
    hot_100_by_date_dict = {}

    # Loop through every month of every year in the specified range.
    for year in range(year_start, year_end + 1):
        current_date = datetime.date(year, 1, 1)

        # Extract the Billboard Hot Hundred chart for the specific date.
        current_chart = \
        billboard.ChartData("hot-100", date=current_date).entries

        # Convert the data into a more readable format
        hot_100_by_date_dict[current_date] = convert_chart(current_chart)
    hot_100_by_date = pd.DataFrame(hot_100_by_date_dict)
    return hot_100_by_date


"""
A helper function to hot_100_data. Return a Billboard Hot Hundred chart as a
list.

Convert the data in each track from a billboard library-specific 'track object'
to a dictionary containing the track's title and artist.

Args:
    current_chart: A list of 'track objects'.

Returns:
    A list of dictionaries, each dictionary containing a track's title and
    artist.
"""
def convert_chart(current_chart):

    # Declare an empty list that will store the data for that chart.
    chart_list = []

    # Loop through each entry, and convert it into a dictionary.
    for chart_entry in current_chart:
        chart_list.append({"title": chart_entry.title, "artist": chart_entry.artist})
    return chart_list
