from pygame import Color
from pygame.mixer import stop
from pygame.sndarray import get_arraytype
from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
Color = "white"  "blue"  "red"  "yellow" "green"
b = -1
c = 1
d = 0
# Na jouw code wachten tot het sluiten van de window:

robotArm.grab()
while robotArm.scan() != "": 
        for i in range (1):
            robotArm.moveRight();
        robotArm.drop()
        for i in range (1):
            robotArm.moveLeft();
            robotArm.grab()
        b = b + 1
for i in range (2):
    robotArm.moveRight();
robotArm.moveLeft();
for i in range (b):
    for i in range (d):
        robotArm.moveLeft();
    robotArm.grab()
    for i in range (c):
        robotArm.moveRight();
    robotArm.drop()
    d = d + 1
    c = c + 1
    
        
    
    
    


        
