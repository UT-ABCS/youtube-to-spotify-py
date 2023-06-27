# Handles the execution of our program

import youtube
import spotify

import secret

# Runs the program without an user interface (using default values in secret.py)
def run():
    songs = youtube.get_songs()
    spotify.create_playlist(songs)

    print()
    print("Playlist created! Check your spotify account.")
    print()

# Runs the program with an user interface
def run_interface():
    # Ask for YouTube information
    playlist_id = secret.PLAYLIST_ID
    response = input("Enter the ID of the YouTube playlist you want to read from. Leave blank to use the default value ({}). \n".format(secret.PLAYLIST_ID))    
    if(response != ""):
        playlist_id = response

    print()
    youtube.update_secret(playlist_id)
    songs = youtube.get_songs()

    # Ask for Spotify information
    client_id = secret.CLIENT_ID
    client_secret = secret.CLIENT_SECRET
    user_id = secret.USER_ID
    redirect_uri = secret.REDIRECT_URI

    print()
    response = input("Enter the Client ID of the Spotify Web App. Leave blank to use the default value ({}). \n".format(client_id))
    if(response != ""):
        client_id = response

    response = input("Enter the Client Secret of the Spotify Web App. Leave blank to use the default value ({}). \n".format(client_secret))
    if(response != ""):
        client_secret = response

    response = input("Enter your Spotify User ID. Leave blank to use the default value ({}). \n".format(user_id))
    if(response != ""):
        user_id = response

    response = input("Enter a redirect uri of the Spotify Web App. Leave blank to use the default value ({}). \n".format(redirect_uri))
    if(response != ""):
        redirect_uri = response

    spotify.update_secret(client_id, client_secret, user_id, redirect_uri)
    spotify.create_playlist(songs)

    print()
    print("Playlist created! Check your spotify account.")
    print()

if __name__ == "__main__":
    # run()
    run_interface()