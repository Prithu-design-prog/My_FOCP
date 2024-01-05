""""
1.
 Using a set comprehension to extract unique letters from an input string s while leaving 
 aside non-alphabetic characters. The sorted() method then guarantees that the letters are 
ordered alphabetically.
""""
def unique_letters(string):
    letters = set()
    for char in string:
        letters.add(char)
    letters = sorted(list(letters))
    return letters
print(unique_letters("cheese"))
#output: ['c', 'e', 'h', 's']
print(unique_letters("python")) 
#output: ['h', 'n', 'o', 'p', 't', 'y']



#2
"""
Write and test three functions that each take two words (strings) as parameters and
return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in both.
Hint: These could all be done programmatically, but consider carefully what topic we
have been discussing this week! Each function can be exactly one line.
"""
def union_letters(word1, word2):
    return sorted(set(word1) | set(word2))

def intersection_letters(word1, word2):
    return sorted(set(word1) & set(word2))

def sym_difference_letters(word1, word2):
    return sorted(set(word1) ^ set(word2))

print(union_letters("hello", "raman"))  #output :['a', 'e', 'h', 'l', 'm', 'n', 'o', 'r']
print(intersection_letters('Hello', 'prithu')) #output : []
print(sym_difference_letters('all', 'good')) #output : ['a', 'd', 'g', 'l', 'o']



#3
"""
Write a program that manages a list of countries and their capital cities. It should
prompt the user to enter the name of a country. If the program already "knows"
the name of the capital city, it should display it. Otherwise it should ask the user to
enter it. This should carry on until the user terminates the program (how this
happens is up to you).
Note: A good solution to this task will be able to cope with the country being entered
variously as, for example, "Wales", "wales", "WALES" and so on
"""
def main():
    country_capital = {}
    while True:
        country = input("Enter the name of a country: ")
        if country.lower() == "exit":
            break
        if country in country_capital:
            print(f"The capital of {country} is {country_capital[country]}")
        else:
            capital = input(f"What is the capital of {country}? ")
            country_capital[country] = capital
            print(f"Added {country} with capital {capital} to the list.")
    print("Goodbye!")

if __name__ == "__main__":
    main()


        
#output
    """
    Enter the name of a country: france
The capital of france is paris
Enter the name of a country: nepal
The capital of nepal is ktm
Enter the name of a country: ktm
What is the capital of ktm? nepal
Added ktm with capital nepal to the list.
Enter the name of a country:
""""
    

