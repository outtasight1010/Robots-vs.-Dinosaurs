
class Weapon:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        

    def random_weapon(self):
        import random
        weapons_list = ["Axe", "Grenade", "Maschete"]
        print("Ok, looks like we will pick a new weapon from the arsenal.It looks like a fight to the finish!")
        print("")
        
        weapon_choice = random.choice(weapons_list)
        print("Here is your new weapon:",weapon_choice,"! OH MY!")
        print("")
        
        return weapon_choice
    
    

    

my_weapon = Weapon("",100)







