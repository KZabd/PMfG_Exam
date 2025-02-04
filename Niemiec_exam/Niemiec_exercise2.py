
import numpy as np
import laspy
import pandas as pd
from scipy.interpolate import RegularGridInterpolator


dem_path = "C:/Users/KN/Downloads/OneDrive_1_4.02.2025/Lubin_2024_03_27.asc"
point_cloud_path = "C:/Users/KN/Downloads/OneDrive_1_4.02.2025/Lubin_2024_03_27_pc.laz"


def read_asc(file_path):
    with open(file_path, 'r') as f:
        header = {}
        for _ in range(6):
            key, value = f.readline().split()
            header[key.upper()] = float(value) if '.' in value else int(value)

    data = pd.read_csv(file_path, skiprows=6, sep=r'\s+', header=None).values

    return header, data

def get_interpolator(asc_path):

    header, dem_data = read_asc(asc_path)

    x_size, y_size = header['NCOLS'], header['NROWS']
    cell_size = header['CELLSIZE']
    

    x_min = header['XLLCENTER'] - (cell_size / 2)
    y_min = header['YLLCENTER'] - (cell_size / 2)
    

    x_coords = np.arange(x_size) * cell_size + x_min
    y_coords = np.arange(y_size) * -cell_size + (y_min + y_size * cell_size)


    interp_dem = RegularGridInterpolator(
        (y_coords[::-1], x_coords),  
        dem_data[::-1, :],           
        bounds_error=False,
        fill_value=np.nan
    )

    return interp_dem



interpolator = get_interpolator(dem_path)



try:
    las = laspy.read(point_cloud_path, laz_backend=laspy.LazBackend.Lazrs)  
except laspy.errors.LaspyException:
    las = laspy.read(point_cloud_path, laz_backend=laspy.LazBackend.Laszip) 


pc_x = las.x
pc_y = las.y
pc_z = las.z  


dem_heights = interpolator(np.vstack((pc_y, pc_x)).T)


deltaH = pc_z - dem_heights


metrics = {
    "Mean Error (Bias)": np.nanmean(deltaH),
    "Standard Deviation": np.nanstd(deltaH),
    "Root Mean Square Error (RMSE)": np.sqrt(np.nanmean(deltaH**2)),
    "Min DeltaH": np.nanmin(deltaH),
    "Max DeltaH": np.nanmax(deltaH),
}


print("\nAccuracy Metrics:")
for key, value in metrics.items():
    print(f"{key}: {value:.3f}")


df = pd.DataFrame({
    "X": pc_x,
    "Y": pc_y,
    "PointCloud_H": pc_z,
    "DEM_H": dem_heights,
    "DeltaH": deltaH
})
df.to_csv("deltaH_results.csv", index=False)
print("\nResults saved to deltaH_results.csv")
