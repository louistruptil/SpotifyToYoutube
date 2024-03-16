# SpotifyToYoutube

SpotifyToYoutube is a Python script for easily and automatically transferring your Spotify playlist into a YouTube Music playlist.

## Installation

### First, install the YouTube Music API (not an official API)

```bash
pip install ytmusicapi
```
  
### Create a .env file
Never share this file with anybody as it contains personal information.

### Create your Spotify app to access your playlist.
Go to https://developer.spotify.com/dashboard, log in with your Spotify account, then click on "Create app".

Fill in all the required information, but in the Redirect URL field, put "http://localhost:8888/callback" and select Web API.

Click on Settings, and in your .env file, create variables with:

```python
SPOTIFY_CLIENT_ID = "YOUR_CLIENT_ID"
SPOTIFY_CLIENT_SECRET = "YOUR_SECRET_ID"
```

### Create a Google project to create your YouTube playlist.

Go to https://console.cloud.google.com/cloud-resource-manager.

Click on "Create project" and give it a name.

Select your project on the top left of the website.

Click on the three lines, go to API, and activate YouTube Data API v3.

Then go to Credentials and create an OAuth client ID.

Set up your OAuth and download the client OAuth.json, rename it to oauth.json, and place it at the root of the project.

## Usage
```bash
python3 main.py  
```
Enter the ID of your playlist. 
For example, the ID here is 37i9dQZF1E38sB3PmLL0wf:

https://open.spotify.com/playlist/37i9dQZF1E38sB3PmLL0wf

Then enter the name you want for your playlist and a description.

The script can take more or less time to execute, with the principal factors being your internet connection and the length of your Spotify playlist.

## Contributing
Pull requests are welcome.

You can contact me to propose some changes.

## Contributor
Louis Truptil

louis.truptil@epitech.eu
