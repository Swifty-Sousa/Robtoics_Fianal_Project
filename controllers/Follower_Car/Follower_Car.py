"""Follower_Car controller."""

from controller import Robot, Motor, Camera

timestep = 10

# create the Robot instance.
robot = Robot()

# get the motor devices
MOTOR_LEFT = robot.getDevice('left wheel motor')
MOTOR_RIGHT = robot.getDevice('right wheel motor')
# set the target position of the motors

# find and enable camera
cam = robot.getDevice('good_camera')
cam.enable(timestep)
cam.recognitionEnable(timestep)
#cam.
while robot.step(timestep) != -1:
   pass