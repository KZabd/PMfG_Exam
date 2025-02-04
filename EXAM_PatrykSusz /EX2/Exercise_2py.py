import rasterio
import numpy as np
import laspy
import pandas as pd
from scipy.interpolate import RegularGridInterpolator


dem_path = "/Users/patryksusz/Documents/exam20240204/team4/task2/files4/Lubin_2024_03_27.asc"
point_cloud_path = "/Users/patryksusz/Documents/exam20240204/team4/task2/files4/Lubin_2024_03_27_pc.laz"


with rasterio.open(dem_path) as dem:
    dem_data = dem.read(1)  
    transform = dem.transform  
    x_size, y_size = dem.width, dem.height

 
    x_coords = np.arange(x_size) * transform.a + transform.c
    y_coords = np.arange(y_size) * transform.e + transform.f

 
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


dem_heights = interp_dem(np.vstack((pc_y, pc_x)).T)


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
