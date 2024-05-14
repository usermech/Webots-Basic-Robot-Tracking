clear all
close all
clc
lidar_table = readtable('lidar_data.csv');
lidar_array=table2array(lidar_table);
lidar_array(isinf(lidar_array)|-isinf(lidar_array))=nan;
noisy_lidar_table = readtable('lidar_noisy_data.csv');
noisy_array=table2array(noisy_lidar_table);
noisy_array(isinf(noisy_array)|-isinf(noisy_array))=nan;

figure
polarplot(linspace(pi,0,length(lidar_array)),lidar_array,'LineWidth',3);
hold on 
polarplot(linspace(pi,0,length(noisy_array)),noisy_array,'LineWidth',1.5);

thetalim([0 180]);

