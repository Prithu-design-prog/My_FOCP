#task1
"""
Last week you wrote a program that printed out a cheery greeting including your
name. Take a copy of it, and modify it so that the user enters their name at the
keyboard, and then receives a greeting. For example:
Hello, what is your name?
 Mr Apricot
Hello, Mr Apricot. Good to meet you!
"""
name = input("Hello, what is your name? ")
print("Hello, Dear " + name + ". Good to meet you!")

 #task 2
"""
Write a program that prompts a user to enter a temperature in Celsius, and then
displays the corresponding temperature in Fahrenheit, like so:
Enter a temperature in Celsius: 32.5
32.5C is equivalent to 90.5F.
 """
celsius = int(input("Enter the Temperature in Celsius:\n"))

fahrenheit = (1.8 * celsius) + 32

print(str(celsius) + " is equivalent to " + str(fahrenheit) + " Fahrenheit.")

#task 3

"""
The Head of Computing at the University of Poppleton is tasked with dividing a
group of students into lab groups. A lab group is usually 24 students, but this is
sometimes varied to create groups of similar size. Write a program that prompts for
the number of students and group size, and then displays how many groups will be
needed and how many will be left over in a smaller group.
How many students? 113
Required group size? 22
There will be 5 groups with 3 students left over.
"""


num_students = 113
required_size = 22
groups = num_students // required_size

remaining_students = num_students % groups
print("There will be " + str(groups) + " group and " + str(remaining_students) + " leftovers.")


#task 4

"""
A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
first count the sweets and then divide them according to how many pupils attend
that day. Write a program that will tell the teacher how many sweets to give to each
pupil, and how many she will have left over.
"""

num_students = int(input("How many students? "))
num_sweets = int(input("how many sweets ? "))
sweets_per_student = num_sweets // num_students
remaining_sweets = num_sweets % num_students
print("Each student should receive " + str(sweets_per_student) + " sweets and " + str(remaining_sweets) + "will be leftovers.")



