from get_songids import get_playlist_tracks
from track_list_feature import id_to_duration
track_id_list = get_playlist_tracks('5FN6Ego7eLX6zHuCMovIR2')
print(id_to_duration(track_id_list))
