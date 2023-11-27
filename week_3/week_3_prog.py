#Question 1
""""
Modify your greeting program so that if the user does not enter a name (i.e. they
just press enter), the program responds "Hello, Stranger!". Otherwise it should print
a greeting with their name as before.
"""
name = input("Hello, what is your name? ")

if name == "":
    print("Hello, Stranger!")
else:
    print("Hello, " + name + ". Good to meet you!")


#Question 2

"""
Write a program that simulates the way in which a user might choose a password.
The program should prompt for a new password, and then prompt again. If the two
passwords entered are the same the program should say "Password Set" or
similar, otherwise it should report an error.

"""


password1 = input("Enter a new password: ")
password2 = input("Enter the password again for confirmation: ")
if password1 == password2:
    print("Password Set")
else:
    print("Error: Passwords do not match")

#Question 3
"""
Modify your previous program so that the password must be between 8 and 12
characters (inclusive) long.
"""

while True:
    password1 = input("Enter a new password: ")

    if 8 <= len(password1) <= 12:
        password2 = input("Enter the password again for confirmation: ")

        if password1 == password2:
            print("Password Set")
            break 
        else:
            print("Error: Passwords do not match.")
    else:
        print("Error: Password must be between 8 and 12 characters.")


#Question 4

"""
Modify your program again so that the chosen password cannot be one of a list of
common passwords, defined thus:
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
"""

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
while True:
    password1 = input("Enter a new password123: ")
    if 8 <= len(password1) <= 12 and password1 not in BAD_PASSWORDS:
        password2 = input("Enter the password again for confirmation: ")
        if password1 == password2:
            print("Password Set")
            break  
        else:
            print("Error: Passwords do not match.")
    else:
        if password1 in BAD_PASSWORDS:
            print("Error: Common password. Choose a different one.")
        else:
            print("Error: Password must be between 8 and 12 characters.")
            
#Question 5\
"""
Modify your program a final time so that it executes until the user successfully
chooses a password. That is, if the password chosen fails any of the checks, the
program should return to asking for the password the first Time
    """
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
while True:
    password1 = input("Enter a new password456: ")
    if 8 <= len(password1) <= 12 and password1 not in BAD_PASSWORDS:
        password2 = input("Enter the password again for confirmation: ")
        if password1 == password2:
            print("Password Set")
            break  
        else:
            print("Error: Passwords do not match.")
    else:
        if password1 in BAD_PASSWORDS:
            print("Error: Common password. Choose a different one.")
        else:
            print("Error: Password must be between 8 and 12 characters.")

#Question 6
"""
Write a program that displays the "Seven Times Table". That is, the result of
multiplying 7 by every number from 0 to 12 inclusive. The output might start:
0 x 7 = 0
1 x 7 = 7
2 x 7 = 14
and so on.
"""

for i in range(13):
    result = i * 7
    print(f"{i} x 7 = {result}")


#Question 7
"""
Modify your "Times Table" program so that the user enters the number of the table
they require. This number should be between 0 and 12 inclusive.
"""
table_number = int(input("Enter the number 0-12 "))
if 0 <= table_number <= 12:
    for i in range(13):
        result = i * table_number
        print(f"{i} x {table_number} = {result}")
else:
    print("Please enter a number between 0 and 12 inclusive.")

#Question 8
"""
Modify the "Times Table" again so that the user still enters the number of the table,
but if this number is negative the table is printed backwards. So entering "-7"
would produce the Seven Times Table starting at "12 times" down to "0 times".
"""
table_number = int(input("Enter the number for the times table: "))

if table_number >= 0:
    for i in range(13):
        result = i * table_number
        print(f"{i} x {table_number} = {result}")
else:
    for i in range(12, -1, -1):
        result = i * table_number
        print(f"{i} x {table_number} = {result}")
















