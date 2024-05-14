clear all
close all
clc

%% uncomment this section for noiseless plot and comment noisy data section
% encoder_table = readtable('encoder_values.txt');
% x_array=table2array(encoder_table(:,1));
% y_array=table2array(encoder_table(:,2));
%% Noisy data plot
encoder_table = readtable('noisy_encoder_values.txt');
x_array=table2array(encoder_table(:,1));
y_array=table2array(encoder_table(:,2));

gps_table = readtable('gps_values.txt');
x_gps=table2array(gps_table(:,1));
y_gps=table2array(gps_table(:,2));

figure
plot(x_array,y_array,'*');
hold on
plot(x_gps,y_gps,'o');
xlim([-0.2 1.7])
grid on


