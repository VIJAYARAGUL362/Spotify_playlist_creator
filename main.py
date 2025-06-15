import requests,os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from music import Spotify

load_dotenv()

URL = "https://www.billboard.com/charts/hot-100"
# dob = input("Enter the day you want to time travel to in the format of YYYY-MM-DD: ")
dob = os.getenv("BIRTHDAY")
header = {
        "User-Agent":os.getenv("USER_AGENT"),
}
response = requests.get(f"{URL}/{dob}",headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text,"html.parser")
music_htmllist = soup.select(selector="li .c-title")

music_playlist = [music_name for music_name in music_htmllist]

with open(f"best music of {dob}.txt",mode="w") as file:
        for music in music_playlist:
                file.write(f"{"".join(music.get_text().split())}\n")


musics = Spotify()
musics.liked_songs()
musics.searching_songs()
musics.creating_playlist()