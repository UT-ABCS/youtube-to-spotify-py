# Handles the interaction with the YouTube Data API

import os
from urllib.parse import quote

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from secret import PLAYLIST_ID

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

# (For the user interface option) Update secret values
def update_secret(playlist_id):
    global PLAYLIST_ID
    PLAYLIST_ID = playlist_id

# Look at: https://developers.google.com/youtube/v3/code_samples/code_snippets
# resource: playlistItems, method: list
def get_songs():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        maxResults=25,
        playlistId=PLAYLIST_ID
    )
    response = request.execute()

    # Get the song info of each video in the playlist from its video title
    songs = []
    for video in response["items"]:
        song_info = get_song_info(video["snippet"]["title"])
        songs.append(song_info)

    return songs

# Given a video title, return the corresponding song information
# e.g. For the video title "Miley Cyrus - Party In The USA", return:
# {
#     artist: "Miley%20Cyrus"
#     song: "Party%20In%20The%20USA"
# }
def get_song_info(video_title):
    info = video_title.split("-")
    artist_name = quote(info[0].strip(), safe = '')
    song_name = quote(info[1].strip(), safe = '')

    return {
        "artist": artist_name,
        "song": song_name
    }