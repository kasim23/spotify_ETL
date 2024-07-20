import pandas as pd

def transform_artist_data(artist_data):
    artist_info = {
        'name': artist_data['name'],
        'followers': artist_data['followers']['total'],
        'popularity': artist_data['popularity'],
        'genres': artist_data['genres']
    }
    artist_df = pd.DataFrame([artist_info])
    return artist_df

def transform_top_tracks_data(top_tracks_data):
    top_tracks = []
    if 'tracks' not in top_tracks_data:
        raise KeyError(f"'tracks' key not found in the response: {top_tracks_data}")
        
    for track in top_tracks_data['tracks']:
        top_tracks.append({
            'name': track['name'],
            'popularity': track['popularity'],
            'album': track['album']['name'],
            'release_date': track['album']['release_date']
        })
    tracks_df = pd.DataFrame(top_tracks)
    return tracks_df

