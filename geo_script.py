import geopandas

# Import sample data
gdf = geopandas.read_file(geopandas.datasets.get_path("naturalearth_lowres"))

# Print column names
print(gdf.columns)
