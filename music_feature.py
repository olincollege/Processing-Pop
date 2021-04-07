import pandas as pd
import datetime
from tqdm.autonotebook import tqdm
from data_compiler import master_dataframe

def average_by_date(start_date, end_date, feature):
    average_by_date = pd.DataFrame(columns=["Date", "Feature", "Average"])

    for year in tqdm(range(start_date, end_date + 1, 1)):
        current_date = datetime.date(year, 6, 1)
        current_sum = 0
        count = 0
        for _, data in master_dataframe.iterrows():
            if data["Date"] == str(current_date):
                current_sum += data[feature]
                count += 1
        average = current_sum / count
        average_by_date = average_by_date.append({"Date": current_date, "Feature": feature, "Average": average}, ignore_index=True)
    return average_by_date


def average_all(start_date, end_date, features):
    average_all_features = pd.DataFrame(columns=["Date", "Feature", "Average"])
    for feature in features:
        current_averages = average_by_date(start_date, end_date, feature)
        average_all_features = pd.concat([average_all_features, current_averages])
    return average_all_features

def key_proportion(start_date, end_date):
    key_name_list = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    key_dataframe = pd.DataFrame(columns=["Date", "Key", "Count", "Proportion"])
    for year in tqdm(range(1961,2021,1)):
        current_date = str(datetime.date(year, 6, 1))
        for current_key in key_name_list:
            count = 0
            year_count = 0
            for _, data in master_dataframe.iterrows():
                if current_date == data["Date"]:
                    year_count += 1
                    if data["key"] == key_name_list.index(current_key):
                        count += 1

            key_dataframe = key_dataframe.append({"Date": current_date, "Key": current_key, "Count":count, "Proportion":count/year_count}, ignore_index=True)

    # print(key_dataframe)
    # import plotly.express as px
    # fig = px.bar(key_dataframe, x="Date", y="Proportion", color="Key", title="Keys Over Time")
    # fig.show()
