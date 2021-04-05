import final_billboard
import final_id_finder
import final_audio_query

billboard_data = final_billboard.hot_100_data(2019,2020)
id_data = final_id_finder.query_all_tracks(billboard_data)
audio_data = final_audio_query.find_audio_features(id_data)

print(audio_data)
