# YouTube to Spotify Automation
<img width="687" alt="Screen Shot 2023-03-22 at 11 59 37 PM" src="https://user-images.githubusercontent.com/91110018/227107829-61dbe774-c069-4cbd-97fc-dd3eff3b8d84.png">

The goal of this project is to utilize the YouTube Data API and the Spotify Web API to take songs from within a public YouTube playlist and automate the creation of a Spotify playlist. This project was inspired by Bukola's [Automate Spotify with Python](https://www.youtube.com/watch?v=7J_qcttfnJA) video.  <br />
This project was taught as a Technical Project Workshop for the Association of Computer Scientists at the University of Texas at Austin. This project is complete, though small changes may be added in the future. You can find more information [here](https://shaded-nigella-ee4.notion.site/Technical-Workshops-f5b3950311e34a1c85e84a4b89cb7702).  <br />

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
Before running this code, make sure that you have a Google Cloud project and a Spotify Web Application made. If you don't, you can go to the respective links for Google Cloud Developers and Spotify Developers.
1. `cd` into this respository
2. Go to the Google Cloud Console and navigate to your Google Cloud project.
3. Download the OAuth 2.0 Client ID associated with your Google Cloud project.
4. Move the OAuth Client ID into your repository on the top level, and title the file `client_secret.json`.
5. In the `src/` directory, create a new file called `secret.py`
6. In `secret.py`, add the following code:
```
# For the YouTube Data API
PLAYLIST_ID = "PLqqrBkAAeqhNGlRf3x2Cp1qDO1Q1MngZK"

# For the Spotify Web API
CLIENT_ID = "89fa6f2bf40948338b7914fa9c1661dc"
CLIENT_SECRET = "56c671dd840d460b9e5451a0e76e1e48"
USER_ID = "31bkyigul7nv7g3jb5uppnruxk3i"

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

## Known Bugs
+ [insert]
+ [insert]
## Potential Future Improvements
For those who want to continue this project you can add additional functionality to:
+ Improve the accuracy of searching for each song
+ Add songs to an existing Spotify playlist instead of creating a new one on each run
+ Saving token information between each subsequent run
+ Using a Python library for the Spotify Web API instead of sending HTTP requests
