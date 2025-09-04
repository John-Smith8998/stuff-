""" Thief!
A thief has managed to find out the four digits for an online PIN code, but doesn’t know the correct sequence needed to hack into the account.
Design and write a program that displays all the possible combinations for any four numerical digits entered by the user. The program should avoid displaying the same
combination more than once. """

import random

num1 = input("Enter a digit: ")
num2 = input("Enter a digit: ")
num3 = input("Enter a digit: ")
num4 = input("Enter a digit: ")
pin_list = []

for x in range(0,6):
    unique = False
    while unique == False:
        digit_list = [num1,num2,num3,num4]
        digit_1 = digit_list[0]
        digit_list.remove(digit_1)
        digit_2 = random.choice(digit_list)
        digit_list.remove(digit_2)
        digit_3 = random.choice(digit_list)
        digit_list.remove(digit_3)
        digit_4 = random.choice(digit_list)
        pin = (digit_1+digit_2+digit_3+digit_4)
        if pin not in pin_list:
            unique = True
    pin_list.append(pin)

for x in range(0,6):
    unique = False
    while unique == False:
        digit_list = [num1,num2,num3,num4]
        digit_1 = digit_list[1]
        digit_list.remove(digit_1)
        digit_2 = random.choice(digit_list)
        digit_list.remove(digit_2)
        digit_3 = random.choice(digit_list)
        digit_list.remove(digit_3)
        digit_4 = random.choice(digit_list)
        pin = (digit_1+digit_2+digit_3+digit_4)
        if pin not in pin_list:
            unique = True
    pin_list.append(pin)

for x in range(0,6):
    unique = False
    while unique == False:
        digit_list = [num1,num2,num3,num4]
        digit_1 = digit_list[2]
        digit_list.remove(digit_1)
        digit_2 = random.choice(digit_list)
        digit_list.remove(digit_2)
        digit_3 = random.choice(digit_list)
        digit_list.remove(digit_3)
        digit_4 = random.choice(digit_list)
        pin = (digit_1+digit_2+digit_3+digit_4)
        if pin not in pin_list:
            unique = True
    pin_list.append(pin)

for x in range(0,6):
    unique = False
    while unique == False:
        digit_list = [num1,num2,num3,num4]
        digit_1 = digit_list[3]
        digit_list.remove(digit_1)
        digit_2 = random.choice(digit_list)
        digit_list.remove(digit_2)
        digit_3 = random.choice(digit_list)
        digit_list.remove(digit_3)
        digit_4 = random.choice(digit_list)
        pin = (digit_1+digit_2+digit_3+digit_4)
        if pin not in pin_list:
            unique = True
    pin_list.append(pin)

print(pin_list)