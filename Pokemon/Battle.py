'''
Created on January 21, 2024
Author: Brandon Hemminghaus
'''

class Pokemon:
    def __init__(self,name,hp,defe,speed,moves):
        self.name = name
        self.hp = hp
        self.defe = defe
        self.speed = speed
        self.moves = moves
    
    def display(self):
        print(self.name + " stats:")
        print("Hp: " + str(self.hp))
        print("Defense: " + str(self.defe))
        print("Speed: " + str(self.speed))
        print("Moves: " + str(self.moves) + "\n")
    
    def pick_move(self,m):
        print(self.name + " used " + m)
        return self.moves.get(m)

print("Welcome to the pokemon world's final match")
print("Battle between Shirou_BH and Operation_X")
print("Pick your pokemon:")
Turtwig = Pokemon("Turtwig",200,50,20,{"Razor leaf": 40, "Tackle": 30})
Turtwig.display()

Chimchar = Pokemon("Chimchar",150,25,60,{"Ember": 50, "Scratch": 30})
Chimchar.display()

Piplup = Pokemon("Piplup",180,40,40,{"Water gun": 40, "Peck": 30})
Piplup.display()