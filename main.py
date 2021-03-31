import pandas as pd
from get_songids import get_playlist_tracks
from track_list_feature import id_to_duration
track_id_list = get_playlist_tracks('5FN6Ego7eLX6zHuCMovIR2')
track_stuff = id_to_duration(track_id_list)

panda_data = pd.DataFrame.from_dict(track_stuff)
panda_data_clean = pd.json_normalize(panda_data['audio_features'])

key_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for song in panda_data_clean['key']:
    key_list[song] += 1

key_name_list = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
dataframe_converted = pd.DataFrame({"Key Name": key_name_list, "Key Count": key_list})
import plotly.express as px
fig = px.pie(dataframe_converted, values="Key Count", names="Key Name", title="Please Work")
fig.show()
