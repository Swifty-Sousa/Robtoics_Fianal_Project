from controller import Robot, Motor, Camera

TIME_STEP = 64

# create the Robot instance.
robot = Robot()

# get the motor devices
MOTOR_LEFT = robot.getDevice('left wheel motor')
MOTOR_RIGHT = robot.getDevice('right wheel motor')
# set the target position of the motors
MOTOR_LEFT.setPosition(10.0)
MOTOR_RIGHT.setPosition(10.0)
robot.camera_enable(10)

while robot.step(TIME_STEP) != -1:
   pass