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
from tqdm.autonotebook import tqdm

def hot_100_data(year_start, year_end):
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

    # Create an empty dataframe to store all the Billboard Hot 100 songs. The
    # datapoints stored for each song is the date it featured on the Billboard
    # Hot 100, the song's name, and the artist's name(s).
    all_hot_100 = pd.DataFrame(columns=["Date", "Song", "Artist"])

    # Loop over each year in the specified time period.
    for year in tqdm(range(year_start, year_end + 1, 1)):

        # Isolates the Billboard Hot 100 list on June 1st of that year.
        current_date = datetime.date(year, 6, 1)
        current_chart = \
        billboard.ChartData("hot-100", date=current_date).entries

        # Loops through each song and 'cleans' the artist name of unnecessary
        # symbols.
        for song in current_chart:
            artist = clean_artist(song.artist)
            all_hot_100 = all_hot_100.append({"Date": current_date, \
            "Song": song.title, "Artist": artist}, ignore_index=True)

    return all_hot_100


def clean_artist(artist):
    """
    Return the artist name in a reformatted form that is consistent across all
    songs that feature multiple artists.

    Convert the artists' names to lowercase, and remove strings such as ".", "&",
    "featuring ", "and ", "+", "?", "x ", and "feat", replacing them with
    whitespace. This makes it easier to keyword search the tracks in the Spotify
    API later on.

    Args:
        artist: A string containing the name(s) of the artist(s) who perform or are
        featured in any track.

    Returns:
        A string containing the reformatted name(s) of the artist(s) in lowercase
        without the unnecessary and confusing symbols used when there are multiple
        artists.

    """
    cleaned_artist = artist.lower()
    # Define the substrings that must be cleaned from the artists' name.
    CLUTTERERS = [".", "&", "featuring ", "and ", "+", "?", " x ", "feat"]

    # Cleans out the artist's name by removing the substrings specified above.
    for item in CLUTTERERS:
        cleaned_artist = cleaned_artist.replace(item, " ")
    return cleaned_artist
