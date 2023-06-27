# Handles the interaction with the YouTube Data API

from urllib.parse import quote

# from secret import ?

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

# Get the song information from each video in the given Youtube playlist
def get_songs():
    videos = get_videos_from_playlist()

    # Get the song info of each video in the playlist from its video title
    songs = []
    for video in videos["items"]:
        song_info = extract_song_info(video["snippet"]["title"])
        songs.append(song_info)

    return songs

# Returns the list of videos from the playlist id specified in the secret.py file
def get_videos_from_playlist():
    pass

# Given a video title, return the corresponding song information
# e.g. For the video title "Miley Cyrus - Party In The USA", return:
# {
#     artist: "Miley%20Cyrus"
#     song: "Party%20In%20The%20USA"
# }
def extract_song_info(video_title):
    info = video_title.split("-")
    artist_name = quote(info[0].strip(), safe = '')
    song_name = quote(info[1].strip(), safe = '')

    return {
        "artist": artist_name,
        "song": song_name
    }