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
