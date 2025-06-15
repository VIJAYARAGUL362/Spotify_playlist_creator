import spotipy,os,time
from spotipy.oauth2 import SpotifyOAuth
class  Spotify:
    def __init__(self):
        self.client_id = os.getenv("CLIENT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")
        self.redirect_id = os.getenv("REDIRECT_URL")
        print(self.redirect_id)
        self.scope = ""
        self.request=""
        self.token = ""
        self.auth = ""
        self.user_id = ""
        self.sp = ""
        self.BIRTHDAY=os.getenv("BIRTHDAY")
        self.file_name = f"best music of {self.BIRTHDAY}.txt"
        self.token_getter()

    def token_getter(self)->None:
        """This function will use our client id and client secret to get the ascess token it is using the
        authentication flow"""
        self.auth = SpotifyOAuth(client_id=self.client_id,
                                 client_secret=self.client_secret,
                                 redirect_uri=self.redirect_id,
                                 state="1",open_browser=True,
                                 scope=["playlist-modify-public","user-library-read"])
        # self.token = self.auth.get_access_token()['access_token']
        # os.environ["TOKEN"] = self.token
        self.sp = spotipy.Spotify(auth_manager=self.auth)
        self.user_id = self.sp.current_user()['id']
        print(self.sp.current_user())
        print(self.user_id)
        # print(self.token)


    def liked_songs(self)->None:
        """This function used our client ID and Client Secret to assess the spotify and
    prints the songs that we have in our liked songs"""

        self.scope = "user-library-read"
        results = self.sp.current_user_saved_tracks()
        for idx, item in enumerate(results['items']):
            track = item['track']
            print(idx, track['artists'][0]['name'], " – ", track['name'])

    def searching_songs(self)->None:
        """This function is used to search for a specific song that is stored in a text file"""
        uri_artist = []
        # token = os.getenv("TOKEN")
        with open(self.file_name,mode="r") as file:
            musics = file.readlines()
            for music in musics:
                time.sleep(2)
                try:
                    print(music)
                    self.request = f"track:{music.strip()}"
                    search_response = self.sp.search(q=self.request,limit=1,type="track")
                    print(search_response)
                    uri_artist.append(search_response["tracks"]["items"][0]["uri"])
                except IndexError:
                    pass

    def creating_playlist(self):
        message = f"""A sonic journey to {os.getenv("BIRTHDAY")}.
This playlist captures the essence of that specific day, 
featuring all the tracks that topped the Billboard Hot 100 chart. 
Curated automatically from historical data, 
it's a unique blend of forgotten gems and timeless classics that were defining the airwaves when you arrived."""
        print(self.sp)
        playlist = self.sp.user_playlist_create(user=self.user_id,name=f"The birthday special on {self.BIRTHDAY}",public=True,description=message)
        print(playlist)