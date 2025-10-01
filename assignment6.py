#6-1
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}

print("First Name:", person['first_name'])
print("Last Name:", person['last_name'])
print("Age:", person['age'])
print("City:", person['city'])
#6-2
favorite_numbers = {
    'Alice': 7,
    'Bob': 42,
    'Charlie': 3,
    'Diana': 13,
    'Evan': 27
}

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")
#6-3
glossary = {
    'variable': 'A container for storing data values.',
    'loop': 'A control structure used to repeat a block of code.',
    'function': 'A block of code which only runs when it is called.',
    'list': 'A collection which is ordered and changeable.',
    'dictionary': 'A collection of key-value pairs.'
}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n  {meaning}\n")
#6-4
glossary = {
    'variable': 'A container for storing data values.',
    'loop': 'A control structure used to repeat a block of code.',
    'function': 'A block of code which only runs when it is called.',
    'list': 'A collection which is ordered and changeable.',
    'dictionary': 'A collection of key-value pairs.',
    'tuple': 'An immutable (unchangeable) ordered collection.',
    'boolean': 'A data type with only two values: True or False.',
    'class': 'A blueprint for creating objects.',
    'module': 'A file containing Python code (functions, variables, etc.) that can be imported.',
    'exception': 'An error detected during execution.'
}

for term, definition in glossary.items():
    print(f"{term.title()}:\n  {definition}\n")
#6-5
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'danube': 'germany'
}

# Print sentences about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nCountries:")
for country in rivers.values():
    print(f"- {country.title()}")
#6-6
favorite_languages = {
    'alice': 'python',
    'bob': 'java',
    'carol': 'c++',
    'dave': 'javascript'
}

# People to poll
people_to_poll = ['alice', 'bob', 'eve', 'frank', 'carol']

# Polling check
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for taking the poll.")
    else:
        print(f"{person.title()}, please take our favorite languages poll!")
#6-7
person1 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}

person2 = {
    'first_name': 'Jane',
    'last_name': 'Smith',
    'age': 25,
    'city': 'Los Angeles'
}

person3 = {
    'first_name': 'Mike',
    'last_name': 'Brown',
    'age': 40,
    'city': 'Chicago'
}

people = [person1, person2, person3]

for person in people:
    print(f"\nName: {person['first_name']} {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
#6-8
pet1 = {'animal': 'dog', 'owner': 'Alice'}
pet2 = {'animal': 'cat', 'owner': 'Bob'}
pet3 = {'animal': 'parrot', 'owner': 'Carol'}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"\nAnimal: {pet['animal'].title()}")
    print(f"Owner: {pet['owner'].title()}")
#6-9
favorite_places = {
    'alice': ['Paris', 'New York', 'Tokyo'],
    'bob': ['Sydney'],
    'carol': ['Rome', 'Barcelona']
}

for person, places in favorite_places.items():
    print(f"\n{person.title()}'s favorite places:")
    for place in places:
        print(f" - {place}")
#6-10
favorite_numbers = {
    'alice': [7, 14],
    'bob': [3, 9, 27],
    'carol': [5],
    'dave': [2, 4, 6],
    'eve': [42]
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f" - {number}")
#6-11
cities = {
    'paris': {
        'country': 'France',
        'population': 2148000,
        'fact': 'Known as the City of Light.'
    },
    'tokyo': {
        'country': 'Japan',
        'population': 13960000,
        'fact': 'The world’s most populous metropolitan area.'
    },
    'new york': {
        'country': 'USA',
        'population': 8419000,
        'fact': 'Home to the Statue of Liberty.'
    }
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f" Country: {info['country']}")
    print(f" Population: {info['population']}")
    print(f" Fact: {info['fact']}")
#6-12
cities = {
    'paris': {
        'country': 'France',
        'population': 2148000,
        'fact': 'Known as the City of Light.',
        'famous_food': 'Croissants',
        'is_capital': True
    },
    'tokyo': {
        'country': 'Japan',
        'population': 13960000,
        'fact': 'The world’s most populous metropolitan area.',
        'famous_food': 'Sushi',
        'is_capital': True
    },
    'new york': {
        'country': 'USA',
        'population': 8419000,
        'fact': 'Home to the Statue of Liberty.',
        'famous_food': 'Pizza',
        'is_capital': False
    }
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    for key, value in info.items():
        print(f" {key.replace('_', ' ').title()}: {value}")