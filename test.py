"""
Used to test all the functions across different files in our code that are
possible to test.
"""
import datetime
import pytest
import pandas as pd
from billboard_scraper import clean_artist

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
single_average_dict_1 = {"Date": [datetime.date(2020, 6, 1)], "Feature": \
["Loudness"], "Average": [0.1], }
single_average_dataframe_1 = pd.DataFrame(single_average_dict_1)


test_dict_2 = {"Date": [str(datetime.date(2020, 6, 1)), \
str(datetime.date(2020, 6, 1))], "Loudness": [0.1, 0.3]}
test_dataframe_2 = pd.DataFrame(test_dict_2)
single_average_dict_2 = {"Date": [datetime.date(2020, 6, 1)], "Feature": \
["Loudness"], "Average": [0.2], }
single_average_dataframe_2 = pd.DataFrame(single_average_dict_2)

test_dict_3 = {"Date": [str(datetime.date(2020, 6, 1)), \
str(datetime.date(2019, 6, 1))], "Loudness": [0.1, 0.3]}
test_dataframe_3 = pd.DataFrame(test_dict_3)
single_average_dict_3 = {"Date": [datetime.date(2019, 6, 1), \
datetime.date(2020, 6, 1)], "Feature": ["Loudness", "Loudness"], \
"Average": [0.3, 0.1]}
single_average_dataframe_3 = pd.DataFrame(single_average_dict_3)

test_dict_4 = {"Date": [str(datetime.date(2020, 6, 1)), \
str(datetime.date(2019, 6, 1))], "Loudness": [0.4, 0.5]}
test_dataframe_4 = pd.DataFrame(test_dict_4)
single_average_dict_4 = {"Date": [datetime.date(2020, 6, 1)], \
"Feature": ["Loudness"], "Average": [0.4]}
single_average_dataframe_4 = pd.DataFrame(single_average_dict_4)

test_dict_5 = {"Date": [str(datetime.date(2020, 6, 1)),\
str(datetime.date(2020, 6, 1)), str(datetime.date(2019, 6, 1)),\
str(datetime.date(2019, 6, 1))], "Loudness": [0.4, 0.6, 0.3, 0.5]}
test_dataframe_5 = pd.DataFrame(test_dict_5)
single_average_dict_5 = {"Date": [datetime.date(2019, 6, 1),\
datetime.date(2020, 6, 1)], "Feature": ["Loudness", "Loudness"], \
"Average": [0.4,0.5]}
single_average_dataframe_5 = pd.DataFrame(single_average_dict_5)

average_by_date_cases = [
    # Cannot take average of no numbers (and is outlined in Docstring), so no
    # testing empty dataframes.
    # Test that a single year, single item dataframe yields the correct average
    (2020, 2020, "Loudness", test_dataframe_1, single_average_dataframe_1),
    # Test that single year, multiple item dataframe yields the correct average
    (2020, 2020, "Loudness", test_dataframe_2, single_average_dataframe_2),
    # Test that a multiple year, single item dataframe yields correct averages
    (2019, 2020, "Loudness", test_dataframe_3, single_average_dataframe_3),
    # Test that limiting the range of years limits the results in a multi year
    # dataframe
    (2020, 2020, "Loudness", test_dataframe_4, single_average_dataframe_4),
    # Test that a multiple year multiple item dataframe yields correct averages
    (2019, 2020, "Loudness", test_dataframe_5, single_average_dataframe_5)
]

# Construct test DataFrames for average_by_date()
test_dict_6 = {"Date": [str(datetime.date(2020, 6, 1))], "Loudness": [0.1], \
"Duration": [5.0]}
test_dataframe_6 = pd.DataFrame(test_dict_6)
multi_average_dict_6 = {"Date": [datetime.date(2020, 6, 1), \
datetime.date(2020, 6, 1)], "Feature": ["Loudness", "Duration"], \
"Average": [0.1, 5.0]}
multi_average_dataframe_6 = pd.DataFrame(multi_average_dict_6)

test_dict_7 = {"Date": [str(datetime.date(2019, 6, 1)), \
str(datetime.date(2019, 6, 1)), str(datetime.date(2020, 6, 1)), \
str(datetime.date(2020, 6, 1))], "Loudness": [0.1, 0.3, 0.8, 1.0], \
"Duration": [5.0, 7.0, 30.0, 40.0]}

