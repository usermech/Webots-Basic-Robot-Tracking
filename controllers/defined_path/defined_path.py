from controller import Robot
import time
import math
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

# get GPS 
gps = robot.getDevice('gps')
gps.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller

while robot.step(timestep) != -1:
    gps_reading = gps.getValues()
# save each encoder value to a new line in the file
    with open('gps_followed.txt', 'a') as f:
            f.write(str(gps_reading[0]) + ' '+ str(gps_reading[1]) +'\n')

    # for first 6 seconds, move forward
    if robot.getTime() < 2:
        motors[0].setPosition(float('inf'))          
        motors[1].setPosition(float('inf'))  
        motors[0].setVelocity(3)       
        motors[1].setVelocity(3)
    # for next 6 seconds, turn left
    elif robot.getTime() < 3:
    #set wheel velocity to 1 m/s 
        motors[0].setPosition(float('inf'))          
        motors[1].setPosition(float('inf'))         
        motors[0].setVelocity(1) 
        motors[1].setVelocity(4)
    # for the next 4 seconds, move forward
    elif robot.getTime() < 6:
        motors[0].setVelocity(5)
        motors[1].setVelocity(5)
    elif robot.getTime() < 8:
    #set wheel velocity to 1 m/s 
        motors[0].setPosition(float('inf'))          
        motors[1].setPosition(float('inf'))         
        motors[0].setVelocity(4) 
        motors[1].setVelocity(2)
         # for the next 4 seconds, move forward
    elif robot.getTime() < 12:
        motors[0].setVelocity(3)
        motors[1].setVelocity(3)
    elif robot.getTime() < 17.5:
    #set wheel velocity to 1 m/s 
        motors[0].setPosition(float('inf'))          
        motors[1].setPosition(float('inf'))         
        motors[0].setVelocity(4) 
        motors[1].setVelocity(6)
         # for the next 4 seconds, move forward
    elif robot.getTime() < 22:
        motors[0].setVelocity(4)
        motors[1].setVelocity(4)
    
    else:
        motors[0].setVelocity(0)
        motors[1].setVelocity(0)
   


   
        
    pass