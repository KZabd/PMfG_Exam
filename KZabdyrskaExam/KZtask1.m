clc; clear;

temp1 = imread('/Users/user/Studia_RSG/S2/Python_Matlab_for_Geoscience/Exam/t5_lst2023_Jun_Aug.tif');
temp2 = imread('/Users/user/Studia_RSG/S2/Python_Matlab_for_Geoscience/Exam/t5_lst2024May.tif');
ndvi1 = imread('/Users/user/Studia_RSG/S2/Python_Matlab_for_Geoscience/Exam/t5_ndvi2024_Jul_Aug.tif');
ndvi2 = imread('/Users/user/Studia_RSG/S2/Python_Matlab_for_Geoscience/Exam/t5_ndvi2024May.tif');

% Convert images to double precision for calculations (if not already)
temp1 = double(temp1);
ndvi1 = double(ndvi1);
temp2 = double(temp2);
ndvi2 = double(ndvi2);

%% Display the images and their differences

figure;
colormap(spring);
% Display original images and differences in a 2x3 grid
subplot(3,2,1);
imagesc(temp1);
axis image; title('Land Surface Temperature Jun-Aug 2023');

subplot(3,2,2);
imagesc(ndvi1);
axis image; title('NDVI Jul-Aug 2024');

subplot(3,2,3);
imagesc(temp2);
axis image; title('Land Surface Temperature May 2024');

subplot(3,2,4);
imagesc(ndvi2);
axis image; title('NDVI May 2024');

subplot(3,2,5);
imagesc(temp2 - temp1);
axis image; title('Land Surface Temperature difference');

subplot(3,2,6);
imagesc(ndvi2 - ndvi1);
axis image; title('NDVI difference');

%% Show histograms for each image

figure;
subplot(2,2,1);
hist(temp1(:), 50); % using 50 bins
xlabel('Value'); ylabel('Frequency');
title('Histogram of Land Surface Temperature Jun-Aug 2023');

subplot(2,2,2);
hist(ndvi1(:), 50);
xlabel('Value'); ylabel('Frequency');
title('Histogram of NDVI Jul-Aug 2024');

subplot(2,2,3);
hist(temp2(:), 50);
xlabel('Value'); ylabel('Frequency');
title('Histogram of Land Surface Temperature May 2024');

subplot(2,2,4);
hist(ndvi2(:), 50);
xlabel('Value'); ylabel('Frequency');
title('Histogram of NDVI May 2024');

%% Scatterplots
% For scatter plots, we flatten the images into vectors

% Scatter Plot 1: temp1 (x) vs ndvi1 (y)
figure;
scatter(temp1(:), ndvi1(:), 10, 'filled'); % marker size 10, filled circles
xlabel('Temperature');
ylabel('NDVI');
title('NDVI to Temperature Jun-Aug 2023');

% Scatter Plot 2: temp2 (x) vs ndvi2 (y)
figure;
scatter(temp2(:), ndvi2(:), 10, 'filled');
xlabel('Temperature');
ylabel('NDVI');
title('NDVI to Temperature May 2024');
