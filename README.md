# PMfG_Exam
*Python, Matlab for Geoscience Exam repository*

Team 4:
- Katarzyna Zabdyrska (files no 5) LEADER
- Paulina Kępa (files no 2)
- Jakub Niemiec (files no 1)
- Patryk Susz (files no 3)

## RESULTS OF TASK 1
The task was to analyze the correlation between temperature and vegetation index (NDVI). The goal was to examine the relationship between the two variables using the data contained in the files “temp1”, “ndvi1”, “temp2” and “ndvi2”. The analysis involved a series of steps: displaying three images of the defined palettes, creating two histograms for each pair of data, and preparing a scatter plot showing the dependence of NDVI on temperature. The analysis had to be carried out in both Python and Matlab/Octave, which made it possible to compare the results obtained in both environments.

### KATARZYNA ZABDYRSKA

### PAULINA KĘPA

**Python**

In the code, I loaded data from TIFF files (temperature and NDVI) for two periods.Then, for each data set, I displayed the images (NDVI, temperature, difference), created histograms for temperature and NDVI, and made a scatter plot showing the relationship between NDVI and temperature.
Link to the code: https://github.com/KZabd/PMfG_Exam/blob/main/exam-pk1 

**My results:**

![475301823_932573358942718_7545075661727662486_n](https://github.com/user-attachments/assets/66aabf7f-fb2d-4497-9a68-30cac174e10d)
![474877261_1816487249146746_4865969536873401495_n](https://github.com/user-attachments/assets/a4f9d29b-bd8b-4507-869e-28790648fe03)
![475328823_1572135816776796_2248693310029245156_n](https://github.com/user-attachments/assets/f63c8568-041b-4e9c-a8eb-fd289b62712a)

Unfortunatelly I lost a lot of time because there is some problems with rasterio lib :(( but Im sure that I have it on my computer
![image](https://github.com/user-attachments/assets/91e90045-dc00-4419-a8e2-986daea95205)

**Octave**

In this code, I loaded temperature and NDVI data from TIFF files.I then displayed images for temperature, NDVI and their difference. I created histograms for temperature and NDVI and a scatter plot showing the relationship between these variables. All this for the period July-August 2023. Link to the code: https://github.com/KZabd/PMfG_Exam/blob/main/pktask1.m

**My results:**

![FIG1](https://github.com/user-attachments/assets/737e6150-872c-4efe-8892-a22af3358527)
![FIG2](https://github.com/user-attachments/assets/ec20a0ec-3232-4ff4-9e1c-00887b2e3824)
![FIG3](https://github.com/user-attachments/assets/fabefdd1-b89f-47dc-a613-bf17fbc63762)
![FIG4](https://github.com/user-attachments/assets/03e85bd0-726c-4443-8da6-2a8fcfbd2b72)
![Zrzut ekranu 2025-02-04 111041](https://github.com/user-attachments/assets/c2e57675-5baa-46c8-9579-06855950ac39)
![Zrzut ekranu 2025-02-04 111122](https://github.com/user-attachments/assets/a5d457bc-e235-46ba-9608-1960bdcb520f)



### JAKUB NIEMIEC

Task 1 was completely done in MatLab and partially in Python. The NDVI and LST was shown and the histograms for the all 4 raster was calculated. Unfortunately, I didn't manage to do Python part completely, due to the problems with the rasterio, caused probably by the computer. Only the LST and NDVI from 2023 was evaluated.


Python

![475301823_932573358942718_7545075661727662486_n (2)](https://github.com/user-attachments/assets/e6bd0807-9623-4787-9085-d8e0239c6ac8)
![474877261_1816487249146746_4865969536873401495_n (2)](https://github.com/user-attachments/assets/a06cfe0b-87ff-420f-96bb-b31d20b184d8)
![475328823_1572135816776796_2248693310029245156_n (2)](https://github.com/user-attachments/assets/bf08bf0b-f780-43bc-bd98-9757fbd46d45)


Matlab

2023
![untitled2](https://github.com/user-attachments/assets/4f86795b-08e4-4b9d-ae98-0bc83f355eb6)
![untitled](https://github.com/user-attachments/assets/1a64f199-3910-4242-85eb-20e5b1344588)
![untitled1](https://github.com/user-attachments/assets/751347ef-a9cd-4176-b6b7-a7fee35fd4e4)
2024
![untitled4](https://github.com/user-attachments/assets/61e46646-b8c4-43a5-b83a-800f1ecea00a)
![untitled5](https://github.com/user-attachments/assets/4b04ec47-7274-4be3-a8ac-9eef2f305dee)
![untitled3](https://github.com/user-attachments/assets/7795305d-1847-4d3e-a660-7704faf29136)

### PATRYK SUSZ
Exercise 1 : 
The objective was to investigate the correlation between temperature and the vegetation index (NDVI) by analyzing data from the files "temp1," "ndvi1," "temp2," and "ndvi2." The analysis followed a structured approach, including displaying three images with predefined color palettes, generating two histograms for each data pair, and creating a scatter plot to illustrate the relationship between NDVI and temperature. The study was conducted using both Python and MATLAB/Octave, allowing for a comparison of results between the two computational environments. The result of it , is that the python code didnt show the combined part as matlab but other plots are similar

Results PY

![Ex1_py](https://github.com/user-attachments/assets/3be2c09b-6ca3-4208-bab6-6a4bcc2eeb2f)

![Zrzut ekranu 2025-02-4 o 11 10 48](https://github.com/user-attachments/assets/867a32b8-e89a-4392-b46e-888274c6fc54)

![Zrzut ekranu 2025-02-4 o 11 10 28](https://github.com/user-attachments/assets/e6352754-3c3e-4c0b-98a3-0b03696d4132)

![Zrzut ekranu 2025-02-4 o 11 10 15](https://github.com/user-attachments/assets/c5bc1b51-04dd-40e0-a628-af2fe9ab549d)


Results MatLab

![Ex1_ML](https://github.com/user-attachments/assets/49f68a65-950f-4d06-8870-6c39adf2241a)

![3 images ML](https://github.com/user-attachments/assets/142c92c3-1ce5-4a85-b41c-601dcad62d0a)

![Histogram_ML](https://github.com/user-attachments/assets/298310df-e407-4ca9-b0dc-0a2ccfa6148f)

![Scatterplot_ML](https://github.com/user-attachments/assets/51c902ce-e3a7-4331-a4a4-d553d01d09d3)

## RESULTS OF TASK 2
### PATRYK SUSZ
The Result:
![Zrzut ekranu 2025-02-4 o 11 22 53](https://github.com/user-attachments/assets/feed4e9a-f84d-419d-b40d-c8285ab0143c)




