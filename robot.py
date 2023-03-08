
class Robot:
    def __init__(self, name):
        self.name = "RX714"
        self.health_meter = 50
        self.power_level = 100
        self.active_weapon = "Sledgehammer"

    def attack(self, dinosaur):
        print("OK, it's RX714's turn!")
        user_attack = input("RX714, are you ready to strike? Type 1. for YES or 2. for No. ")
        while user_attack != "1" and user_attack != "2":
            print("Sorry, you must choose 1 or 2.")
            user_attack = input("Would you like to attack T-Rex20? Type 1. for YES or 2. for No. ")
        else:
            if user_attack == "1":
                print("Congrats, you have used Sledgehammer on T-Rex20! His health is down to 40, and attack power is reduced to 60!")
            elif user_attack == "2": 
                print("Oh boy, looks like T-Rex20 struck you with his Sledgehammer when you weren't looking!!.\nYour health is now 20 and your attack power is 40! \nSucks for you!")
        
        return user_attack
    
