import requests
import pandas as pd

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
#print(auth_response_data)

# save the access token
access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

# Track ID from the URI
track_id = '6y0igZArWVi6Iz0rj35c1Y'

# actual GET request with proper header
r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)

r = r.json()
#print(r)

def get_playlist_tracks(playlist_id):
    response = requests.get(BASE_URL + 'playlists/' + playlist_id + '/tracks', headers=headers)
    response = response.json().get('items')
    track_ids = []
    for item in response:
        track = item.get('track')
        track_ids.append(track.get('id'))
    return track_ids


# top_50_id = '5FN6Ego7eLX6zHuCMovIR2'
# print(get_playlist_tracks(top_50_id))

