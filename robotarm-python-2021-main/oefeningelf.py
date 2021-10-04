from pygame.constants import WINDOWHITTEST
from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:
color = "white"
# Na jouw code wachten tot het sluiten van de window:
for i in range (1):
    for i in range (9):
        robotArm.moveRight();
    for i in range (15):
        robotArm.grab()
        color = robotArm.scan()
        print(color)
        if color == "white":
            robotArm.moveRight();
            robotArm.drop()
            robotArm.moveLeft();
        else:
            robotArm.drop()
            robotArm.moveLeft();



