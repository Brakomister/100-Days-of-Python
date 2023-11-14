import requests
import os
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# ------------ Scraping Billboard 100 Website -------------- #
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(URL)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")
print(soup)
# songs = soup.select(selector='li ul li h3')
# songs_list = [song.text.strip() for song in songs]
#
# # ------------- Authentication with Spotify ------------ #
# CLIENT_ID = "bf6e1c33e629466980da7bf28f961e90"
# CLIENT_SECRET = "5185ab9fbc074bd3ac3c15c109527c8b"
# REDIRECT_URI = 'https://example.com'
#
# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope="playlist-modify-private",
#         redirect_uri=REDIRECT_URI,
#         client_id=CLIENT_ID,
#         client_secret=CLIENT_SECRET,
#         show_dialog=True,
#         cache_path="token.txt"
#     )
# )
# user_id = sp.current_user()["id"]
#
# # ------------- Search Spotify for the Songs ------------ #
# songs_uri = []
# for song_q in songs_list:
#     song = sp.search(f"track:{song_q} year:{date[:4]}", type='track', limit=1)
#
#     try:
#         song_uri = song['tracks']['items'][0]['uri']
#         songs_uri.append(song_uri)
#
#     except IndexError:
#         print("This song does not exist")
#
# playlist = sp.user_playlist_create(user_id, f"{date} Billboard 100", public=False)
# playlist_uri = playlist['uri']
#
# sp.playlist_add_items(playlist_uri, songs_uri)
#
# # songs_ = [sp.search(f"track:{song_q} year:{date[:4]}", type='track', limit=1)['tracks']['items'] for song_q in \
# #            songs_list]
# # print(songs_[0])
