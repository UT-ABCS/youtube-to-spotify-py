# Handles the interaction with the Spotify Web API

import requests
import base64
import urllib.parse
import webbrowser

from secret import CLIENT_ID, CLIENT_SECRET, USER_ID, PLAYLIST_INFO

# (For the user interface option) Update secret values
def update_secret(client_id, client_secret, user_id, playlist_info):
    global CLIENT_ID, CLIENT_SECRET, USER_ID, PLAYLIST_INFO
    CLIENT_ID = client_id
    CLIENT_SECRET = client_secret
    USER_ID = user_id
    PLAYLIST_INFO = playlist_info

# Create the playlist with the given songs
def create_playlist(songs):
    access_token = get_user_permission()
    track_uris = get_track_uris(songs, access_token)
    create_and_populate_playlist(track_uris, access_token)

# Get permission from the user to make changes to their account by obtaining
# an authorization token. Follow the Authorization Code Flow
# See more: https://developer.spotify.com/documentation/web-api/tutorials/code-flow
# Adapted from: https://stackoverflow.com/questions/65435932/spotify-api-authorization-code-flow-with-python
# and: https://python.plainenglish.io/bored-of-libraries-heres-how-to-connect-to-the-spotify-api-using-pure-python-bd31e9e3d88a  
def get_user_permission():
    # Get user authorization to obtain the authorization code
    query = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri":"https://open.spotify.com/collection/playlists",
        "scope":"playlist-modify-private"
    }
    webbrowser.open("https://accounts.spotify.com/authorize?" + urllib.parse.urlencode(query))
    auth_code = input("After authorizing this application, enter the authorization code: ")

    # Make a request to the /token endpoint to get an access token
    auth_header = base64.urlsafe_b64encode((CLIENT_ID + ':' + CLIENT_SECRET).encode())
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic %s' % auth_header.decode('ascii')
    }
    payload = {
        'grant_type': 'authorization_code',
        'code': auth_code,
        'redirect_uri': 'https://open.spotify.com/collection/playlists',
    }
    TOKEN_URL = 'https://accounts.spotify.com/api/token'
    response = requests.post(url=TOKEN_URL, data=payload, headers=headers)

    return response.json()["access_token"]

# Get the Spotify URI of each track
def get_track_uris(songs, token):
    track_uris = []

    for track in songs:
        # Send a GET request to retreive the song info
        searchURL = "https://api.spotify.com/v1/search?q=remaster%2520track%3A{}%2520artist%3A{}&type=track".format(track["song"], track["artist"])
        head = {'Authorization': 'Bearer {}'.format(token)}
        response = requests.get(searchURL, headers=head)

        # Obtain the URI of the track from the response and add it to the list
        uri = response.json()["tracks"]["items"][0]["uri"]
        track_uris.append(uri)
    
    return track_uris

# Creates a new playlist with the tracks from the given track_uris
def create_and_populate_playlist(track_uris, token):
    head = {'Authorization': 'Bearer {}'.format(token), 'Content-Type': 'application/json'}

    # Send a POST request to create the playlist
    url = "https://api.spotify.com/v1/users/{}/playlists".format(USER_ID)
    json_data = PLAYLIST_INFO
    response = requests.post(url, json=json_data, headers=head)

    # Send another POST request to add the songs to the playlist
    playlist_id = response.json()["id"]
    json_data = {
        "uris": track_uris,
        "position": 0
    }
    url = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist_id)
    response = requests.post(url, json=json_data, headers=head)