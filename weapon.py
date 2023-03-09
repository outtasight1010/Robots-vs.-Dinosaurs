
class Weapon:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        

    def random_weapon():
        import random
        weapons_list = ["Axe", "Grenade", "Maschete"]
        weapon_choice = random.choice(weapons_list)
        return weapon_choice

    

my_weapon = Weapon.random_weapon()
print(my_weapon)






