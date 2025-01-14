import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from pathlib import Path

def generate_heatmap(events):
    # Ensure the static path exists
    static_dir = Path('events/static/events/')
    static_dir.mkdir(parents=True, exist_ok=True)  # Create directory if it doesn't exist

    # Path to save the heatmap
    output_path = static_dir / 'heatmap.png'

    # Load shapefile and create the map
    shapefile_path = static_dir / 'shapefiles/ne_110m_admin_0_countries.shp'
    usa = gpd.read_file(shapefile_path)
    usa = usa[usa['ADMIN'] == 'United States of America']  # Filter for USA

    # Prepare event data
    df = pd.DataFrame([{'latitude': e.latitude, 'longitude': e.longitude} for e in events])
    event_points = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude))

    # Generate the plot
    base = usa.plot(color='white', edgecolor='black')
    event_points.plot(ax=base, color='red', alpha=0.5)

    # Save the heatmap
    plt.savefig(output_path)
    plt.close()

    return f'/static/events/heatmap.png'
