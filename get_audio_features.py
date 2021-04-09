"""
Find the audio features for each song when provided its Spotify Track ID. The
ID is used to find the corresponding audio features for each song through the
Spotify API. Do this for all the relevant Billboard Hot 100 Songs to be
analyzed.
"""

# Import the required libraries.
import pandas as pd
import requests
from tqdm import tqdm

# Import the authentication details from spotify_id_query in order to avoid
# repeating the authentication process.
from spotify_id_query import BASE_URL, headers

def find_audio_features(id_dataframe):
    """
    Return a dataframe containing the Date, Song, Artist and Spotify Track ID,
    and various audio features for every searchable song on Billboard Hot 100
    over the past 60 years.

    Use the Spotify Track IDs to find the corresponding audio features for that
    track. A maximum of 100 IDs can be queried in one request, and this enables
    us to speed up the feature querying significantly. The resulting data is
    arranged into a pandas dataframe containing the input dataframe plus
    columns for each of the audio features provided by Spotify.

    Args:
        id_dataframe: A Pandas dataframe, imported from spotify_id_query, that
        contains the Billboard Hot 100 songs on the June 1st of every year from
        1961 to 2020 as well as their corresponding Spotify Track IDs. The
        dataframe has four columns: Date, Song, Artist, and Track ID. Each row
        represents one song.

    Returns:
        song_audio_dataframe: A Pandas dataframe that contains the Billboard
        Hot 100 songs on the June 1st of every year from 1961 to 2020 with
        their corresponding Spotify Track IDs and Spotify-generated audio
        features. The dataframe has twenty four columns: Date, Song, Artist,
        Track ID, and the remaining columns represent various audio features.
        Each row represents one song.
    """
    # Convert the Track ID column in the dataframe to a list.
    track_id_master = id_dataframe["Track ID"].tolist()

    # Initialise the dataframe that stores the audio features by finding the
    # audio features for the first track ID.
    audio_dataframe = id_to_audio_feature([track_id_master[0]])

    # Break up the list of track IDs into a list containing sbulists with 100
    # IDs each.
    track_id_master_split = [track_id_master[i:i+100] for i in range(1, \
    len(track_id_master), 100)]

    # Loop through each sublist.
    for list_section in tqdm(track_id_master_split):

        # Extract the audio features for the 100 (or less) songs in the sublist
        # as a dataframe, and append to the main audio feature dataframe.
        dataframe_section = id_to_audio_feature(list_section)
        audio_dataframe = audio_dataframe.append(dataframe_section, \
        ignore_index=True)

    # Concatenate the dataframe containing the date, song, artist, and track ID
    # with the dataframe containing the corresponding audio features.
    song_audio_dataframe = pd.concat([id_dataframe, audio_dataframe], axis=1)
    return song_audio_dataframe

def id_to_audio_feature(track_id_list):
    """
    Return a dataframe containing the audio features for each of the input
    Spotify Track IDs.

    Query the list of track IDs in one big GET request to the Spotify API.
    Convert and index the resulting data to form a dataframe with the relevant
    audio features (around 20 for each track).

    Args:
        track_id_list: A list containing the Spotify IDs as strings. Can have a
        maximum length of 100, but occasionally can be shorter.

    Returns:
        audio_data_clean: A Pandas dataframe containing the audio features for
        each of the IDs in the input list.
    """
    # Concatenate the list of Track IDs into a single, comma-separated string.
    track_id_string = ",".join(track_id_list)

    # Send GET request to Spotify API using the string of comma-separated Track
    # IDs.
    query_data = requests.get(BASE_URL + 'audio-features/?ids=' + \
    track_id_string, headers=headers)

    # Convert the response to a JSON file.
    query_data = query_data.json()

    # Restructure JSON file into a Pandas dataframe.
    audio_data = pd.DataFrame.from_dict(query_data)
    audio_data_clean = pd.json_normalize(audio_data['audio_features'])
    return audio_data_clean
