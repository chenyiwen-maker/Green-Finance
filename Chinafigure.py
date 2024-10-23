import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

# Load the score data
df = pd.read_excel('data/Score.xlsx')
ranges = {
    "1990-2000": (1990, 2000),
    "2001-2011": (2001, 2011),
    "2012-2021": (2012, 2021)
}
gdf = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
gdf.plot(aspect=1)
# Create a new dataframe to store the average scores
avg_scores = pd.DataFrame()

for period, (start_year, end_year) in ranges.items():
    avg = df[(df['Time'] >= start_year) & (df['Time'] <= end_year)].groupby('Location')['Score'].mean()
    avg_scores[period] = avg

# Load the China province shapefile with province-level data
china_map = gpd.read_file("data/gadm41_CHN_shp/gadm41_CHN_2.shp")

# 检查是否有 CRS
if china_map.crs is None:
    # 设置 CRS 为 WGS84 (EPSG:4326)
    china_map = china_map.set_crs(epsg=4326)

# Merge the average scores with the shapefile data using the correct column
merged = china_map.merge(avg_scores, left_on="NAME_1", right_on="Location")

# 检查并删除无效几何数据（例如为空或无效的几何形状）
merged = merged[~merged['geometry'].is_empty]  # 删除几何数据为空的行
merged = merged[merged['geometry'].notnull()]  # 删除几何数据为null的行

# Plotting the maps for each period

fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# 1990-2000
merged.plot(column='1990-2000', ax=axs[0], legend=True, cmap='OrRd', legend_kwds={'label': "1990-2000 Average Score"})
axs[0].set_title("1990-2000")

# 2001-2011
merged.plot(column='2001-2011', ax=axs[1], legend=True, cmap='OrRd', legend_kwds={'label': "2001-2011 Average Score"})
axs[1].set_title("2001-2011")

# 2012-2021
merged.plot(column='2012-2021', ax=axs[2], legend=True, cmap='OrRd', legend_kwds={'label': "2012-2021 Average Score"})
axs[2].set_title("2012-2021")

plt.tight_layout()
plt.show()
