"""
Process the audio feature data so that it can be plotted appropriately. This
involves thaking averages of various metrics, and counting and summing other
features.
"""

# Import the required libraries.
import datetime
import pandas as pd
from tqdm.autonotebook import tqdm

def average_by_date(start_date, end_date, feature, song_dataframe):
    """
    Return a dataframe containing the average values of a given feature for all
    the songs in each year.

    Calculate the numerical average (mean) of the values of the input feature
    type for all of the songs in a given year, looped over each year in the
    specified time period. Count and sum through the entire dataframe of songs
    for a feature, and construct a dataframe of the results.

    Args:
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

    Returns:
        average_by_date: A Pandas dataframe that contains the Date (of
        featuring on Billboard Hot 100), Feature (audio feature by Spotify),
        and Average (the numerical value of a particular audio feature for all
        the songs in a given year) for each of the years in the range specified.
    """
    # Declare an empty dataframe with the appropriate columns.
    feature_average = pd.DataFrame(columns=["Date", "Feature", "Average"])

    # Loop through each year in the specified range.
    for year in tqdm(range(start_date, end_date + 1, 1)):

        # Set the date to the June 1st of the current year.
        current_date = datetime.date(year, 6, 1)
        current_sum = 0
        count = 0

        # Loop through each row in the input audio features dataframe.
        for _, data in song_dataframe.iterrows():
            # Check if the date matches at that instance.
            if data["Date"] == str(current_date):
                # Add the audio feature values.
                current_sum += data[feature]
                count += 1

        # Calculate the average.
        average = current_sum / count
        feature_average = feature_average.append({"Date": current_date, \
        "Feature": feature, "Average": average}, ignore_index=True)
    return feature_average


def average_all(start_date, end_date, features, song_dataframe):
    """
    Return a dataframe containing the average values of each of the given
    features for all the songs in each year.

    Calculate the mean of the values of the input features for all of the songs
    in a given year, looped over each year in the specified time period. Create
    a dataframe for each audio feature and concatenate.

    Args:
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

    Returns:
        average_all: A Pandas dataframe that contains the Date (of featuring on
        Billboard Hot 100), Feature (audio feature by Spotify), and Average
        (the numerical value of a particular audio feature for all the songs in
        a given year) for each of the years in the range specified.
    """
    # Declare an empty dataframe with the appropriate columns.
    average_all_features = pd.DataFrame(columns=["Date", "Feature", "Average"])

    # Loop through each feature in the input list.
    for feature in features:
        # Find the dataframe containing the averages the current feature.
        current_averages = average_by_date(start_date, end_date, feature, \
        song_dataframe)
        # Concatenate dataframes together fall all the features.
        average_all_features = pd.concat\
        ([average_all_features, current_averages], ignore_index=True)

    return average_all_features

# A list containing all the 12 musical keys in a particular standard format so
# that an index of 0 corresponds to C and so forth.
KEY_NAME_LIST = ["C", "C#", "D", "D#", "E", "F", \
"F#", "G", "G#", "A", "A#", "B"]

def key_proportion(start_date, end_date, song_dataframe):
    """
    Return a dataframe containing the relative proportion of songs in each key
    for each year.

    Add up the number of songs in each key for each year, and divide by the
    total number of songs in each year (which may not be 100 if all the track
    IDs couldn't be found for a particular year).

    Args:
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

    Returns:
        key_dataframe_final: A Pandas dataframe that contains the Date, Key,
        Count, and Proportion for each of the years in the range specified.
    """
    # Declare a list of years spanning the specified time period
    year_list = [str(datetime.date(year, 6, 1)) for year in range(start_date, \
    end_date+1)]

    # Slice out the section of the input dataframe that is within the specified
    # time period.
    time_span_dataframe = song_dataframe[song_dataframe.Date.isin(year_list)]

    # Count the number of songs for each key for each year.
    key_dataframe = time_span_dataframe.groupby(by=["Date","key"]).count()

    # Remove the redundant columns, keeping only the first one.
    key_dataframe = key_dataframe.drop\
    (key_dataframe.columns[range(1,len(key_dataframe.columns))], axis=1)

    # Calculate the proportion of each key by summing the number of songs for
    # each year and dividing that by the number of songs in a particular key
    # for the respective years.
    key_proportions = key_dataframe.groupby(level=0).apply\
    (lambda x: x/float(x.sum()))

    # Concatenating the dataframes containing the Count and Proportion and
    # re-introducing the columns containing the Date and the Key.
    key_dataframe_final = pd.concat([key_dataframe, key_proportions], axis=1)\
    .reset_index()

    # Setting the names for the columns of the resulting dataframe.
    key_dataframe_final.columns = ["Date", "Key", "Count", "Proportion"]

    # Replacing the key index integer returned by the Spotify API with a string
    # containing the actual key corresponding to that key index.
    key_dataframe_final["Key"] = key_dataframe_final["Key"].replace(range(12),
    KEY_NAME_LIST)

    return key_dataframe_final
