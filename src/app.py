# Handles the execution of our program

import youtube
import spotify

import secret

# Runs the program without an user interface (using default values in secret.py)
def run():
    songs = youtube.get_songs()
    spotify.create_playlist(songs)

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
    playlist_info = secret.PLAYLIST_INFO

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

    print()
    response = input("Would you like to update playlist information? Leave blank to use the default values. \n")
    if(response != ""):
        response = input("Enter the name of your new Playlist. Leave blank to use the default value ({}). \n".format(playlist_info["name"]))
        if(response != ""):
            playlist_info["name"] = response
        
        response = input("Enter the description of your new Playlist. Leave blank to use the default value ({}). \n".format(playlist_info["description"]))
        if(response != ""):
            playlist_info["description"] = response
        
        response = input("Would you like your playlist to be public (Y/N)? Leave blank to use the default value ({}). \n".format(playlist_info["public"]))
        if(response != ""):
            if(response == "Y"):
                playlist_info["public"] = True
            elif(response == "N"):
                playlist_info["public"] = False
        
        response = input("Would you like your playlist to be collaborative (Y/N)? Leave blank to use the default value ({}). \n".format(playlist_info["collaborative"]))
        if(response != ""):
            if(response == "Y"):
                playlist_info["collaborative"] = True
            elif(response == "N"):
                playlist_info["collaborative"] = False

    spotify.update_secret(client_id, client_secret, user_id, playlist_info)
    spotify.create_playlist(songs)

if __name__ == "__main__":
    # run()
    run_interface()