"""
Converts a list of Spotify track IDs to a pandas dataframe containing all of
its audio features.

TODO: Add a function that converts not only one list but the entire dataframe of
all the songs by looping over each chart and inputting it into id_to_duration
(change that function name to more sensible one) so that the queries happen in
batches of 100 (which conveniently happens to be the maximum length of one query).
"""
import pandas as pd
import requests
from tqdm.autonotebook import tqdm
#Get the client and secret IDs from files stored and remove the newline
with open('client_id.txt') as f:
    CLIENT_ID = str(f.read())
CLIENT_ID = CLIENT_ID[0:-1]

with open('secret_id.txt') as f:
    CLIENT_SECRET = str(f.read())
CLIENT_SECRET = CLIENT_SECRET[0:-1]

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'
#
# id_dataframe = pd.DataFrame([['Blah', 'Blah', '6y0igZArWVi6Iz0rj35c1Y'], \
# ['Blahh', 'Blah', '6y0igZArWVi6Iz0rj35c1Y'], ['Blahhhh', 'Blah', '6y0igZArWVi6Iz0rj35c1Y'], \
# ['Blahhhh', 'Blah', '6y0igZArWVi6Iz0rj35c1Y']], columns=['Song', 'Artist', 'Track ID'])

def find_audio_features(id_dataframe):


    track_id_master = id_dataframe["Track ID"].tolist()
    audio_dataframe = id_to_audio_feature([track_id_master[0]])
    track_id_master_split = [track_id_master[i:i+100] for i in range(1, len(track_id_master), 100)]
    for list_section in tqdm(track_id_master_split):
        dataframe_section = id_to_audio_feature(list_section)
        audio_dataframe = audio_dataframe.append(dataframe_section, ignore_index=True)
    THE_dataframe = pd.concat([id_dataframe, audio_dataframe], axis=1)
    return(THE_dataframe)

def id_to_audio_feature(track_id_list):
    track_id_string = ",".join(track_id_list)

    # actual GET request with proper header
    r = requests.get(BASE_URL + 'audio-features/?ids=' + \
    track_id_string, headers=headers)
    r = r.json()

    panda_data = pd.DataFrame.from_dict(r)
    panda_data_clean = pd.json_normalize(panda_data['audio_features'])
    return(panda_data_clean)

#print(id_to_audio_feature(['6y0igZArWVi6Iz0rj35c1Y', '6y0igZArWVi6Iz0rj35c1Y', '6y0igZArWVi6Iz0rj35c1Y', '6y0igZArWVi6Iz0rj35c1Y']))
