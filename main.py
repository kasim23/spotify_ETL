# main.py
from src.extract import get_artist_data, get_artist_top_tracks
from src.transform import transform_artist_data, transform_top_tracks_data
from src.load import upload_to_s3
from src.logging import setup_logger

# Set up the logger
logger = setup_logger('spotify_etl', 'spotify_etl.log')

def main():
    artist_id = '46pWGuE3dSwY3bMMXGBvVS'  # Replace with the actual artist ID you want to fetch data for

    logger.info('Starting ETL process')
    
    try:
        artist_data = get_artist_data(artist_id)  # Pass the artist ID to the function
        top_tracks_data = get_artist_top_tracks(artist_id)  # Pass the artist ID to the function
        
        if not top_tracks_data:
            logger.error(f"No top tracks data found for artist {artist_id}. Skipping transformation and loading.")
            return
        
        artist_df = transform_artist_data(artist_data)
        tracks_df = transform_top_tracks_data(top_tracks_data)
        
        upload_to_s3(artist_df, f'spotify_data/{artist_id}_artist_info.csv')
        upload_to_s3(tracks_df, f'spotify_data/{artist_id}_top_tracks.csv')
        
        logger.info('ETL process completed successfully')
    except Exception as e:
        logger.error(f'Error occurred: {e}', exc_info=True)

if __name__ == '__main__':
    main()
