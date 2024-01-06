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
    city = 'ques_6.py'
    create_backup(city)


#C:\Users\Dell\OneDrive\Desktop>python ques_6.py
#Backup created successfully. Original file: ques_6.py, Backup file: ques_6.py.bak
