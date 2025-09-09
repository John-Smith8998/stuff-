#Random module
import random

#A class to create rolls of the dice and their attributes
class die:
    def __init__(self,points,num):
        self.points = points
        self.num = num

#Function to roll dice
def DiceRoll():
    roll = random.randint(1,6)
    return roll

def ScoreCalc(dice_list):
    total = 0
    for x in range(len(dice_list)):
        total = total + dice_list[x].points #Looks at the 'points' atrribute of the current roll and adds it to a total
    return total

dice_list = [] #The list of dice objects

for x in range(5):
    roll = DiceRoll() #Decides the roll of the dice(1-6)
    if roll == 3:
        roll = die(2,roll) #Assigining the right amount of points to the roll by creating it as a 'die' object
    elif roll == 5:
        roll = die(4,roll)
    else:
        roll = die(0,roll)
        
    dice_list.append(roll) #Adding this die object to the list

points = ScoreCalc(dice_list)

print("Dice: ")
for z in range(len(dice_list)):
    print(dice_list[z].num) #Prints the actual dice rolls
print("\nThis is the total points:",points)