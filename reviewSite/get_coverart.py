import requests
import xml
import xml.etree.ElementTree as ET

def lastfm_get(payload):

    """
    Get function for the lastfm API to get the albums. As parameter, send {'method': 'album.getInfo'}
    """

    headers = {'user-agent': "reviewappJoost"}
    url = 'https://ws.audioscrobbler.com/2.0/'

    payload['api_key'] = '5c80444361eb979f32f62f17b26f2518'
    payload['format'] = 'xml'

    response = requests.get(url, headers=headers, params=payload)
    return response


def read_xlmobject(response):

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the XML content
        root = ET.fromstring(response.content)

        # Print the XML object
        xml_string = ET.tostring(root, encoding="utf-8")
        print(xml_string.decode("utf-8"))
    else:
        print("Failed to fetch data from the API:", response.status_code)


    return


import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "97a3b01c82c8422b8996948504c5a551"
CLIENT_SECRET = "ea5fb92602dc483d894f53c4b6f66859"
AUTH_URL = "https://accounts.spotify.com/api/token"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(CLIENT_ID="YOUR_APP_CLIENT_ID",
                                               CLIENT_SECRET="YOUR_APP_CLIENT_SECRET",
                                               redirect_uri="YOUR_APP_REDIRECT_URI",
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])




def spotify_get(payload):


    AUTH_URL = "https://accounts.spotify.com/api/token"

def main():    
    m = {
        "method": "album.getInfo",
        "mbid": "643aea71-63db-4a4e-86f3-93366fb0f292"
        # "artist": "Paramore",
        # "album": "This Is Why"
    }

    response = lastfm_get(m)

    read_xlmobject(response)

    return


if __name__ == "__main__":
    main()