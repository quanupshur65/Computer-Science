#9-1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant '{self.restaurant_name}' serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"The restaurant '{self.restaurant_name}' is now open!")
        

# Create an instance
restaurant = Restaurant("Pasta Palace", "Italian")

# Print attributes individually
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Call methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
#9-2
# Create three different instances
restaurant1 = Restaurant("Sushi World", "Japanese")
restaurant2 = Restaurant("Burger Haven", "American")
restaurant3 = Restaurant("Curry Corner", "Indian")

# Call describe_restaurant() for each
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
#9-3
class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email

    def describe_user(self):
        print(f"\nUser Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

# Create several user instances
user1 = User("Alice", "Johnson", 28, "New York", "alice@example.com")
user2 = User("Brian", "Smith", 35, "Los Angeles", "brian@example.com")
user3 = User("Clara", "Lee", 22, "Chicago", "clara@example.com")

# Call methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
#9-4
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value

    def describe_restaurant(self):
        print(f"The restaurant '{self.restaurant_name}' serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"The restaurant '{self.restaurant_name}' is now open!")

    def set_number_served(self, number):
        """Set the number of customers served."""
        if number >= 0:
            self.number_served = number
        else:
            print("Number served cannot be negative.")

    def increment_number_served(self, number):
        """Increment the number of customers served by a given amount."""
        if number > 0:
            self.number_served += number
        else:
            print("Increment must be positive.")


# Create an instance of Restaurant
restaurant = Restaurant("Pasta Palace", "Italian")

# Print default number served
print(f"Customers served: {restaurant.number_served}")

# Change the value directly
restaurant.number_served = 50
print(f"Customers served (after direct change): {restaurant.number_served}")

# Use set_number_served()
restaurant.set_number_served(120)
print(f"Customers served (after using set_number_served): {restaurant.number_served}")

# Use increment_number_served()
restaurant.increment_number_served(30)
print(f"Customers served (after increment): {restaurant.number_served}")
#9-5
class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.login_attempts = 0  # Default value

    def describe_user(self):
        print(f"\nUser Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

    def increment_login_attempts(self):
        """Increment login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to 0."""
        self.login_attempts = 0


# Create an instance of User
user = User("Alice", "Johnson", 28, "New York", "alice@example.com")

# Increment login attempts several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print(f"Login attempts: {user.login_attempts}")

# Reset login attempts
user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}")
#9-6
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant '{self.restaurant_name}' serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"The restaurant '{self.restaurant_name}' is now open!")

    def set_number_served(self, number):
        if number >= 0:
            self.number_served = number
        else:
            print("Number served cannot be negative.")

    def increment_number_served(self, number):
        if number > 0:
            self.number_served += number
        else:
            print("Increment must be positive.")


# Subclass for Exercise 9-6
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors  # List of flavors

    def display_flavors(self):
        print(f"\nAvailable ice cream flavors at '{self.restaurant_name}':")
        for flavor in self.flavors:
            print(f"- {flavor}")


# Create an instance and display flavors
ice_cream_stand = IceCreamStand("Sweet Scoops", "Dessert", ["Vanilla", "Chocolate", "Strawberry", "Mint"])
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()
#9-7
class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nUser Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# Subclass for Exercise 9-7
class Admin(User):
    def __init__(self, first_name, last_name, age, location, email):
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can reset passwords"
        ]

    def show_privileges(self):
        print(f"\nAdministrator Privileges for {self.first_name}:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# Create an admin instance and show privileges
admin = Admin("Sophia", "Green", 30, "Seattle", "sophia.admin@example.com")
admin.describe_user()
admin.show_privileges()
#9-8
class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class AdminWithPrivileges(User):
    def __init__(self, first_name, last_name, age, location, email):
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = Privileges()


# Create a new admin and show privileges
admin2 = AdminWithPrivileges("Liam", "Turner", 42, "Boston", "liam.admin@example.com")
admin2.describe_user()
admin2.privileges.show_privileges()
#9-9
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}".title()


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade the battery if it isn’t already 65."""
        if self.battery_size < 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh.")
        else:
            print("Battery is already at maximum capacity.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


# Create an electric car and demonstrate battery upgrade
my_tesla = ElectricCar("Tesla", "Model 3", 2025)
print(f"\n{my_tesla.get_descriptive_name()}")
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# Upgrade and show improved range
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
#9-10
restaurant_module.py
import_restaurant.py
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant '{self.restaurant_name}' serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"The restaurant '{self.restaurant_name}' is now open!")

    def set_number_served(self, number):
        if number >= 0:
            self.number_served = number

    def increment_number_served(self, number):
        if number > 0:
            self.number_served += number
from restaurant_module import Restaurant

# Create an instance to verify import works
my_restaurant = Restaurant("The Food Loft", "Fusion")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
#9-11
user_module.py
import_admin.py
class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}, Age: {self.age}, Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, location, email):
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = Privileges()
from user_module import Admin

# Create an admin instance
admin_user = Admin("Olivia", "Clark", 38, "Denver", "olivia.admin@example.com")
admin_user.describe_user()
admin_user.privileges.show_privileges()
#9-12
user_class.py
admin_privileges.py
import_multiple.py
class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}, Age: {self.age}, Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")
from user_class import User

class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ["can add post", "can delete post", "can ban user"]
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, location, email):
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = Privileges()
from admin_privileges import Admin

# Create and use an Admin instance
super_admin = Admin("Ethan", "Brooks", 45, "Chicago", "ethan.admin@example.com")
super_admin.describe_user()
super_admin.privileges.show_privileges()
