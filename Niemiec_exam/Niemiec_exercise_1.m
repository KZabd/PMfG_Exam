lst1 = imread("C:\Users\KN\OneDrive\Dokumenty\Exam_task1\t1_lst2023_Jul_Aug.tif");
lst2 = imread("C:\Users\KN\OneDrive\Dokumenty\Exam_task1\t1_lst2024May.tif");
ndvi1 = imread("C:\Users\KN\OneDrive\Dokumenty\Exam_task1\t1_ndvi2023_Jul_Aug.tif");
ndvi2 = imread("C:\Users\KN\OneDrive\Dokumenty\Exam_task1\t1_ndvi2024May.tif");

figure;
subplot(1,2,1);
imagesc(lst1);
title('LST 2023');
colorbar;

subplot(1,2,2);
imagesc(ndvi1);
title('NDVI 2023');
colorbar;

figure;
subplot(1,2,1);
histogram(lst1(:));
title('LST 2023 - Histogram');
xlabel('Temperatura');

subplot(1,2,2);
histogram(ndvi1(:));
title('NDVI 2023 - Histogram');
xlabel('NDVI');

figure;
scatter(ndvi1(:), lst1(:));
xlabel('NDVI');
ylabel('LST');
title('NDVI 2023 - Temperature');
grid on;

%%

figure;
subplot(1,2,1);
imagesc(lst2);
title('LST 2024');
colorbar;

subplot(1,2,2);
imagesc(ndvi2);
title('NDVI 2024');
colorbar;

figure;
subplot(1,2,1);
histogram(lst2(:));
title('LST 2024 - Histogram');
xlabel('Temperatura');

subplot(1,2,2);
histogram(ndvi2(:));
title('NDVI 2024 - Histogram');
xlabel('NDVI 2024');

figure;
scatter(ndvi2(:), lst2(:));
xlabel('NDVI 2024');
ylabel('LST 2024');
title('NDVI - Temperature');
grid on;