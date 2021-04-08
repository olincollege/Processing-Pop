import pytest
import datetime
import pandas as pd
from billboard_scraper import clean_artist

from spotify_id_query import (
    query_track,
    query_all_tracks
)

from music_feature import (
    average_by_date
    average_all
    key_proportion
)


clean_artist_cases = [
    # Test empty string returns itself
    ("", ""),
    # Test that a clean lowercase name returns itself
    ("steve", "steve"),
    # Test multiple clean lowercase words return itself
    ("justin bieber", "justin bieber"),
    # Test that an uppercase name returns lowercase of itself
    ("JUSTIN", "justin"),
    # Test that a list of all clutterers gets replaced by a space for each
    (".&featuring and +? x feat", "        "),
    # Test that a cluttered uppercase phrase is correctly cleaned
    ("Benji & Vedaant", "benji   vedaant"),
    # Test that capitalized "FEAT" is removed
    ("benji FEAT vedaant", "benji   vedaant")
]

query_track_cases = [
    # Test if a blank string for title and artist returns "Error: Not in
    # Spotify"
    ("","", "Error: Not in Spotify"),
    # Test that a valid song title and artist returns the correct ID
    ("Halo", "Beyonce", "4JehYebiI9JE8sR8MisGVb"),
    # Test that a valid title and noisy artist name returns "Error: Not in
    # Spotify"
    ("Montero", "Lil ndfkoadsjif X", "Error: Not in Spotify"),
    # Test that a noisy title and valid artist name returns "Error: Not in
    # Spotify"
    ("asdjflasjdf", "Lil Nas X", "Error: Not in Spotify")
]

# Construct test DataFrames for average_by_date(), average_all(), and key_proportion()
test_dict_1 = {"Date": ["6/1/2020"], "Loudness": [0.1]}
test_dataframe_1 = pd.DataFrame(test_average_dict)
single_average_dict_1 = {"Date": [datetime.date(6,1,2020)], "Feature": ["Loudness"], "Average": [0.1], }
single_average_dataframe_1 = pd.DataFrame(single_average_dict_1)

test_dict_2 = {"Date": ["6/1/2020", "6/1/2020"], "Loudness": [0.1, 0.3]}
test_dataframe_1 = pd.DataFrame(test_average_dict)
single_average_dict_1 = {"Date": [datetime.date(6,1,2020)], "Feature": ["Loudness"], "Average": [0.2], }
single_average_dataframe_1 = pd.DataFrame(single_average_dict_1)

test_dict_1 = {"Date": ["6/1/2020", "6/1/2019"], "Loudness": [0.1, 0.3]}
test_dataframe_1 = pd.DataFrame(test_average_dict)
single_average_dict_1 = {"Date": [datetime.date(6,1,2019), datetime.date(6,1,2020)], "Feature": ["Loudness", "Loudness"], "Average": [0.1, 0.3]}
single_average_dataframe_1 = pd.DataFrame(single_average_dict_1)

average_by_date_cases = [
    # Test that a single year, single item dataframe yields the correct average
    (2020, 2020, "Loudness", test_dataframe_1, single_average_dataframe_1)
    # Test that a single year, multiple item dataframe yields the correct average
    (2020, 2020, "Loudness", test_dataframe_2, single_average_dataframe_2)
    # Test that a multiple year, single item dataframe yields correct average
    (2019, 2020, "Loudness", test_dataframe_2, single_average_dataframe_2)
]

@pytest.mark.parametrize("artist,cleaned_artist", clean_artist_cases)
def test_clean_artist(artist, cleaned_artist):
    assert clean_artist(artist) == cleaned_artist


@pytest.mark.parametrize("title,artist,track_id", query_track_cases)
def test_query_track(title, artist, track_id):
    assert query_track(title, artist) == track_id

