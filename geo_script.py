import geopandas

# Import sample data
gdf = geopandas.read_file("ne_110m_admin_0_countries.gpkg")

# Print column names
print(gdf.columns)
