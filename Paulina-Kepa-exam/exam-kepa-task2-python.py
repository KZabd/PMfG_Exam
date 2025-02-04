##Paulina Kępa, task 1, files no 2 (provided in anaconda jupyter notebook)

import numpy as np
import matplotlib.pyplot as plt
import rasterio

# wczytanie plokow tiff
def load_raster(file):
    with rasterio.open(file) as src:
        return src.read(1), src.transform  # Odczytaj pierwszą warstwę

# moje pliki wejsciowe
temp1_file = "t2_lst2023_Jul_Aug.tif"
ndvi1_file = "t2_ndvi2023_Jul_Aug.tif"
temp2_file = "t2_lst2024May.tif"
ndvi2_file = "t2_ndvi2024May.tif"

# wczytanie danych
temp1, _ = load_raster(temp1_file)
ndvi1, _ = load_raster(ndvi1_file)
temp2, _ = load_raster(temp2_file)
ndvi2, _ = load_raster(ndvi2_file)

# wyswietlanie obrazow
def plot_images(ndvi, temp, title=""):
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    cmap = "viridis"  

    axes[0].imshow(ndvi, cmap=cmap)
    axes[0].set_title("NDVI")
    axes[1].imshow(temp, cmap=cmap)
    axes[1].set_title("Temperature")
    axes[2].imshow(temp - ndvi, cmap="RdBu")
    axes[2].set_title("Difference (Temp - NDVI)")

    fig.suptitle(title)
    plt.show()

# histrogramy
def plot_histograms(ndvi, temp, title=""):
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    
    axes[0].hist(ndvi.flatten(), bins=50, color='g', alpha=0.7)
    axes[0].set_title("NDVI Histogram")
    
    axes[1].hist(temp.flatten(), bins=50, color='r', alpha=0.7)
    axes[1].set_title("Temperature Histogram")

    fig.suptitle(title)
    plt.show()

# plot
def scatter_plot(ndvi, temp, title=""):
    plt.figure(figsize=(6, 6))
    plt.scatter(ndvi.flatten(), temp.flatten(), alpha=0.5, color='blue', s=1)
    plt.xlabel("NDVI")
    plt.ylabel("Temperature")
    plt.title(title)
    plt.grid()
    plt.show()

# analiza temp1/ndvi1
plot_images(ndvi1, temp1, title="Analysis of Temp1 & NDVI1")
plot_histograms(ndvi1, temp1, title="Histograms Temp1 & NDVI1")
scatter_plot(ndvi1, temp1, title="Scatter Plot Temp1 vs NDVI1")

# analiza temp2//ndvi2
plot_images(ndvi2, temp2, title="Analysis of Temp2 & NDVI2")
plot_histograms(ndvi2, temp2, title="Histograms Temp2 & NDVI2")
scatter_plot(ndvi2, temp2, title="Scatter Plot Temp2 vs NDVI2")
