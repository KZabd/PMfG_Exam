import numpy as np
import laspy
import pandas as pd
from scipy.interpolate import RegularGridInterpolator


dem_path = "jupiter01/Lubin_2024_03_27.asc"
point_cloud_path = "jupiter01/Lubin_2024_03_27_pc.laz"


# Funkcja do wczytywania pliku DEM w formacie ASCII
def load_dem_ascii(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # indeksy, które zaczynają się od "ncols", "nrows", "xllcorner" i "yllcorner"
    ncols, nrows, xllcorner, yllcorner, cellsize = None, None, None, None, None
    for line in lines:
        if line.startswith("ncols"):
            ncols = int(line.split()[1])
        elif line.startswith("nrows"):
            nrows = int(line.split()[1])
        elif line.startswith("xllcorner"):
            xllcorner = float(line.split()[1])
        elif line.startswith("yllcorner"):
            yllcorner = float(line.split()[1])
        elif line.startswith("cellsize"):
            cellsize = float(line.split()[1])

    # dane mapy wysokości
    dem_data = np.loadtxt(lines[len(lines)-nrows:])  # Ostatnie nrows wierszy zawierają dane DEM

    #współrzędne X i Y
    x_coords = np.arange(ncols) * cellsize + xllcorner
    y_coords = np.arange(nrows) * cellsize + yllcorner

    return dem_data, x_coords, y_coords


#danee DEM
dem_data, x_coords, y_coords = load_dem_ascii(dem_path)

#interpol dem
interp_dem = RegularGridInterpolator(
    (y_coords[::-1], x_coords),  
    dem_data[::-1, :],         bounds_error=False,
    fill_value=np.nan
)


try:
    las = laspy.read(point_cloud_path, laz_backend=laspy.LazBackend.Lazrs)  
except laspy.errors.LaspyException:
    las = laspy.read(point_cloud_path, laz_backend=laspy.LazBackend.Laszip) 


pc_x = las.x
pc_y = las.y
pc_z = las.z  


#inteporl wysokości DEM dla punktów chmury
dem_heights = interp_dem(np.vstack((pc_y, pc_x)).T)

##różnice wysokości (DeltaH)
deltaH = pc_z - dem_heights


#metrki
metrics = {
    "Mean Error (Bias)": np.nanmean(deltaH),
    "Standard Deviation": np.nanstd(deltaH),
    "Root Mean Square Error (RMSE)": np.sqrt(np.nanmean(deltaH**2)),
    "Min DeltaH": np.nanmin(deltaH),
    "Max DeltaH": np.nanmax(deltaH),
}


#wysw
print("\nAccuracy Metrics:")
for key, value in metrics.items():
    print(f"{key}: {value:.3f}")


#do csv
df = pd.DataFrame({
    "X": pc_x,
    "Y": pc_y,
    "PointCloud_H": pc_z,
    "DEM_H": dem_heights,
    "DeltaH": deltaH
})
df.to_csv("deltaH_results.csv", index=False)
print("\nResults saved to deltaH_results.csv")
