import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import time
from datetime import datetime
import requests, os


def albumids_from_file(fp):
    ''' Function that asks for a filepath to the csvfile that contains the spotify album ID's for albums. Returns the isolated ids from the csvfile as a list.'''

    ids = []
    # Open csv file, get ids
    with open(fp) as csvfile:

        reader = csv.reader(csvfile)

        # Proces header
        header = next(reader)

        # read csv file, get album_ids
        for row in reader:
            ids.append(row[2])

    return ids

def get_spotipy_albums(album_id):
    '''Function that makes connection to the spotify API, then gets album information for a given album_id. Returns the API results.'''

    CLIENT_ID = "97a3b01c82c8422b8996948504c5a551"
    CLIENT_SECRET = "ea5fb92602dc483d894f53c4b6f66859"

    # Setup spotify client
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

    # Get album from Spotify API using spotify album_id and return results
    return sp.album(album_id)


def download_image(url, save_path):    
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Open a file in binary write mode and write the content of the response to it
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print("Image downloaded successfully!")
        else:
            print("Failed to download image. Status code:", response.status_code)
    except Exception as e:
        print("Error:", e)


def process_albums(results):
    # get title
    albumtitle = str(results["name"])

    # get artist
    artist = results["artists"][0]["name"]
    
    # get and process release date
    release_date = results["release_date"]
    ord = datetime.strptime(release_date, "%Y-%m-%d")
    release_date = datetime.strftime(ord, "%d-%m-%Y")

    # get and process cover art
    images = results["images"]
    for image_dict in images:
        h = image_dict["height"]
        w = image_dict["width"]
        
        path = f"./media/cover_art/{albumtitle}/".replace(" ", "_").lower()
        print(f"Path: {path}")
        if not os.path.exists(path):
            print(f"Creating path..")
            os.makedirs(path)
        else:
            print(f"{path} exists.")

        #TODO make directory for album
        download_image(image_dict["url"], save_path=f'./media/cover_art/{albumtitle.replace(" ", "_").lower()}/{h}x{w}.jpg')
        time.sleep(2)

    return 


def main():
    # Set filepath of csv file with spotify album_ids
    filepath = "C:\\Users\\nicol\\OneDriveJoost\\OneDrive\\Documenten\\Coding\\reviewwebsite\\reviewSite\\data\\albums_spotify2023.csv"
    
    album_ids = albumids_from_file(filepath)
    
    for aid in album_ids:
        results = get_spotipy_albums(aid)
        print(results)
        process_albums(results)

    return

if  __name__ == '__main__':
    main()