from controller import Robot, Motor, GPS
import matplotlib.pyplot as plt
import numpy as np
import random
# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())


# Initialize motors
motors = []
motorNames = ['left_wheel', 'right_wheel']
for i in range(len(motorNames)):
    motors.append(robot.getDevice(motorNames[i]))
    motors[i].setPosition(float('inf'))
    motors[i].setVelocity(0.0)
#initalize gps
gps = robot.getDevice('gps')
gps.enable(timestep*10)

gps_x_values =[]
gps_y_values =[]
# Main loop:
# - perform simulation steps until Webots is stopping the controller
velocity = 5
while robot.step(timestep) != -1:
# Read GPS values
   
    left_error = 1*(np.random.normal(0,0.5))
    right_error = 1*(np.random.normal(0,0.5))
    gps_reading = gps.getValues()
    #go straight for 5 meters
    if robot.getTime() < 5.032:
        motors[0].setVelocity(5+left_error)
        motors[1].setVelocity(5+right_error)
    else:
         with open('gps_results.txt', 'a') as f:
            f.write('\n' + str(gps_reading[0]) + ' ' + str(gps_reading[1]) )
   
         for i in range(len(motorNames)):
            motors[i].setVelocity(0)
         break
         
             
     
          

     
     
    