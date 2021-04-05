import pandas as pd
import datetime
from data_compiler import master_dataframe
from tqdm.autonotebook import tqdm

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

# key_dataframe = pd.DataFrame(columns=["Date", "Key Name", "Key Count", "Key Proportion"])
#
# for _, song in master_dataframe.iterrows():
#     key_dataframe = key_dataframe.append({"Date":song["Date"], \
#     "Key Name":key_name_list[song["key"]], "Key Count": key_list[song["key"]], \
#     "Key Proportion":key_list[song["key"]]/sum(key_list)}, ignore_index=True)
# key_list_proportion = [count/sum(key_list) for count in key_list]
# dataframe_converted = pd.DataFrame({"Key Name": key_name_list, "Key Count": key_list, "Key Proportion": key_list_proportion})
print(key_dataframe)
import plotly.express as px
fig = px.bar(key_dataframe, x="Date", y="Proportion", color="Key", title="Keys Over Time")
fig.show()
