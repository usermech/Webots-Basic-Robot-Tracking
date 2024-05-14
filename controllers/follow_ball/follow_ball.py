"""get_camera controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Camera
import cv2
import numpy as np
# create the Robot instance.
robot = Robot()
# get camera
camera = robot.getDevice("camera")
camera.enable(2)
# get wheel motors
leftMotor = robot.getDevice("left_wheel")
rightMotor = robot.getDevice("right_wheel")
#enable motors
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

def find_ball(image):
    # find green ball in the image
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([70, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    # find contours in the mask and initialize the current
    # (x, y) center of the ball
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
    # only proceed if at least one contour was found
    if len(cnts) > 0:
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        try:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            # return the center of the ball and the radius
            return center, radius
        except:
            return None, None
        
# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)
# get GPS 
gps = robot.getDevice('gps')
gps.enable(timestep)


# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:    
    gps_reading = gps.getValues()
# save each encoder value to a new line in the file
    with open('gps_following.txt', 'a') as f:
            f.write(str(gps_reading[0]) + ' '+ str(gps_reading[1]) +'\n')
    # Get image and convert to OpenCV format
    img = camera.getImage()
    img = np.frombuffer(img, np.uint8).reshape(camera.height, camera.width, 4)
    image = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)    
    image = cv2.flip(image, 1)
    center, radius = find_ball(image)
    if center is not None:        
        speedError = 120 - radius
        if radius < 120:
            speed = (0.2 + speedError*0.1) * leftMotor.getMaxVelocity()
        elif radius < 140:
            speed = (0.2 + speedError*0.2) * leftMotor.getMaxVelocity()
        else:
            speed = 0
        
        
        # calculate the error
        error = center[0] - image.shape[1] / 2
        print("error: ", error)
        print("Radius: ", radius)
        print(center[0])

        # calculate the speed of the wheels
        leftSpeed = speed - error * 0.06
        rightSpeed = speed + error * 0.06
        # set the motor speeds
        leftMotor.setVelocity(leftSpeed)
        rightMotor.setVelocity(rightSpeed)
        print("left speed: ", leftSpeed)
        print("right speed: ", rightSpeed)
    
    # Display image
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
