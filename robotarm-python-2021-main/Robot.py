# Robotarm bibliotheek inladen
from RobotArm import RobotArm
            
# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
robotArm = RobotArm('exercise 1')
            
# Jouw python instructies zet je vanaf hier:

# Na jouw code wachten tot het sluiten van de window:
robotArm.randomLevel(5,3)
robotArm.moveRight();
robotArm.grab()
robotArm.moveRight();
robotArm.drop()
robotArm.wait()