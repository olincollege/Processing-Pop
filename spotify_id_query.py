"""
Find the unique Spotify Track IDs for each song in the Billboard Hot 100 lists.
Do this by keyword searching each song in the Spotify API. Some songs do not
yield results in Spotify hence the final number of Track IDs obtained will be
less than the number of songs queried.
"""

# Import the required libraries.
import time
import pandas as pd
import requests
from tqdm import tqdm


# The Track IDs are queried using GET requests to the Spotify API, and these
# requests require Authorization in the form of client and secret IDs that
# are specific to the user accessing the API (and stored in external text files
# because these must not be publicly shared.) These text files are not provided
# in the repository and must be created independently and named as illustrated
# in the code below.


#Get the client and secret IDs from files stored and remove the newline
with open('client_id.txt') as f:
    CLIENT_ID = str(f.read())
CLIENT_ID = CLIENT_ID[0:-1]

with open('secret_id.txt') as f:
    CLIENT_SECRET = str(f.read())
CLIENT_SECRET = CLIENT_SECRET[0:-1]

# URL used to create an access token.
AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# Convert the response to JSON.
auth_response_data = auth_response.json()

# Save the access token.
access_token = auth_response_data['access_token']

# Define the GET request headers.
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

# Base URL of all Spotify API endpoints.
BASE_URL = 'https://api.spotify.com/v1/'


def query_track(title, artist):
    """
    Return the Spotify Track ID of a given song title and artist.

    Each unique song consists of its title and the artist performing it.
    Concatenate these and query in the the Spotify API by using a GET request.
    Convert the GET request's response and appropriately index to find the
    Track ID. If GET request fails, print error and repeat until successful.

    Args:
        title: A string containing the title of the song to be queried.
        artist: A string containing the name(s) of the artist(s) performing
        and/or featured in the song.

    Returns:
        track_id: A string containing the unique Spotify Track ID for the song.
    """
    # Send GET request to Spotify API using the song title and artist as
    # keyword searches.
    response = requests.get(BASE_URL + 'search', params={"q": \
    f"{title} {artist}", "type": "track", "limit": 1}, headers=headers)

    # Catch GET request failure. Print, pause, and repeat action until the
    # request succeeds.
    while response.status_code != 200:
        print("Failed Spotify Request")
        time.sleep(1)
        response = requests.get(BASE_URL + 'search', params={"q": \
        f"{title} {artist}", "type": "track", "limit": 1}, headers=headers)

    # Convert the response to a JSON file.
    response = response.json()

    # Check that GET request doesn't return empty.
    if response["tracks"]["items"] == []:
        return "Error: Not in Spotify"

    # Index the JSON file appropriately to find the Track ID
    track_id = response["tracks"]["items"][0]["id"]

    return track_id

def query_all_tracks(track_dataframe):
    """
    Return a dataframe containing the Date, Song, Artist and Spotify Track ID
    for every searchable song on Billboard Hot 100 over the past 60 years.

    Use the songs (title) and artists stored in the input dataframe to find the
    corresponding Spotify Track IDs using keyword searches involving GET
    requests to the Spotify API (see the documentation of query_track). Store
    the results in another dataframe containing the input dataframe plus an
    additional column containing the Spotify Track IDs for each song.

    Args:
        track_dataframe: A Pandas dataframe, imported from billboard_scraper,
        that contains the Billboard Hot 100 songs on the June 1st of every year
        from 1961 to 2020. The dataframe has three columns: Date, Song, and
        Artist, and each row represents one song. Note: 'Date' refers to the
        date of featuring on Billboard Hot 100, NOT the release date, while
        'Song' refers to the song's title.

    Returns:
        id_dataframe: A Pandas dataframe that contains the Billboard Hot 100
        songs on the June 1st of every year from 1961 to 2020 as well as their
        corresponding Spotify Track IDs. The dataframe has four columns: Date,
        Song, Artist, and Track ID. Each row represents one song.
    """
    # Declare an empty dataframe with the appropriate columns.
    id_dataframe = pd.DataFrame(columns=["Date", "Song", "Artist", "Track ID"])

    # Loop through each row in the dataframe (i.e. each song).
    for _, data in tqdm(track_dataframe.iterrows()):

        # Query the Track ID for the current song and artist.
        current_id = query_track(data["Song"], data["Artist"])

        # Only append Track ID to the dataframe if the error message is not
        # returned.
        if current_id != "Error: Not in Spotify":
            id_dataframe = id_dataframe.append({"Date": data["Date"], \
            "Song": data["Song"], "Artist": data["Artist"], \
            "Track ID" : current_id}, ignore_index=True)
    return id_dataframe
