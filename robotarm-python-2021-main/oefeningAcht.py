from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:

i = 3
# Na jouw code wachten tot het sluiten van de window:
for i in range (7):
    for i in range (9):
        robotArm.moveRight();
        robotArm.grab()
    robotArm.drop()
    for i in range (8):
        robotArm.moveLeft();
    robotArm.grab()
   