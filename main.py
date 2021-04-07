import pandas as pd
import billboard_scraper
import spotify_id_query
import get_audio_features

billboard_data = billboard_scraper.hot_100_data(1991,2000)
id_data = spotify_id_query.query_all_tracks(billboard_data)
audio_data = get_audio_features.find_audio_features(id_data)

audio_data.to_csv(path_or_buf='1990s.csv')
