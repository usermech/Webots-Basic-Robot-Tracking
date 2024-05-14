from controller import Robot, Motor
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
#get positional encoders
encoders = []
encoderNames = ['left_encoder', 'right_encoder']
for i in range(len(encoderNames)):
    encoders.append(robot.getDevice(encoderNames[i]))
    encoders[i].enable(timestep)
# get GPS 
gps = robot.getDevice('gps')
gps.enable(timestep)

# wheel radius
wheelRadius = 0.12
axleLength = 0.36
distValues = [0, 0]
robotPose = [0, 0, 0]
lastDistValues = [0, 0]
counter = 0
# Main loop:
# - perform simulation steps until Webots is stopping the controller

while robot.step(timestep) != -1:    
    # for first 6 seconds, move forward
    if robot.getTime() < 9:
        motors[0].setPosition(12.5)
        motors[0].setVelocity(2)
        motors[1].setPosition(12.5)
        motors[1].setVelocity(2)
    # for next 6 seconds, turn left
    elif robot.getTime() < 11.35:
    #set wheel velocity to 1 m/s 
        motors[0].setPosition(float('inf'))          
        motors[1].setPosition(float('inf'))         
        motors[0].setVelocity(-1) 
        motors[1].setVelocity(1)
    # for the next 4 seconds, move forward
    elif robot.getTime() < 17.60:
        motors[0].setVelocity(2)
        motors[1].setVelocity(2)
    elif robot.getTime() < 19.95:
    #set wheel velocity to 1 m/s 
        motors[0].setPosition(float('inf'))          
        motors[1].setPosition(float('inf'))         
        motors[0].setVelocity(-1) 
        motors[1].setVelocity(1)
         # for the next 4 seconds, move forward
    elif robot.getTime() < 26.15:
        motors[0].setVelocity(2)
        motors[1].setVelocity(2)
    elif robot.getTime() < 28.54:
    #set wheel velocity to 1 m/s 
        motors[0].setPosition(float('inf'))          
        motors[1].setPosition(float('inf'))         
        motors[0].setVelocity(-1) 
        motors[1].setVelocity(1)
         # for the next 4 seconds, move forward
    elif robot.getTime() < 34.79:
        motors[0].setVelocity(2)
        motors[1].setVelocity(2)
    elif robot.getTime() < 37.15:
    #set wheel velocity to 1 m/s 
        motors[0].setPosition(float('inf'))          
        motors[1].setPosition(float('inf'))         
        motors[0].setVelocity(-1) 
        motors[1].setVelocity(1)
         # for the next 4 seconds, move forward 
    # for the rest of the time stop
    else:
        motors[0].setVelocity(0)
        motors[1].setVelocity(0)
    # read encoders
    left_encoder = encoders[0].getValue()
    right_encoder = encoders[1].getValue()

    for index in range(2):
        distValues[index] = (encoders[index].getValue() - lastDistValues[index]) * wheelRadius
        lastDistValues[index] = encoders[index].getValue()
    v = (distValues[0] + distValues[1]) / 2
    w = (distValues[0] - distValues[1]) / axleLength

    robotPose[2] += w 
    robotPose[0] += v*math.cos(robotPose[2]) 
    robotPose[1] += v*math.sin(robotPose[2])

    # every 0.1 seconds, print the robot's pose
    counter += 1 
    if counter % 10 == 0:
        gps_reading = gps.getValues()
    # save each encoder value to a new line in the file
        with open('encoder_values.txt', 'a') as f:
            f.write(str(robotPose[0]) + ' '+ str(-robotPose[1]) + ' ' + str(robotPose[2])+ ';'+'\n')
        with open('gps_values.txt', 'a') as f2:
                f2.write(str(gps_reading[0]) + ' '+ str(gps_reading[1]) +'\n')
            
        
    pass