test_dataframe_7 = pd.DataFrame(test_dict_7)
multi_average_dict_7 = {"Date": [datetime.date(2019, 6, 1), \
datetime.date(2020, 6, 1), datetime.date(2019, 6, 1), \
datetime.date(2020, 6, 1)], "Feature": ["Loudness", "Loudness", "Duration", \
"Duration"], "Average": [0.2, 0.9, 6.0, 35.0]}
multi_average_dataframe_7 = pd.DataFrame(multi_average_dict_7)

average_all_cases = [
    # Test that a single year, single feature, single item dataframe yields the
    # correct average
    (2020, 2020, ["Loudness"], test_dataframe_1, single_average_dataframe_1),
    # Test that a single year, multiple feature, singe item dataframe yields
    # the correct averages
    (2020, 2020, ["Loudness", "Duration"], test_dataframe_6, \
    multi_average_dataframe_6),
    # Test that multiple year, multiple feature, multiple item dataframe yields
    (2019, 2020, ["Loudness", "Duration"], test_dataframe_7, \
    multi_average_dataframe_7),
    # Since this function calls average_by_date, there isn't very much need to
    # test the specifics of individual behaviors.
]

# Construct test DataFrames for key_proportion()
test_dict_8 = {"Date": [str(datetime.date(2020, 6, 1))], "key": [0], \
"duration":[5]}
test_dataframe_8 = pd.DataFrame(test_dict_8)
key_dict_8 = {"Date": [str(datetime.date(2020, 6, 1))], "Key": ["C"], \
"Count": [1], "Proportion":[1.0]}
key_dataframe_8 = pd.DataFrame(key_dict_8)

test_dict_9 = {"Date": [str(datetime.date(2020, 6, 1)), \
str(datetime.date(2019, 6, 1))], "key": [0,2], "duration":[5,5]}
test_dataframe_9 = pd.DataFrame(test_dict_9)
key_dict_9 = {"Date": [str(datetime.date(2019, 6, 1)), \
str(datetime.date(2020, 6, 1))], "Key": ["D", "C"], "Count": [1, 1], \
"Proportion":[1.0, 1.0]}
key_dataframe_9 = pd.DataFrame(key_dict_9)

test_dict_10 = {"Date": [str(datetime.date(2020, 6, 1)), \
str(datetime.date(2020, 6, 1)), str(datetime.date(2019, 6, 1))], \
"key": [0,2,2], "duration":[5,5,5]}
test_dataframe_10 = pd.DataFrame(test_dict_10)
key_dict_10 = {"Date": [str(datetime.date(2019, 6, 1)), \
str(datetime.date(2020, 6, 1)), str(datetime.date(2020, 6, 1))], \
"Key": ["D", "C", "D"], "Count": [1, 1, 1], "Proportion":[1.0, 0.5,0.5]}
key_dataframe_10 = pd.DataFrame(key_dict_10)

test_dict_11 = {"Date": [str(datetime.date(2020, 6, 1)), \
str(datetime.date(2020, 6, 1))], "key": [0,0], "duration":[5,5]}
test_dataframe_11 = pd.DataFrame(test_dict_11)
key_dict_11 = {"Date": [str(datetime.date(2020, 6, 1))], \
"Key": ["C"], "Count": [2], "Proportion":[1.0]}
key_dataframe_11 = pd.DataFrame(key_dict_11)



key_proportion_cases = [
    # Test that a single key in a single year returns a proportion of 1.0
    (2020, 2020, test_dataframe_8, key_dataframe_8),
    # Test that a single key in multiple years returns correctly
    (2019, 2020, test_dataframe_9, key_dataframe_9),
    # Test that multiple keys in multiple years returns correctly
    (2019, 2020, test_dataframe_10, key_dataframe_10),
    # Test that a single repeated key returns a proportion of 1.0
    (2020, 2020, test_dataframe_11, key_dataframe_11)
]

