import pandas as pd
from get_songids import get_playlist_tracks
from track_list_feature import id_to_duration
track_id_list = get_playlist_tracks('5FN6Ego7eLX6zHuCMovIR2')
track_stuff = id_to_duration(track_id_list)

panda_data = pd.DataFrame.from_dict(track_stuff)
panda_data_clean = pd.json_normalize(panda_data['audio_features'])
