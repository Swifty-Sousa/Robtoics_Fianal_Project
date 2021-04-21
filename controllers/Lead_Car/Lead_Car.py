"""Lead_Car controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, LED, DistanceSensor, Motor, Keyboard

robot = Robot()
timestep = int(robot.getBasicTimeStep())
MAX_SPEED =  5.0
# create the Robot instance.
ring_leds=[]
led_name=['led0', 'led1', 'led2', 'led3', 'led4', 'led5', 'led6', 'led7']

for i in led_name:
    ring_leds.append(robot.getDevice(i))
body_led= robot.getDevice('led8')
# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

MOTOR_LEFT = robot.getDevice('left wheel motor')
MOTOR_RIGHT= robot.getDevice('right wheel motor')
keyboard = robot.getKeyboard()
keyboard.enable(timestep)
MOTOR_LEFT.setPosition(float('inf'))
MOTOR_RIGHT.setPosition(float('inf'))
#led0-led7 are the red ring on top
#led 8 is the greed ring 



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
    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    MOTOR_LEFT.setVelocity(vL)
    MOTOR_RIGHT.setVelocity(vR)
    if vL ==0 and vR==0:
        # turn on red ring and turn off green body light
        body_led.set(0)
        for i in ring_leds:
            i.set(1)
    else:
        #turn off red ring and turn on green body light
        body_led.set(1)
        for i in ring_leds:
            i.set(0)
# Enter here exit cleanup code.
