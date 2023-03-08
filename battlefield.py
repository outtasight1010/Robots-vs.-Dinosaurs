class Battlefield:
    def  __init__(self):
        self.robot = Robot()
        self.dinosaur = Dinosaur()


    def run_game(self):
        greeting_input = input("Greetings and welcome to battle! Who will win this war? Will it be 1.", my_dinosaur.name, " or 2.", my_robot.name " ?")
        while greeting_input != "1" and greeting_input != "2":
            print("Oops, but that's NOT a choice. AHA, please choose again!") 
            greeting_input = input("Greetings and welcome to battle! Who will win this war? Will it be 1.", my_dinosaur.name, " or 2.", my_robot.name " ?")
        else:
            if greeting_input== "1": 
                print("Here comes ", my_dinosaur.name,"! ROARRRRRRRRRRR!")
            elif greeting_input == "2":
                print("BEEP BOP BOOP! The one and only", my_robot.name"!")

        return greeting_input
    




    def display_weapon(self):
        
    def battle_phase(self):
        pass

    def display_winner(self):





    