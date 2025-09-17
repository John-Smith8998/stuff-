"""Create a program that will only open a text document if the correct password is entered. The user should choose the username and password first and it should also verify
the password before allowing it.
Extensions:
1. Create a random password first of at least 8 characters first as a suggested password
2. Create a random password that contains at least a lowercase, uppercase and special character of at least 8 characters in length
3. Verify that the password given by the user matches:
a. The limits in Extension 1 above
b. The limits in Extension 2 above"""

# Imports libraries
import random
import string

# Random password generator
def PasswordGen():
    recommended_password = ""
    for x in range(8):
        chars = string.ascii_letters + string.digits + '!@#$%^&*()'
        temp = random.choice(chars)
        recommended_password = recommended_password + temp
    print("Recommended password:",recommended_password,"\n")
    return recommended_password

# Gets the correct username and password
def GetPassword():
    generated_password = PasswordGen()
    valid = False
    while valid == False:
        password = input("Create a new password (enter 1 to use recommended password):\n")
        if len(password) > 7:
            valid = True
            return password
        elif password == "1":
            return generated_password
            valid = True
        else:
            print("Please create a password that is at least 8 characters\n")

# Checks the entered password against the actual password
def PasswordCheck(password, input_password):
    if password == input_password:
        return True
    else:
        return False
    
# Gets the user to enter a password
def MainLoop():
    password = GetPassword() # Sets the correct password
    print("\n" * 50) # Clears screen
    valid = False # Represents whether the given password is correct
    # Loops until the correct password is given
    while valid == False:
        user_input = input("\nEnter the password:\n") # Gets input from user
        valid = PasswordCheck(password, user_input) # Checks this input
        # Message if given password is wrong
        if valid == False:
            print("Try again...")
        # Message for if it is correct
        else:
            print("Correct\n")
    # Opens and displays the content of the file
    print("This is the contents of the file:\n")
    file = open("info.txt",)
    print(file.read())

# Runs program
MainLoop()