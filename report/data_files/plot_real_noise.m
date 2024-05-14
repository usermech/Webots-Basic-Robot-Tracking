clear all
close all
clc

gps_table = readtable('gps_results_real_noise.txt');
x_results = table2array(gps_table(:,1));
y_results = table2array(gps_table(:,2));

figure 
plot(x_results,y_results,'*');
ylim([-0.8 0.8]);
xlim([2.9 3.1]);
title('Resulting Position of The Robot')
xlabel('Position in x (m)')
ylabel('Position in y (m)')
hold on
plot(3,3,'x');
