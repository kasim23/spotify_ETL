import requests
from src.authenticate import get_access_token
from src.logging import setup_logger

# Set up the logger
logger = setup_logger('spotify_etl', 'spotify_etl.log')

def get_artist_data(artist_id):
    access_token = get_access_token()
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    artist_url = f'https://api.spotify.com/v1/artists/{artist_id}'
    artist_response = requests.get(artist_url, headers=headers)
    return artist_response.json()

def get_artist_top_tracks(artist_id):
    access_token = get_access_token()
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    top_tracks_url = f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks'
    params = {'market': 'US'}
    top_tracks_response = requests.get(top_tracks_url, headers=headers, params=params)
    
    # Log the full response
    logger.info(f"Response from Spotify API for artist {artist_id}: {top_tracks_response.json()}")
    
    # Check for errors in the response
    if top_tracks_response.status_code != 200:
        logger.error(f'Error fetching top tracks for artist {artist_id}: {top_tracks_response.json()}')
        return {}
    
    response_json = top_tracks_response.json()
    
    if 'tracks' not in response_json:
        logger.error(f"'tracks' key not found in the response for artist {artist_id}: {response_json}")
        return {}
    
    return response_json
