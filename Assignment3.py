3-1 

freinds = ["Prince", "Hunter", "Paul", "Rico"]
print(freinds[0])
print(freinds[1])
print(freinds[2])
print(freinds[3])

#3-2

print(f"what's up, {freinds[0]}")
print(f"what's up, {freinds[1]}")
print(f"what's up, {freinds[2]}")
print(f"what's up, {freinds[3]}")

#3-3

cars = ["BMW", "Honda" , "Dodge Ram"]
print(f"I would love to own a {cars[0]}")
print(f"I need to get a {cars[1]}")
print(f"My dream car is a {cars[2]}")

#3-4
invites = ["Ray Lewis" , "Shakespeare" , "Kobe Bryant"]
print(f"{invites[0]}, You are invited to my at home dinner")
print(f"{invites[1]}, You are invited to my at home dinner")
print(f"{invites[2]}, You are invited to my at home dinner")

#3-5

invites[1] = "Michael Jordan"
print(f"{invites[1]}, You are invited to my at home dinner")
print(f"{invites[0]}, You are invited to my at home dinner")
print(f"{invites[2]}, You are invited to my at home dinner")

#3-6 

print("Hey everyone, I found a bigger dinner table, so more people can come!")
invites.insert(3, "Lebron James")
invites.insert(4, "Stephen Curry")
invites.insert(5, "Kevin Durant")
print(f"{invites[0]}, You are invited to my at home dinner")
print(f"{invites[1]}, You are invited to my at home dinner")
print(f"{invites[2]}, You are invited to my at home dinner")
print(f"{invites[3]}, You are invited to my at home dinner")
print(f"{invites[4]}, You are invited to my at home dinner")
print(f"{invites[5]}, You are invited to my at home dinner")

#3-7
print("Hey everyone, the new dinner table won't be ready in time, so I can only invite two people for dinner.")
invites.pop(0)
invites.pop(1)
invites.pop(2)
print(f"{invites[0]}, You are still invited to the at home dinner")
print(f"{invites[1]}, You are still invited to the at home dinner")
print(f"{invites[2]}, You are still invited to the at home dinner")
del invites[2]
del invites[1]
print(invites)

#3-8

places = ["Japan", "Italy", "Greece", "Spain", "France"]
print(places)
print(sorted(places))
print(places)
print(sorted)
print(places)
places.reverse()
print(places)

#3-9

print(len(invites))

#3-10

cities = ["Baltimore", "New York", "Miami"]
print(cities[0])
print(cities[1])
print(cities[2])
cities.pop(0)

#3-11 I had fewer items then i was trying to pop and tried to access and it was not there.