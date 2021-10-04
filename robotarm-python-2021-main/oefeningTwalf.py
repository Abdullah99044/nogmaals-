from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:


# Na jouw code wachten tot het sluiten van de window:
color = "red"
# Na jouw code wachten tot het sluiten van de window:
for i in range (1):
    for i in range (9):
        robotArm.moveRight();
    for i in range (27):
        robotArm.grab()
        color = robotArm.scan()
        print(color)
        if color == "red":
            for i in range(9):
                robotArm.moveRight();
            robotArm.drop()
            robotArm.moveLeft();
        else:
            robotArm.drop()
            robotArm.moveLeft();
