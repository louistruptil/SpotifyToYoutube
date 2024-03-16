import os
import json
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from ytmusicapi import YTMusic

def create_playlist(name, description, tracks):
    oauth_filepath = "oauth.json"
    yt = YTMusic(oauth_filepath)
    playlistId = yt.create_playlist(name, description)
    print("\033[93mYour playlist has been created\033[0m")
    for idx, item in enumerate(tracks):
        track = item['track']
        song = track['artists'][0]['name'] + track['name']
        search_results = yt.search(song)
        if (not search_results) :
            print("\033[91m", idx, "\033[0m")
        else:
            if 'videoId' in search_results[0]:
                try:
                    yt.add_playlist_items(playlistId, [search_results[0]['videoId']])
                    print("\033[92m", idx, search_results[0]['title'])
                except Exception as e:
                    print(f"Failed to add song {idx} to playlist: {e}")
            else:
                print(f"Expected a dictionary with a key 'videoId', but got {search_results[0]}")
    return name


def get_song_spotify(playlist_id):
    scope = "playlist-read-private"
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    redirect_uri = "http://localhost:8888/callback"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))
    all_tracks = []
    results = sp.playlist_tracks(playlist_id, fields=None, limit=100, offset=0, market=None, additional_types=('track', ))
    all_tracks.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        all_tracks.extend(results['items'])
    print("\033[93mThe song from your Spotify playlist have been collected\033[0m")
    return all_tracks

def main():
    load_dotenv()
    playlist_id = input("Enter the ID of the playlist: ")
    all_tracks = get_song_spotify(playlist_id)
    name_playlist = input("Enter the name of the playlist: ")
    description_playlist = input("Enter the description of the playlist: ")
    name = create_playlist(name_playlist, description_playlist, all_tracks)
    print(f"\033[96mYour playlist {name} is successfully uploaded on YouTube\033[0m")

if (__name__ == "__main__"):
    main()