#5-1
# Test 1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')  # True because car is 'subaru'

# Test 2
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')  # False because car is 'subaru', not 'audi'

# Test 3
age = 25
print("\nIs age > 20? I predict True.")
print(age > 20)  # True because 25 is greater than 20

# Test 4
print("\nIs age < 18? I predict False.")
print(age < 18)  # False because 25 is not less than 18

# Test 5
number = 10
print("\nIs number == 10? I predict True.")
print(number == 10)  # True because number is 10

# Test 6
print("\nIs number != 10? I predict False.")
print(number != 10)  # False because number is 10, so it’s not unequal to 10

# Test 7
favorite_color = 'blue'
print("\nIs favorite_color == 'blue'? I predict True.")
print(favorite_color == 'blue')  # True because favorite_color is 'blue'

# Test 8
print("\nIs favorite_color == 'red'? I predict False.")
print(favorite_color == 'red')  # False because favorite_color is not 'red'

# Test 9
height = 5.9
print("\nIs height >= 5.5? I predict True.")
print(height >= 5.5)  # True because 5.9 is greater than or equal to 5.5

# Test 10
print("\nIs height <= 5.5? I predict False.")
print(height <= 5.5)  # False because 5.9 is greater than 5.5

#5-2
print("=== Tests for equality and inequality with strings ===")
name = "Alice"
print("Is name == 'Alice'? I predict True.")
print(name == "Alice")  # True
print("Is name != 'Bob'? I predict True.")
print(name != "Bob")  # True
print("Is name == 'Bob'? I predict False.")
print(name == "Bob")  # False
print("Is name != 'Alice'? I predict False.")
print(name != "Alice")  # False

print("\n=== Tests using the lower() method ===")
city = "New York"
print("Is city.lower() == 'new york'? I predict True.")
print(city.lower() == "new york")  # True
print("Is city.lower() == 'los angeles'? I predict False.")
print(city.lower() == "los angeles")  # False

print("\n=== Numerical tests involving equality and inequality ===")
age = 30
print("Is age == 30? I predict True.")
print(age == 30)  # True
print("Is age != 25? I predict True.")
print(age != 25)  # True
print("Is age > 20? I predict True.")
print(age > 20)  # True
print("Is age < 40? I predict True.")
print(age < 40)  # True
print("Is age >= 30? I predict True.")
print(age >= 30)  # True
print("Is age <= 29? I predict False.")
print(age <= 29)  # False

print("\n=== Tests using 'and' keyword ===")
print("Is age > 20 and age < 40? I predict True.")
print(age > 20 and age < 40)  # True
print("Is age > 40 and age < 50? I predict False.")
print(age > 40 and age < 50)  # False

print("\n=== Tests using 'or' keyword ===")
print("Is age < 20 or age == 30? I predict True.")
print(age < 20 or age == 30)  # True
print("Is age < 20 or age > 40? I predict False.")
print(age < 20 or age > 40)  # False

print("\n=== Test whether an item is in a list ===")
fruits = ['apple', 'banana', 'cherry']
print("Is 'banana' in fruits? I predict True.")
print('banana' in fruits)  # True
print("Is 'orange' in fruits? I predict False.")
print('orange' in fruits)  # False

print("\n=== Test whether an item is not in a list ===")
print("Is 'orange' not in fruits? I predict True.")
print('orange' not in fruits)  # True
print("Is 'apple' not in fruits? I predict False.")
print('apple' not in fruits)  # False

#5-3
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")
#5-4
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points for shooting the green alien!")
else:
    print("You just earned 10 points for shooting a non-green alien!")
#5-5
alien_color = 'green'

if alien_color == 'green':
    print("You earned 5 points for shooting a green alien!")
elif alien_color == 'yellow':
    print("You earned 10 points for shooting a yellow alien!")
else:
    print("You earned 15 points for shooting a red alien!")
alien_color = 'yellow'

if alien_color == 'green':
    print("You earned 5 points for shooting a green alien!")
elif alien_color == 'yellow':
    print("You earned 10 points for shooting a yellow alien!")
else:
    print("You earned 15 points for shooting a red alien!")
alien_color = 'red'

if alien_color == 'green':
    print("You earned 5 points for shooting a green alien!")
elif alien_color == 'yellow':
    print("You earned 10 points for shooting a yellow alien!")
else:
    print("You earned 15 points for shooting a red alien!")
#5-6
age = 25  # Change this value to test with different ages

if age < 2:
    print("You are a baby.")
elif age >= 2 and age < 4:
    print("You are a toddler.")
elif age >= 4 and age < 13:
    print("You are a kid.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
elif age >= 20 and age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")
#5-7
favorite_fruits = ['banana', 'apple', 'strawberry']

if 'banana' in favorite_fruits:
    print("You really like bananas!")

if 'apple' in favorite_fruits:
    print("You really like apples!")

if 'strawberry' in favorite_fruits:
    print("You really like strawberries!")

if 'grape' in favorite_fruits:
    print("You really like grapes!")

if 'orange' in favorite_fruits:
    print("You really like oranges!")
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")
requested_toppings = ['mushrooms', 'green peppers', 'pineapple']

for requested_topping in requested_toppings:
    if requested_topping == 'pineapple':
        print(f"Sorry, we're out of {requested_topping} today.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")
#5-8
usernames = ['jaden', 'admin', 'sara', 'john', 'alice']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")
#5-9
usernames = []  # List is empty to simulate the case

if not usernames:
    print("We need to find some users!")
else:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
#5-10
current_users = ['jaden', 'admin', 'sara', 'john', 'alice']

new_users = ['john', 'mike', 'Sara', 'bob', 'Jaden']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please choose a different one.")
    else:
        print(f"The username '{new_user}' is available.")
#5-11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
#5-12
I styled it all appropiately
#5-13
Data exploration, and games