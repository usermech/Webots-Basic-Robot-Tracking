"""lidar_data controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor,Lidar
import matplotlib.pyplot as plt
import numpy as np
import math
import time



# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# get the motor devices
leftMotor = robot.getDevice('left_wheel')
rightMotor = robot.getDevice('right_wheel')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)

# get the lidar device
lidar = robot.getDevice('Sick LMS 291')
lidar.enable(timestep)
lidar.enablePointCloud()

# max_range = lidar.getMaxRange()
# num_points = lidar.getNumberOfPoints()




# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the lidar data
    lidarData = lidar.getRangeImage()
    np.savetxt('lidar_noisy_data.csv', lidarData, delimiter=',')
    plt.polar(np.linspace(np.pi, 0, len(lidarData)), lidarData)    
    plt.ylim(0, 10)
    plt.pause(0.0001)
    plt.clf()
    pass
plt.show()

# export data to csv
np.savetxt('lidar_data.csv', lidarData, delimiter=',')

# Enter here exit cleanup code.
