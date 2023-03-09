class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 50
        

    def attack(self, robot):
        user_attack = input("Would you like to attack RX714? Type 1. for YES or 2. for No. ")
        while user_attack != "1" and user_attack != "2":
            print("Sorry, you must choose 1 or 2.")
            user_attack = input("Would you like to attack RX714? Type 1. for YES or 2. for No. ")
        else:
            if user_attack == "1":
                print("Congrats, you have used Sledgehammer on RX714! His health is down to 40, and attack power is reduced to 80!")
            elif user_attack == "2": 
                print("Oh no, you have been HIT!. Your health is now 30 and your attack power is 70!")

        return user_attack

my_dinosaur = Dinosaur("T-Rex20",100)
print(my_dinosaur.name)
print(my_dinosaur.attack_power)
print(my_dinosaur.health)
    



        
    


