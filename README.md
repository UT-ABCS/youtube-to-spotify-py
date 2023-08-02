# YouTube to Spotify Automation
<img width="687" alt="Screen Shot 2023-03-22 at 11 59 37 PM" src="https://user-images.githubusercontent.com/91110018/227107829-61dbe774-c069-4cbd-97fc-dd3eff3b8d84.png">

This project was taught as a Technical Project Workshop for the Association of Computer Scientists at the University of Texas at Austin. This project is complete, though small changes may be added in the future. You can find more information [here](https://github.com/UT-ABCS/tech-workshops).  <br />

This workshop will cover the use of Google Cloud Services and a Web API within a Python application. The goal of this project is to utilize the YouTube Data API and the Spotify Web API to take songs from within a public YouTube playlist and automate the creation of a Spotify playlist. You can find the slides associated with this workshop at [this link](https://docs.google.com/presentation/d/1Sj1JqZSncf4TMeBEiAPnfc_c-5rV9AhUNHfglV_-A8k/edit?usp=sharing). This project was inspired by Bukola's [Automate Spotify with Python](https://www.youtube.com/watch?v=7J_qcttfnJA) video.  <br />
  
__Technology Used__
+ Python
+ Google Cloud Platform
+ YouTube Data API
+ Spotify Web API

## Installation
1. Ensure that you have the latest version of Python and `pipenv` installed on your computer. 
2. Clone this repository, `cd` into this respository and call `pipenv install`.

## How to run
Before running this code, make sure that you have a Google Cloud project and a Spotify Web Application made.
1. `cd` into this respository
2. Go to the Google Cloud Console and navigate to your Google Cloud project.
3. Download the OAuth 2.0 Client ID associated with your Google Cloud project.
4. Move the OAuth Client ID into your repository on the top level, and title the file `client_secret.json`.
5. In the `src/` directory, create a new file called `secret.py`
6. In `secret.py`, add the following code:
```
# For the YouTube Data API
PLAYLIST_ID = "ID OF YOUTUBE PLAYLIST"

# For the Spotify Web API
CLIENT_ID = "SPOTIFY WEB APP CLIENT ID"
CLIENT_SECRET = "SPOTIFY WEB APP CLIENT SECRET"
USER_ID = "YOUR SPOTIFY USERNAME"

PLAYLIST_INFO = {
    "name": "My YouTube Playlist",
    "description": "Playlist created by the tutorial on developer.spotify.com",
    "public": False,
    "collaborative": True
} 
```
7. Replace the information in `secret.py` with information from your Google Cloud project and Spotify Web App.
  + PLAYLIST_ID is the ID of the YouTube playlist you want the program to use.
  + CLIENT_ID and CLIENT_SECRET is the client ID and client secret, respectively, of your Spotify Web Application. You can find both in the settings of your Spotify Web Application in the Spotify Developer Console.
  + USER_ID is the user id of the Spotify account you want the application to use. You can find this information by logging in to Spotify with the account, navigating to [this link](https://www.spotify.com/us/account/overview/?utm_source=spotify&utm_medium=menu&utm_campaign=your_account) and using the Username specified in the Profile section of Account Overview.
8. Call `pipenv run python3 src/app.py` to launch the UI.

## Find a bug?
If you found an issue or would like to submit an improvement to this project, please submit an issue using the issues tab above. If you would like to submit a PR with a fix, reference the issue you created!

## Potential Future Improvements
For those who want to continue this project you can add additional functionality to:
+ Improve the accuracy of searching for each song
+ Add songs to an existing Spotify playlist instead of creating a new one on each run
+ Saving token information between each subsequent run
+ Using a Python library for the Spotify Web API instead of sending HTTP requests
