import pandas as pd
import datetime
from tqdm.autonotebook import tqdm

def average_by_date(start_date, end_date, feature, song_dataframe):
    average_by_date = pd.DataFrame(columns=["Date", "Feature", "Average"])

    for year in tqdm(range(start_date, end_date + 1, 1)):
        current_date = datetime.date(year, 6, 1)
        current_sum = 0
        count = 0
        for _, data in song_dataframe.iterrows():
            if data["Date"] == str(current_date):
                current_sum += data[feature]
                count += 1
        average = current_sum / count
        average_by_date = average_by_date.append({"Date": current_date, "Feature": feature, "Average": average}, ignore_index=True)
    return average_by_date


def average_all(start_date, end_date, features, song_dataframe):
    average_all_features = pd.DataFrame(columns=["Date", "Feature", "Average"])
    for feature in features:
        current_averages = average_by_date(start_date, end_date, feature, song_dataframe)
        average_all_features = pd.concat([average_all_features, current_averages], ignore_index=True)
    return average_all_features

KEY_NAME_LIST = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
def key_proportion(start_date, end_date, song_dataframe):
    year_list = [str(datetime.date(year, 6, 1)) for year in range(start_date, end_date+1)]
    time_span_dataframe = song_dataframe[song_dataframe.Date.isin(year_list)]
    key_dataframe = time_span_dataframe.groupby(by=["Date","key"]).count()
    key_dataframe = key_dataframe.drop(key_dataframe.columns[range(1,len(key_dataframe.columns))], axis=1)
    key_proportion = key_dataframe.groupby(level=0).apply(lambda x: x/float(x.sum()))
    key_dataframe_final = pd.concat([key_dataframe, key_proportion], axis=1).reset_index()
    key_dataframe_final.columns = ["Date", "Key", "Count", "Proportion"]
    key_dataframe_final["Key"] = key_dataframe_final["Key"].replace(range(12), KEY_NAME_LIST)
    return(key_dataframe_final)
