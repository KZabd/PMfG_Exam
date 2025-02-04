import numpy as np
import matplotlib.pyplot as plt
import rasterio
from rasterio.plot import show


lst_1 = rasterio.open("C:/Users/KN/OneDrive/Dokumenty/Exam_task1/t1_lst2023_Jul_Aug.tif").read()
ndvi_1 = rasterio.open("C:/Users/KN/OneDrive/Dokumenty/Exam_task1/t1_ndvi2023_Jul_Aug.tif").read()


fig, axes = plt.subplots(1, 3, figsize=(15, 5))
cmap = 'viridis'

show(lst_1, ax=axes[0], cmap=cmap)
axes[0].set_title("Temperature Jul-Aug 2023")

show(ndvi_1, ax=axes[1], cmap=cmap)
axes[1].set_title("NDVI Jul-Aug 2023")

combined = np.dstack((ndvi_1, lst_1, np.zeros_like(ndvi_1)))
axes[2].imshow(combined / np.max(combined))  # Normalize for display
axes[2].set_title("Combined Visualization Jul-Aug 2023")

plt.show()


fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].hist(lst_1.flatten(), bins=50, color='red', alpha=0.7)
axes[0].set_title("Temperature Histogram Jul-Aug 2023")
axes[0].set_xlabel("Temperature")
axes[0].set_ylabel("Frequency")

axes[1].hist(ndvi_1.flatten(), bins=50, color='green', alpha=0.7)
axes[1].set_title("NDVI Histogram Jul-Aug 2023")
axes[1].set_xlabel("NDVI")
axes[1].set_ylabel("Frequency")

plt.show()


plt.figure(figsize=(8, 6))
plt.scatter(ndvi_1.flatten(), lst_1.flatten(), alpha=0.3, color='blue')
plt.xlabel("NDVI")
plt.ylabel("Temperature")
plt.title("Scatter Plot: NDVI vs Temperature Jul-Aug 2023")
plt.show()