"""Leader controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Motor, Keyboard

# create the Robot instance.
robot = Robot()
MAX_SPEED= 5.0
# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())
MOTOR_LEFT= robot.getDevice('left wheel motor')
MOTOR_RIGHT = robot.getDevice('right wheel motor')
keyboard = robot.getKeyboard()
keyboard.enable(timestep)
MOTOR_LEFT.setPosition(float('inf'))
MOTOR_RIGHT.setPosition(float('inf'))

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
vL=0
vR=0

while robot.step(timestep) != -1:
    key = keyboard.getKey()
    while(keyboard.getKey() != -1): continue
    if key == ord('A') :
        vL = -MAX_SPEED
        vR = MAX_SPEED
    elif key == ord('D'):
        vL = MAX_SPEED
        vR = -MAX_SPEED
    elif key == ord('W'):
        print("W is being pressed")
        vL = MAX_SPEED
        vR = MAX_SPEED
    elif key == ord('S'):
        vL = -MAX_SPEED
        vR = -MAX_SPEED
    elif key==-1:
        vL = 0
        vR = 0
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    MOTOR_LEFT.setVelocity(vL)
    MOTOR_RIGHT.setVelocity(vR)
    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)

# Enter here exit cleanup code.
