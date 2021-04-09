import pytest
import datetime
import pandas as pd
from billboard_scraper import clean_artist

from spotify_id_query import (
    query_track,
    query_all_tracks
)

from music_feature import (
    average_by_date,
    average_all,
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

# Construct test DataFrames for average_by_date()
test_dict_1 = {"Date": [str(datetime.date(2020, 6, 1))], "Loudness": [0.1]}
test_dataframe_1 = pd.DataFrame(test_dict_1)
single_average_dict_1 = {"Date": [datetime.date(2020, 6, 1)], "Feature": ["Loudness"], "Average": [0.1], }
single_average_dataframe_1 = pd.DataFrame(single_average_dict_1)

test_dict_2 = {"Date": [str(datetime.date(2020, 6, 1)), str(datetime.date(2020, 6, 1))], "Loudness": [0.1, 0.3]}
test_dataframe_2 = pd.DataFrame(test_dict_2)
single_average_dict_2 = {"Date": [datetime.date(2020, 6, 1)], "Feature": ["Loudness"], "Average": [0.2], }
single_average_dataframe_2 = pd.DataFrame(single_average_dict_2)

test_dict_3 = {"Date": [str(datetime.date(2020, 6, 1)), str(datetime.date(2019, 6, 1))], "Loudness": [0.1, 0.3]}
test_dataframe_3 = pd.DataFrame(test_dict_3)
single_average_dict_3 = {"Date": [datetime.date(2019, 6, 1), datetime.date(2020, 6, 1)], "Feature": ["Loudness", "Loudness"], "Average": [0.3, 0.1]}
single_average_dataframe_3 = pd.DataFrame(single_average_dict_3)

test_dict_4 = {"Date": [str(datetime.date(2020, 6, 1)), str(datetime.date(2019, 6, 1))], "Loudness": [0.4, 0.5]}
test_dataframe_4 = pd.DataFrame(test_dict_4)
single_average_dict_4 = {"Date": [datetime.date(2020, 6, 1)], "Feature": ["Loudness"], "Average": [0.4]}
single_average_dataframe_4 = pd.DataFrame(single_average_dict_4)

test_dict_5 = {"Date": [str(datetime.date(2020, 6, 1)),\
str(datetime.date(2020, 6, 1)), str(datetime.date(2019, 6, 1)),\
str(datetime.date(2019, 6, 1))], "Loudness": [0.4, 0.6, 0.3, 0.5]}
test_dataframe_5 = pd.DataFrame(test_dict_5)
single_average_dict_5 = {"Date": [datetime.date(2019, 6, 1),\
datetime.date(2020, 6, 1)], "Feature": ["Loudness", "Loudness"], "Average": [0.4,0.5]}
single_average_dataframe_5 = pd.DataFrame(single_average_dict_5)

average_by_date_cases = [
    # Cannot take average of no numbers (and is outlined in Docstring), so no
    # testing empty dataframes.
    # Test that a single year, single item dataframe yields the correct average
    (2020, 2020, "Loudness", test_dataframe_1, single_average_dataframe_1),
    # Test that a single year, multiple item dataframe yields the correct average
    (2020, 2020, "Loudness", test_dataframe_2, single_average_dataframe_2),
    # Test that a multiple year, single item dataframe yields correct averages
    (2019, 2020, "Loudness", test_dataframe_3, single_average_dataframe_3),
    # Test that limiting the range of years limits the results in a multi year dataframe
    (2020, 2020, "Loudness", test_dataframe_4, single_average_dataframe_4),
    # Test that a multiple year, multiple item dataframe yields correct averages
    (2019, 2020, "Loudness", test_dataframe_5, single_average_dataframe_5)
]

# Construct test DataFrames for average_by_date()
test_dict_6 = {"Date": [str(datetime.date(2020, 6, 1))], "Loudness": [0.1], "Duration": [5.0]}
test_dataframe_6 = pd.DataFrame(test_dict_6)
multi_average_dict_6 = {"Date": [datetime.date(2020, 6, 1), \
datetime.date(2020, 6, 1)], "Feature": ["Loudness", "Duration"], "Average": [0.1, 5.0]}
multi_average_dataframe_6 = pd.DataFrame(multi_average_dict_6)

test_dict_7 = {"Date": [str(datetime.date(2019, 6, 1)), str(datetime.date(2019, 6, 1)), str(datetime.date(2020, 6, 1)), str(datetime.date(2020, 6, 1))], "Loudness": [0.1, 0.3, 0.8, 1.0], "Duration": [5.0, 7.0, 30.0, 40.0]}
test_dataframe_7 = pd.DataFrame(test_dict_7)
multi_average_dict_7 = {"Date": [datetime.date(2019, 6, 1), datetime.date(2020, 6, 1), datetime.date(2019, 6, 1), datetime.date(2020, 6, 1)], "Feature": ["Loudness", "Loudness", "Duration", "Duration"], "Average": [0.2, 0.9, 6.0, 35.0]}
multi_average_dataframe_7 = pd.DataFrame(multi_average_dict_7)

average_all_cases = [
    # Test that a single year, single feature, single item dataframe yields the
    # correct average
    (2020, 2020, ["Loudness"], test_dataframe_1, single_average_dataframe_1),
    # Test that a single year, multiple feature, singe item dataframe yields
    # the correct averages
    (2020, 2020, ["Loudness", "Duration"], test_dataframe_6, multi_average_dataframe_6),
    # Test that multiple year, multiple feature, multiple item dataframe yields
    (2019, 2020, ["Loudness", "Duration"], test_dataframe_7, multi_average_dataframe_7),
    # Since this function calls average_by_date, there isn't very much need to test
    # the specifics of individual behaviors.
]

# Construct test DataFrames for key_proportion()
# test_dict_8 = {"Date": [str(datetime.date(2020, 6, 1))], "Key": ["A"]}
# test_dataframe_8 = pd.DataFrame(test_dict_8)
# single_average_dict_8 = {"Date": [datetime.date(2020, 6, 1)], "Key": ["A"], "Count": [1], "Proportion":}
# single_average_dataframe_8 = pd.DataFrame(single_average_dict_8)

# Test clean_artist()
@pytest.mark.parametrize("artist,cleaned_artist", clean_artist_cases)
def test_clean_artist(artist, cleaned_artist):
    assert clean_artist(artist) == cleaned_artist

# Test query_track()
@pytest.mark.parametrize("title,artist,track_id", query_track_cases)
def test_query_track(title, artist, track_id):
    assert query_track(title, artist) == track_id

# Test average_by_date
@pytest.mark.parametrize("start_date,end_date,feature,song_dataframe,date_average", average_by_date_cases)
def test_average_by_date(start_date, end_date, feature, song_dataframe, date_average):
    assert average_by_date(start_date, end_date, feature, song_dataframe).equals(date_average)

# Test average_all
@pytest.mark.parametrize("start_date,end_date,features,song_dataframe,date_average", average_all_cases)
def test_average_all(start_date, end_date, features, song_dataframe, date_average):
    assert average_all(start_date, end_date, features, song_dataframe).equals(date_average)

