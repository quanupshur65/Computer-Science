#4-1
# List of favorite pizzas
pizzas = ['Pepperoni', 'Margherita', 'BBQ Chicken']

# For loop to print each pizza name
for pizza in pizzas:
    print(f"I like {pizza} pizza.")

# Statement about how much I love pizza
print("I really love pizza!")
#4-2
# List of animals with a common characteristic
animals = ['Dog', 'Cat', 'Rabbit']

# For loop to print a statement about each animal
for animal in animals:
    print(f"A {animal} would make a great pet.")

# Statement about what these animals have in common
print("Any of these animals would make a great pet!")

#4-3
for number in range(1, 21):
    print(number)
    #4-4
    # Creating the list
numbers = list(range(1, 1000001))
#4-4
# Printing the numbers
for number in numbers:
    print(number)
    #4-5
    numbers = list(range(1, 1000001))

# Check the first and last numbers using min() and max()
print("Min:", min(numbers))
print("Max:", max(numbers))

# Sum the numbers
total = sum(numbers)
print("Sum of numbers from 1 to 1 million:", total)
#4-6
for number in range(1, 21, 2):
    print(number)
#4-7
for number in range(3, 31, 3):
    print(number)
#4-8
for number in range(1, 11):
    cube = number ** 3
    print(f"The cube of {number} is {cube}")
#4-9
cubes = [number ** 3 for number in range(1, 11)]
print(cubes)
#4-10
# Let's assume the list from Exercise 4-4 (numbers from 1 to 10)
numbers = list(range(1, 11))

# Print the first three items
print("The first three items in the list are:", numbers[:3])

# Print three items from the middle of the list
middle_start = len(numbers) // 3  # Start around one-third of the list
middle_end = middle_start + 3  # Get three items from there
print("Three items from the middle of the list are:", numbers[middle_start:middle_end])

# Print the last three items
print("The last three items in the list are:", numbers[-3:])
#4-11
# Original list of pizzas
my_pizzas = ['pepperoni', 'margherita', 'hawaiian']

# Make a copy of the list for a friend
friend_pizzas = my_pizzas[:]

# Add a new pizza to the original list
my_pizzas.append('vegetarian')

# Add a different pizza to the friend's list
friend_pizzas.append('bbq chicken')

# Prove that you have two separate lists
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
#4-12
# Example list of foods
foods = ['pizza', 'burger', 'pasta', 'salad', 'sushi']

# Using two for loops to print the list
print("My favorite foods are:")
for food in foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in foods:
    print(food)
    #4-13
    # Step 1: Create a tuple with five basic foods
buffet_menu = ('pizza', 'pasta', 'salad', 'sushi', 'burger')

# Step 2: Use a for loop to print each food offered by the restaurant
print("The restaurant offers the following foods:")
for food in buffet_menu:
    print(food)

# Step 3: Try to modify one of the items (will raise an error)
# Uncommenting the next line will cause an error because tuples are immutable
# buffet_menu[1] = 'tacos'  # This line will raise a TypeError

# Step 4: The restaurant changes its menu. Rewriting the tuple with new foods
buffet_menu = ('pizza', 'steak', 'fries', 'tacos', 'sushi')

# Step 5: Print the updated menu
print("\nThe updated menu is:")
for food in buffet_menu:
    print(food)
    #4-15
    my_pizzas = ['pepperoni', 'margherita', 'hawaiian']
friend_pizzas = my_pizzas[:]

my_pizzas.append('vegetarian')
friend_pizzas.append('bbq chicken')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)