"""Follower_Car controller."""

from controller import Robot, Motor, Camera
from controller import CameraRecognitionObject as CRO

# create the Robot instance.
robot = Robot()
timestep = int(robot.getBasicTimeStep())
MAX_SPEED= 5.0

# get the motor devices
MOTOR_LEFT = robot.getDevice('left wheel motor')
MOTOR_RIGHT = robot.getDevice('right wheel motor')
MOTOR_LEFT.setPosition(float('inf'))
MOTOR_RIGHT.setPosition(float('inf'))
# set the target position of the motors

# find and enable camera
cam = robot.getDevice('good_camera')
cam.enable(timestep)
cam.recognitionEnable(timestep)
#getting the object
#https://stackoverflow.com/questions/60091830/how-to-recognize-objects-using-camera-on-webots


#leader_id= leader.get_id()
#pos= leader.get_postition()
flag = True
size=0
vL=0
vR=0
while robot.step(timestep) != -1:
    if flag:
        #get size for later
        l= cam.getRecognitionObjects()[0]
        size=l.get_size_on_image()
        #print(size)
        flag= False
    leader= cam.getRecognitionObjects()[0]
    leader_id= leader.get_id()
    pos= leader.get_position_on_image()
    size= leader.get_size_on_image()
    #print(size)
    #target is on the left
    #print(pos)
    if pos[0] <250:
        vL= -MAX_SPEED * 0.5
        vR= MAX_SPEED * 0.5
    elif pos[0] > 450:
        vL= MAX_SPEED * 0.5
        vR= -MAX_SPEED *0.5
    elif size[0]> 230:
        vL=0
        vR=0
        #print("we should be stoppping")
    else:
        vL=MAX_SPEED
        vR= MAX_SPEED

    #print(leader)
    #print(leader_id)
    #postition returns a list like this
    #[num1, num2]
    #num1 is left or right (lower is left,  higher), camera width is 640 so middle is about 320
    #num2 is top to bottom which I will ignore because i will be using smaller and larger to see if the 
    
    MOTOR_LEFT.setVelocity(vL)
    MOTOR_RIGHT.setVelocity(vR)
    #print(s)
    #size one image works the same. gives list [n1,n2] with width height respectivly
#print(pos)
    pass