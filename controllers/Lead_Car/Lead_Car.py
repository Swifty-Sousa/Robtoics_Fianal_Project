"""Lead_Car controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, LED, DistanceSensor, Motor, Keyboard

MAX=  7.0
LEFT_MOTOR=  
RIGHT_MOTOR=
# create the Robot instance.
robot = Robot()
'''leds=[]
led_name=['led0', 'led1', 'led2', 'led3', 'led4', 'led5', 'led6', 'led7', 'led8', 'led9']

for i in range(len(led_name)):
    leds.append(robot.getDevice(led_name))
# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())
leds[9].wb_led_set(1)
'''
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')




while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    leftMotor.setPosition(10.0)
    rightMotor.setPosition(10.0)
    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
