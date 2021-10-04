from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:

 
# Na jouw code wachten tot het sluiten van de window:

for i in range(4):
    for i in range(4):
        robotArm.grab()
        for i in range(4):
            robotArm.moveRight();
        robotArm.drop()
        for i in range(4):
            robotArm.moveLeft();
    for i in range(1):
            robotArm.moveRight();


        
        
    

   
        
    
     
     
     
    
         
    
    
    