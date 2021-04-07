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


def query_track(title, artist):
    # Search Spotify for
    response = requests.get(BASE_URL + 'search', params={"q": f"{title} {artist}", "type": "track", "limit": 1}, headers=headers)
    response = response.json()
    # Transform the response into a single string as the Spotify id
    # First we must make sure spotify has found the track, so it doesn't result in errors later
    if response["tracks"]["items"] == []:
        return "Error: Not in Spotify"
    track_id = response["tracks"]["items"][0]["id"]
    return track_id

def query_all_tracks(track_dataframe):
    id_dataframe = pd.DataFrame(columns=["Date", "Song", "Artist", "Track ID"])
    for _, data in tqdm(track_dataframe.iterrows()):
        current_id = query_track(data["Song"], data["Artist"])
        if current_id != "Error: Not in Spotify":
            id_dataframe = id_dataframe.append({"Date": data["Date"], "Song": data["Song"], "Artist": data["Artist"], "Track ID" : current_id}, ignore_index=True)
    return id_dataframe
