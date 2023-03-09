from dinosaur import Dinosaur
from robot import Robot
# imported both Robot and Dinosaur classes into the Battlefield

class Battlefield:
    def  __init__(self):
        self.robot = Robot("RX714")
        self.dinosaur = Dinosaur("T-Rex20", 50)
        my_robot = Robot("RX714")
        my_dinosaur = Dinosaur("T-Rex20", 50)


    #def run_game(self):

    def game_greeting():
        greeting_input = input("Greetings and welcome to battle! Who will win this war? Will it be 1.", my_dinosaur.name "or 2.", my_robot.name"? " )
        while greeting_input != "1" and greeting_input != "2":
            print("Oops, but that's NOT a choice. AHA, please choose again!") 
            greeting_input = input("Greetings and welcome to battle! Who will win this war? Will it be 1. T-Rex20 or 2. RX714? ")
            
        else:
            if greeting_input== "1": 
                print("Here comes T-Rex20! ROARRRRRRRRRRR!")
            elif greeting_input == "2":
                print("BEEP BOP BOOP! The one and only RX714!")
        return greeting_input

my_dinosaur = Dinosaur("T-Rex20", 100)
my_robot = Robot("RX714")

    




    #def display_weapon(self):
        
        #def battle_phase(self):
           

    #def display_winner(self):





    