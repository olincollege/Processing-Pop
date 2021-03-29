"""
Converts a list of Spotify track IDs to a json file containing all its audio features.
"""
def id_to_duration(track_id_list):
    track_id_string = ",".join(track_id_list)
    print(track_id_string)
    #track_id_string = track_id_dataframe.to_string()
    #print(track_id_string)
    import requests

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

    # actual GET request with proper header
    r = requests.get(BASE_URL + 'audio-features/?ids=' + track_id_string, headers=headers)
    r = r.json()
    return(r)
