
import numpy as np
import matplotlib.pyplot as plt
import rasterio
from rasterio.plot import show

data_dir = "/Users/patryksusz/Documents/exam20240204/team4/task1/"
temp_files = ["t3_lst2023_Jul_Aug.tif", "t3_lst2024May.tif"]
ndvi_files = ["t3_ndvi2023_Jul_Aug.tif", "t3_ndvi2024May.tif"]

temp_data_list = [rasterio.open(data_dir + file).read(1) for file in temp_files]
ndvi_data_list = [rasterio.open(data_dir + file).read(1) for file in ndvi_files]

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
cmap = 'viridis'

show(temp_data_list[0], ax=axes[0], cmap=cmap)
axes[0].set_title("Temperature Jul-Aug 2023")

show(ndvi_data_list[0], ax=axes[1], cmap=cmap)
axes[1].set_title("NDVI Jul-Aug 2023")

combined = np.dstack((ndvi_data_list[0], temp_data_list[0], np.zeros_like(ndvi_data_list[0])))
axes[2].imshow(combined / np.max(combined)) 
axes[2].set_title("Combined Visualization Jul-Aug 2023")

plt.show()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].hist(temp_data_list[0].flatten(), bins=50, color='red', alpha=0.7)
axes[0].set_title("Temperature Histogram Jul-Aug 2023")
axes[0].set_xlabel("Temperature")
axes[0].set_ylabel("Frequency")

axes[1].hist(ndvi_data_list[0].flatten(), bins=50, color='green', alpha=0.7)
axes[1].set_title("NDVI Histogram Jul-Aug 2023")
axes[1].set_xlabel("NDVI")
axes[1].set_ylabel("Frequency")

plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(ndvi_data_list[0].flatten(), temp_data_list[0].flatten(), alpha=0.3, color='blue')
plt.xlabel("NDVI")
plt.ylabel("Temperature")
plt.title("Scatter Plot: NDVI vs Temperature Jul-Aug 2023")
plt.show()
