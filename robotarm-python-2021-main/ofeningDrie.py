from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

# Jouw python instructies zet je vanaf hier:

i = 3

# Na jouw code wachten tot het sluiten van de window:
for i in range(1):
    robotArm.grab()
    robotArm.moveRight();
    robotArm.drop()
    robotArm.moveLeft();
    robotArm.grab()
    robotArm.moveRight();
    robotArm.drop()
    robotArm.moveLeft();
    robotArm.grab()
    robotArm.moveRight();
    robotArm.drop()
    robotArm.moveLeft();
    robotArm.grab()
    robotArm.moveRight();
    robotArm.drop()