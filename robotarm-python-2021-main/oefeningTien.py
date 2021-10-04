from random import randrange
from typing import TextIO
from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:

b = 10
# Na jouw code wachten tot het sluiten van de window:
for i in range (5):
    b = b - 1
    for i in range (1):
        for i in range(b):
            robotArm.grab()
            robotArm.moveRight();
        robotArm.drop()
        for i in range(b):
            robotArm.moveLeft();



        


        
        
    

   

    





