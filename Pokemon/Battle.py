'''
Created on January 21, 2024
Author: Brandon Hemminghaus
'''

class Trutwig:
    def __init__(self):
        self.hp = 200
        self.defe = 50
        self.speed = 20
        self.move_names = ["Razor leaf", "Tackle"]
        self.move_damage = [50, 30]
    
    def display(self):
        print("Trutwig stats:")
        print("Hp: " + str(self.hp))
        print("Defense: " + str(self.defe))
        print("Speed: " + str(self.speed))
        print("Moves:")
        for i in range(len(self.move_names)):
            print(" Move " + str(i+1) + ": " + self.move_names[i] + "(" + str(self.move_damage[i]) + ")")

print("Welcome to the pokemon world's final match")
print("Battle between Shirou and DoubleProtect")
print("Pick your pokemon")
mon_1 = Trutwig()
mon_1.display()