#11-1
def city_country(city, country, population=None):
    """Return a string in the format 'City, Country' or 'City, Country - population xxx'."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    return f"{city.title()}, {country.title()}"
#11-2
from city_functions import city_country

def test_city_country():
    """Test the formatting of a simple city/country pair."""
    result = city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'

def test_city_country_population():
    """Test city/country formatting with a population added."""
    result = city_country('santiago', 'chile', 5000000)
    assert result == 'Santiago, Chile - population 5000000'
#11-3
# employee.py

class Employee:
    """A simple representation of an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Add a raise to the annual salary. Default is $5,000."""
        self.annual_salary += amount
#version 1
# test_employee_no_fixture.py
from employee import Employee

def test_give_default_raise():
    emp = Employee("John", "Doe", 50000)
    emp.give_raise()
    assert emp.annual_salary == 55000

def test_give_custom_raise():
    emp = Employee("John", "Doe", 50000)
    emp.give_raise(10000)
    assert emp.annual_salary == 60000
#version 2
# test_employee_with_fixture.py
import pytest
from employee import Employee

@pytest.fixture
def employee():
    """Create an Employee instance for use in tests."""
    return Employee("John", "Doe", 50000)

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.annual_salary == 55000

def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.annual_salary == 60000