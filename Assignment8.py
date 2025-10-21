#8-1
def display_message():
    print("I am learning about functions in this chapter.")

# Call the function
display_message()
#8-2
def favorite_book(title):
    print(f"One of my favorite books is {title}.")

# Call the function with a book title
favorite_book("Alice in Wonderland")
#8-3
def make_shirt(size, message):
    print(f"The shirt size is {size} and it will say: '{message}'")

# Call the function using positional arguments
make_shirt("Medium", "Code is life!")

# Call the function using keyword arguments
make_shirt(message="Keep calm and code on", size="Large")
#8-4
def make_shirt(size="Large", message="I love Python"):
    print(f"The shirt size is {size} and it will say: '{message}'")

# Large shirt with default message
make_shirt()

# Medium shirt with default message
make_shirt(size="Medium")

# Custom size and custom message
make_shirt(size="Small", message="Debugging is fun!")
#8-5
def describe_city(city, country="USA"):
    print(f"{city} is in {country}.")

# Call the function with default country
describe_city("New York")
describe_city("Los Angeles")

# Call the function with a different country
describe_city("Tokyo", country="Japan")
#8-6
def city_country(city, country):
    return f"{city}, {country}"

# Call the function with at least three city-country pairs
print(city_country("Santiago", "Chile"))
print(city_country("Paris", "France"))
print(city_country("Tokyo", "Japan"))
#8-7
def make_album(artist, title, songs=None):
    album = {
        "artist": artist,
        "title": title
    }
    if songs:
        album["songs"] = songs
    return album

# Create three albums
album1 = make_album("Adele", "30")
album2 = make_album("The Beatles", "Abbey Road")
album3 = make_album("Taylor Swift", "1989", songs=13)

# Print each album
print(album1)
print(album2)
print(album3)
#8-8
def make_album(artist, title, songs=None):
    album = {
        "artist": artist,
        "title": title
    }
    if songs:
        album["songs"] = songs
    return album

while True:
    print("\nEnter album details (or type 'quit' to stop):")
    artist = input("Artist name: ")
    if artist.lower() == 'quit':
        break

    title = input("Album title: ")
    if title.lower() == 'quit':
        break

    songs_input = input("Number of songs (press enter to skip): ")
    if songs_input.lower() == 'quit':
        break

    if songs_input:
        album = make_album(artist, title, songs=int(songs_input))
    else:
        album = make_album(artist, title)

    print("\nAlbum info:", album)
#8-9
def show_messages(messages):
    for message in messages:
        print(message)

# List of messages
messages = ["Hello!", "How are you?", "Good luck!", "See you soon!"]

# Call the function
show_messages(messages)
#8-10
def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        msg = messages.pop(0)  # Remove from original list
        print(f"Sending: {msg}")
        sent_messages.append(msg)  # Add to sent list

# Original list
messages = ["Hello!", "How are you?", "Good luck!", "See you soon!"]
sent_messages = []

# Call the function
send_messages(messages, sent_messages)

# Show lists after sending
print("\nOriginal messages list:", messages)
print("Sent messages list:", sent_messages)
#8-11
def send_messages(messages, sent_messages):
    while messages:
        msg = messages.pop(0)
        print(f"Sending: {msg}")
        sent_messages.append(msg)

# Original list
original_messages = ["Hello!", "How are you?", "Good luck!", "See you soon!"]
sent_messages = []

# Send using a copy of the list
send_messages(original_messages[:], sent_messages)

# Show that original list is unchanged
print("\nOriginal messages list (after function):", original_messages)
print("Sent messages list:", sent_messages)
#8-12
def make_sandwich(*items):
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
    print("Your sandwich is ready!\n")

# Call the function with different numbers of items
make_sandwich("turkey", "lettuce", "tomato")
make_sandwich("peanut butter", "jelly")
make_sandwich("grilled chicken", "cheese", "onions", "pickles", "mustard")
#8-13
def build_profile(first, last, **user_info):
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Build your own profile
my_profile = build_profile(
    "John", "Doe",
    age=30,
    location="New York",
    hobby="photography"
)

print(my_profile)
#8-14
def make_car(manufacturer, model, **car_info):
    car = {
        "manufacturer": manufacturer,
        "model": model
    }
    for key, value in car_info.items():
        car[key] = value
    return car

# Call the function with required and optional arguments
car = make_car("subaru", "outback", color="blue", tow_package=True)

print(car)
#8-15
# printing_functions.py

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(f"- {model}")
# printing_models.py

import printing_functions  # Import the entire module

unprinted = ['phone case', 'robot pendant', 'dodecahedron']
completed = []

printing_functions.print_models(unprinted, completed)
printing_functions.show_completed_models(completed)
#8-16
# greetings.py

def greet_user(name):
    print(f"Hello, {name}!")
# main.py

# 1. import module_name
import greetings
greetings.greet_user("Alice")

# 2. from module_name import function_name
from greetings import greet_user
greet_user("Bob")

# 3. from module_name import function_name as fn
from greetings import greet_user as greet
greet("Charlie")

# 4. import module_name as mn
import greetings as gr
gr.greet_user("Diana")

# 5. from module_name import *
from greetings import *
greet_user("Eve")
#8-17
def make_sandwich(*items):
    """Print a summary of the sandwich being made."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {
        "first_name": first,
        "last_name": last
    }
    for key, value in user_info.items():
        profile[key] = value
    return profile
def make_car(manufacturer, model, **car_info):
    """Build a dictionary representing a car."""
    car = {
        "manufacturer": manufacturer,
        "model": model
    }
    car.update(car_info)
    return car