# Test clean_artist()
@pytest.mark.parametrize("artist,cleaned_artist", clean_artist_cases)
def test_clean_artist(artist, cleaned_artist):
    """
    Check that the artist's name(s) is formatted and cleaned correctly.

    A set of clutter strings such as 'x' or 'featuring' often obscure the
    artists' names and make the songs difficult to keyword search. Hence, these
    are removed appropriately.

    args:
        artist: A string containing the unformatted artist's name.
        cleaned_artist: A string containing the artist;s name after it has been
        appropriately formatted.
    """
    assert clean_artist(artist) == cleaned_artist

# Test average_by_date
@pytest.mark.parametrize("start_date,end_date,feature,\
song_dataframe,date_average", average_by_date_cases)
def test_average_by_date(start_date, end_date, feature, song_dataframe, \
date_average):
    """
    Check the yearly averages for a specified feature are correctly calculated
    for a dataframe over the specified period.

    The average value of an audio feature is calculated per year by taking the
    sum of the features' numeric values and dividing by the number of tracks.

    args:
        start_date: An integer between 1958 and 2021 that contains the starting
        year of the time period for which the audio feature is averaged.

        end_date: An integer between 1958 and 2021 that must be greater than or
        equal to start_date that contains the ending year of the time period
        for which the audio feature is averaged.

        feature: A string that specifies the name of the feature to be averaged
        such as 'duration_ms' or 'instrumentalness'.

        song_dataframe: A Pandas dataframe that contains the Billboard
        Hot 100 songs on the June 1st of every year from 1961 to 2020 with
        their corresponding Spotify Track IDs and Spotify-generated audio
        features. The dataframe has twenty four columns: Date, Song, Artist,
        Track ID, and the remaining columns represent various audio features.
        Each row represents one song.

        date_average: A Panda dataframe containing the calculated averages in
        the correct structure.
    """
    assert average_by_date(start_date, end_date, feature, song_dataframe).\
    equals(date_average)

# Test average_all
@pytest.mark.parametrize("start_date,end_date,features,song_dataframe,\
date_average", average_all_cases)
def test_average_all(start_date, end_date, features, song_dataframe, \
date_average):
    """
    Check the yearly averages for a list of specified features are correctly
    calculated for a dataframe over the specified period.

    The average value of an audio feature is calculated per year by taking the
    sum of the features' numeric values and dividing by the number of tracks.

    args:
        start_date: An integer between 1958 and 2021 that contains the starting
        year of the time period for which the audio features are averaged.

        end_date: An integer between 1958 and 2021 that must be greater than or
        equal to start_date that contains the ending year of the time period
        for which the audio features are averaged.

        features: A list of strings that specifies the names of the features to
        be averaged, such as ['duration_ms', 'instrumentalness'].

        song_dataframe: A Pandas dataframe that contains the Billboard
        Hot 100 songs on the June 1st of every year from 1961 to 2020 with
        their corresponding Spotify Track IDs and Spotify-generated audio
        features. The dataframe has twenty four columns: Date, Song, Artist,
        Track ID, and the remaining columns represent various audio features.
        Each row represents one song.

        date_average: A Panda dataframe containing the calculated averages in
        the correct structure.
    """
    assert average_all(start_date, end_date, features, song_dataframe).\
    equals(date_average)

# Test key_proportion()
@pytest.mark.parametrize("start_date,end_date,song_dataframe,key_dataframe", \
key_proportion_cases)
def test_key_proportion(start_date, end_date, song_dataframe, key_dataframe):
    """
    Check the yearly counts for the number of songs of a particular key, and
    their relative proportion to all the songs that year.

    Count over each key for each year, and divide by the total count for each
    year to give the relative proportion of the keys that year.

    args:
        start_date: An integer between 1958 and 2021 that contains the starting
        year of the time period for which the audio feature is averaged.

        end_date: An integer between 1958 and 2021 that must be greater than or
        equal to start_date that contains the ending year of the time period
        for which the audio feature is averaged.

        song_dataframe: A Pandas dataframe that contains the Billboard
        Hot 100 songs on the June 1st of every year from 1961 to 2020 with
        their corresponding Spotify Track IDs and Spotify-generated audio
        features. The dataframe has twenty four columns: Date, Song, Artist,
        Track ID, and the remaining columns represent various audio features.
        Each row represents one song.

        date_average: A Panda dataframe containing the total counts and
        proportions of each of the keys for each of the years.
    """
    assert key_proportion(start_date, end_date, song_dataframe).\
    equals(key_dataframe)
