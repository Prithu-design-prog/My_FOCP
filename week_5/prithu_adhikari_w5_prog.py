"""
1
Using command-line arguments involves the sys module. Review the docs for this
module and using the information in there write a short program that when run
from the command-line reports what operating system platform is being used.
""""



import sys

print(f"The operating system platform is {sys.platform}.")

#The operating system platform is win32.


#2
"""
Write a program that, when run from the command line, reports how many
arguments were provided. (Remember that the program name itself is not an
argument)
"""

import sys

num_arguments = len(sys.argv) - 1

print(f"Number of arguments provided: {num_arguments}")

#Number of arguments provided: 3

#3

"""Write a program that takes a bunch of command-line arguments, and then prints
out the shortest. If there is more than one of the shortest length, any will do.
Hint: Don't overthink this. A good way to find the shortest is just to sort them.

?"""
import sys

arguments = sys.argv[1:]

if arguments:
    shortest_argument = sorted(arguments, key=len)[0]
    print(f"The shortest argument is: {shortest_argument}")
else:
    print("No arguments provided.")

# python question_3.py 12 13 14 15
    # The shortest argument is: 12

#4
    """
    Write a program that takes a URL as a command-line argument and reports
whether or not there is a working website at that address.
Hint: You need to get the HTTP response code.
Another Hint: StackOverflow is your friend
"""
import sys
import requests

STACK_OVERFLOW_URL = "https://stackoverflow.com"

def check_stack_overflow():
    try:
        response = requests.head(STACK_OVERFLOW_URL)
        if response.status_code == 200:
            print(f"The Stack Overflow website at {STACK_OVERFLOW_URL} is working.")
        else:
            print(f"The Stack Overflow website at {STACK_OVERFLOW_URL} returned a non-OK status code: {response.status_code}")
    except requests.ConnectionError:
        print(f"Could not connect to {STACK_OVERFLOW_URL}. Check your internet connection.")

if __name__ == "__main__":
    check_stack_overflow()


#pip install requests
    #C:\Users\Dell\OneDrive\Desktop>python hyu.py
#The Stack Overflow website at https://stackoverflow.com is working.
    
#5
    """
    Last week you wrote a program that processed a collection of temperature readings
entered by the user and displayed the maximum, minimum, and mean. Create a
version of that program that takes the values from the command-line instead. Be
sure to handle the case where no arguments are provided!
"""
import sys

if len(sys.argv) > 1:
    Temp = [float(temp) for temp in sys.argv[1:]]
    if Temp:
        max_temp = max(Temp)
        min_temp = min(Temp)
        mean_temp = sum(Temp) / len(Temp)

        print(f"Max temperature: {max_temp}")
        print(f"Min temperature: {min_temp}")
        print(f"Mean temperature: {mean_temp}")
    else:
        print("Provide temperature values.")


#6
"""
Write a program that takes the name of a file as a command-line argument, and
creates a backup copy of that file. The backup should contain an exact copy of the
contents of the original and should, obviously, have a different name.
Hint: By now, you should be getting the idea that there is a built-in way to do the
heavy lifting here! Take a look at the "Brief Tour of the Standard Library" in the docs.
"""

import sys
import shutil

def create_backup(city):
    try:
        citylight = city + '.bak'
        shutil.copy2(city, citylight)
        print(f"Backup created successfully. Original file: {city}, Backup file: {citylight}")
    except FileNotFoundError:
        print(f"Error: File '{city}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    city = 'hello.py'
    create_backup(city)
    

    

    
    




