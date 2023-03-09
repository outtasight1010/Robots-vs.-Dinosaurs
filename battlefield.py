from dinosaur import Dinosaur
from robot import Robot
# imported both Robot and Dinosaur classes into the Battlefield

class Battlefield:
    def  __init__(self):
        self.robot = Robot("RX714")
        self.dinosaur = Dinosaur("T-Rex20", 50)
        my_robot = Robot("RX714")
        my_dinosaur = Dinosaur("T-Rex20", 50)
    
    

    def run_game(self):
        self.display_welcome()
        print("")
        my_dinosaur.attack_dino("RX714")
        print("")
        my_robot.attack_robot("T-Rex20")
        print("")
        self.battle_phase()


    
    
    
    def display_welcome(self):
        print("Welcome to battle! Which side will win this war? Only one way to find out...It's GO-TIME!" )

    def battle_phase(self):
        print("UH OH, not sure what happened, but", my_dinosaur.name ," and ", my_robot.name," have gone off the rails! They are both going at IT!")
        print("")
        print(my_dinosaur.name,"just attacked ",my_robot.name," with his Sledgehammer! WOW, now ",my_robot.name," just did the same thing to ",my_dinosaur.name,"!")



my_battlefield = Battlefield()
my_dinosaur = Dinosaur("T-Rex20", 100)
my_robot = Robot("RX714")







    




    #def display_weapon(self):
        
        #def battle_phase(self):
           

    #def display_winner(self):





    