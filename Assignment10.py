#10-1
In Python you can store data in variables.
In Python you can use loops to repeat actions.
In Python you can define functions to organize your code.
In Python you can work with files and read their contents.
# Read the entire file
filename = 'learning_python.txt'

print("Reading the entire file:")
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

print("\nReading line by line using a list:")
# Read line by line using a list
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())
#10-2
filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    new_line = line.replace('Python', 'C')
    print(new_line.strip())
In C you can store data in variables.
In C you can use loops to repeat actions.
In C you can define functions to organize your code.
In C you can work with files and read their contents.
#10-3
filename = 'learning_python.txt'

print("Reading the entire file:")
with open(filename) as file_object:
    print(file_object.read())

print("\nReading line by line (no temporary variable):")
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())
#10-4
filename = 'guest.txt'

name = input("Please enter your name: ")

with open(filename, 'w') as file_object:
    file_object.write(name)

print(f"Hello, {name}! Your name has been written to {filename}.")
#10-5
# 10-5. Guest Book

filename = 'guest_book.txt'

print("Enter 'quit' at any time to stop.\n")

while True:
    name = input("Please enter your name: ")
    if name.lower() == 'quit':
        break

    print(f"Welcome, {name}!")
    with open(filename, 'a') as file_object:  # 'a' appends new entries
        file_object.write(name + "\n")

print(f"\nAll guests have been recorded in {filename}.")
with open(filename) as file_object:
    print("\nCurrent Guest Book Entries:")
    print(file_object.read())
#10-6
print("Give me two numbers, and I'll add them together.")

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
except ValueError:
    print("Oops! That’s not a valid number. Please enter numeric values only.")
else:
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}.")
#10-7
print("Enter two numbers, and I'll add them together.")
print("Type 'q' at any time to quit.\n")

while True:
    num1 = input("First number: ")
    if num1.lower() == 'q':
        break

    num2 = input("Second number: ")
    if num2.lower() == 'q':
        break

    try:
        result = int(num1) + int(num2)
    except ValueError:
        print("❌ Please enter valid numbers!\n")
    else:
        print(f"The sum of {num1} and {num2} is {result}\n")
#10-8
Whiskers
Luna
Shadow
Buddy
Charlie
Daisy
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print(f"Sorry, the file '{filename}' was not found.")
    else:
        print(f"\nContents of {filename}:")
        print(contents.strip())
#10-9
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass  # fail silently
    else:
        print(f"\nContents of {filename}:")
        print(contents.strip())
#10-10
def count_word(filename, word):
    """Count how many times a word appears in a text file."""
    try:
        with open(filename, encoding='utf-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print(f"File {filename} not found.")
    else:
        # Count both raw and more specific occurrences
        count = contents.lower().count(word)
        count_with_space = contents.lower().count(word + " ")
        print(f"\nIn '{filename}':")
        print(f"  '{word}' appears about {count} times.")
        print(f"  '{word} ' (with space) appears about {count_with_space} times.")

# Example: analyze multiple texts
filenames = ['alice.txt', 'sherlock.txt', 'mobydick.txt']
for file in filenames:
    count_word(file, 'the')
#10-11
import json

filename = 'favorite_number.json'

favorite_number = input("What's your favorite number? ")

with open(filename, 'w') as f:
    json.dump(favorite_number, f)

print(f"Thanks! I’ll remember that your favorite number is {favorite_number}.")
import json

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    print("I don’t know your favorite number yet!")
else:
    print(f"I know your favorite number! It’s {favorite_number}.")
#10-12
import json

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    favorite_number = input("What’s your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    print("Got it! I’ll remember that.")
else:
    print(f"I know your favorite number! It’s {favorite_number}.")
#10-13
import json

filename = 'user_info.json'

# Collect user data
name = input("What is your name? ")
age = input("How old are you? ")
city = input("What city do you live in? ")

user_data = {
    'name': name,
    'age': age,
    'city': city
}

# Save dictionary as JSON
with open(filename, 'w') as f:
    json.dump(user_data, f)

print("\nUser information saved!")

# Read it back and print summary
with open(filename) as f:
    stored_data = json.load(f)

print(f"\nHere’s what I remember about you:")
print(f"Name: {stored_data['name']}")
print(f"Age: {stored_data['age']}")
print(f"City: {stored_data['city']}")
#10-14
import json

filename = 'username.json'

def get_stored_username():
    """Get stored username if available."""
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username and store it."""
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        correct = input(f"Are you {username}? (y/n): ")
        if correct.lower() == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We’ll remember you next time, {username}!")
    else:
        username = get_new_username()
        print(f"We’ll remember you next time, {username}!")

greet_user()
