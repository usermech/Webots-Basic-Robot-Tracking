clear all
close all
clc

following_table = readtable('gps_following.txt');
x_following=table2array(following_table(:,1));
y_following=table2array(following_table(:,2));

followed_table = readtable('gps_followed.txt');
x_followed=table2array(followed_table(:,1));
y_followed=table2array(followed_table(:,2));

distances = sqrt((x_followed - x_following).^2+(y_followed - y_following).^2);
figure
plot(linspace(0,22.4,length(distances)),distances,'LineWidth',2)
hold on 
yline(0.65,'red')
ylim([0 1])
xlim([0 22.4])
title('Tracking Distance vs Time')
xlabel('Simulation Time (s)') 
ylabel('Tracking Distance (m)') 