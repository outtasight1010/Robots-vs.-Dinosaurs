from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon
from battlefield import Battlefield

my_dinosaur = Dinosaur("T-Rex20", 100)
my_robot = Robot("RX714")
my_weapon = Weapon("Sledgehammer", 100)


print(my_dinosaur.name, my_dinosaur.attack_power)
print(my_robot.name)
print(my_weapon.name)

my_dinosaur.attack("RX714")
my_robot.attack("T-Rex20")
#the_battlefield.run_game()

Battlefield.game_greeting()





