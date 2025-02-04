
data_dir = "/Users/patryksusz/Documents/exam20240204/team4/task1/";
temp_files = {"t3_lst2023_Jul_Aug.tif", "t3_lst2024May.tif"};
ndvi_files = {"t3_ndvi2023_Jul_Aug.tif", "t3_ndvi2024May.tif"};

temp_data1 = imread(fullfile(data_dir, temp_files{1}));
temp_data2 = imread(fullfile(data_dir, temp_files{2}));
ndvi_data1 = imread(fullfile(data_dir, ndvi_files{1}));
ndvi_data2 = imread(fullfile(data_dir, ndvi_files{2}));

figure;
subplot(1,3,1);
imagesc(temp_data1);
colormap('parula');
colorbar;
title('Temperature Jul-Aug 2023');

subplot(1,3,2);
imagesc(ndvi_data1);
colormap('parula');
colorbar;
title('NDVI Jul-Aug 2023');

subplot(1,3,3);
combined = cat(3, ndvi_data1, temp_data1, zeros(size(ndvi_data1)));
imshow(combined / max(combined(:)));
title('Combined Visualization Jul-Aug 2023');

figure;
subplot(1,2,1);
histogram(temp_data1(:), 50, 'FaceColor', 'r', 'FaceAlpha', 0.7);
title('Temperature Histogram Jul-Aug 2023');
xlabel('Temperature');
ylabel('Frequency');

subplot(1,2,2);
histogram(ndvi_data1(:), 50, 'FaceColor', 'g', 'FaceAlpha', 0.7);
title('NDVI Histogram Jul-Aug 2023');
xlabel('NDVI');
ylabel('Frequency');

figure;
scatter(ndvi_data1(:), temp_data1(:), 10, 'b', 'filled', 'MarkerFaceAlpha', 0.3);
xlabel('NDVI');
ylabel('Temperature');
title('Scatter Plot: NDVI vs Temperature Jul-Aug 2023');
grid on;