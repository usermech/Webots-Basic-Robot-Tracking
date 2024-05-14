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
# leftMotor = robot.getDevice("left_wheel")
# rightMotor = robot.getDevice("right_wheel")



# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    
    # Get image and convert to OpenCV format
    image = camera.getImageArray()
    image = np.asarray(image, dtype=np.uint8)
    image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)
    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    # image = cv2.resize(image,(1280,720))
    image = cv2.flip(image, 1)
    # Save image
    cv2.imwrite("image5.jpg", image)
    # Display image
    
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
