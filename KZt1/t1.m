
data_dir = "C:/Users/user/Studia_RSG/S2/Python_Matlab_for_Geoscience/Exam/";
temp_files = {"t5_lst2023_Jun_Aug.tif", "t5_lst2024May.tif"};
ndvi_files = {"t5_lst2023_Jun_Aug.tif", "t5_ndvi2024May.tif"};

temp_data1 = imread(fullfile(data_dir, temp_files{1}));
temp_data2 = imread(fullfile(data_dir, temp_files{2}));
ndvi_data1 = imread(fullfile(data_dir, ndvi_files{1}));
ndvi_data2 = imread(fullfile(data_dir, ndvi_files{2}));

function display_images(temp_data, ndvi_data, title_str)
    figure;
    subplot(1,3,1);
    imagesc(temp_data);
    colormap(spring);
    colorbar;
    title(['Temperature ', title_str]);

    subplot(1,3,2);
    imagesc(ndvi_data);
    colormap(spring);
    colorbar;
    title(['NDVI ', title_str]);

    subplot(1,3,3);
    imagesc(temp_data - ndvi_data);  % Różnica temperatury i NDVI
    colormap('jet');
    colorbar;
    title(['Difference (Temp - NDVI) ', title_str]);
end

function display_histograms(temp_data, ndvi_data, title_str)
    figure;
    subplot(1,2,1);
    hist(temp_data(:), 50);  % W Octave zamiast 'histogram' używamy 'hist'
    title(['Temperature Histogram ', title_str]);
    xlabel('Temperature');
    ylabel('Frequency');

    subplot(1,2,2);
    hist(ndvi_data(:), 50);  % W Octave zamiast 'histogram' używamy 'hist'
    title(['NDVI Histogram ', title_str]);
    xlabel('NDVI');
    ylabel('Frequency');
end

function display_scatter_plot(ndvi_data, temp_data, title_str)
    figure;
    scatter(ndvi_data(:), temp_data(:), 10, 'b', 'filled');
    xlabel('NDVI');
    ylabel('Temperature');
    title(['Scatter Plot: NDVI vs Temperature ', title_str]);
    grid on;
end

display_images(temp_data1, ndvi_data1, 'Jun-Aug 2023');
display_histograms(temp_data1, ndvi_data1, 'Jun-Aug 2023');
display_scatter_plot(ndvi_data1, temp_data1, 'Jun-Aug 2023');

display_images(temp_data2, ndvi_data2, 'May 2024');
display_histograms(temp_data2, ndvi_data2, 'May 2024');
display_scatter_plot(ndvi_data2, temp_data2, 'May 2024');


