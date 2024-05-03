from datetime import datetime
from typing import List, Dict

# Base Class
class Person:
    def __init__(self, name: str, age: int, date_of_birth: str, passport_details: str):
        self.name = name
        self.age = age
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
        self.passport_details = passport_details

# Employee Class and its Subclasses
class Employee(Person):
    def __init__(self, name: str, age: int, date_of_birth: str, passport_details: str,
                 employee_id: str, department: str, job_title: str, basic_salary: float):
        super().__init__(name, age, date_of_birth, passport_details)
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary

class SalesManager(Employee):
    pass

class Salesperson(Employee):
    pass

class MarketingManager(Employee):
    pass

class Marketer(Employee):
    pass

class Accountant(Employee):
    pass

class Designer(Employee):
    pass

class Handyman(Employee):
    pass

# Client Class
class Client(Person):
    def __init__(self, name: str, age: int, date_of_birth: str, passport_details: str,
                 client_id: str, address: str, contact_details: str, budget: float):
        super().__init__(name, age, date_of_birth, passport_details)
        self.client_id = client_id
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

# Guest Class
class Guest(Person):
    def __init__(self, name: str, age: int, date_of_birth: str, passport_details: str,
                 guest_id: str, address: str, contact_details: str):
        super().__init__(name, age, date_of_birth, passport_details)
        self.guest_id = guest_id
        self.address = address
        self.contact_details = contact_details

# Supplier Class
class Supplier:
    def __init__(self, supplier_id: str, name: str, service_type: str, contact_details: str):
        self.supplier_id = supplier_id
        self.name = name
        self.service_type = service_type
        self.contact_details = contact_details

# Event Class
class Event:
    def __init__(self, event_id: str, type: str, theme: str, date: str, time: str,
                 duration: float, venue_address: str, client_id: str, guest_list: List[Guest],
                 suppliers: List[Supplier], invoice: str):
        self.event_id = event_id
        self.type = type
        self.theme = theme
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.time = time
        self.duration = duration
        self.venue_address = venue_address
        self.client_id = client_id
        self.guest_list = guest_list
        self.suppliers = suppliers
        self.invoice = invoice

# Venue Class
class Venue:
    def __init__(self, venue_id: str, name: str, address: str, contact: str, min_guests: int, max_guests: int):
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests

# Test Cases
if __name__ == "__main__":
    # Create some people
    alice = Client("Alice Johnson", 34, "1986-04-12", "P1234567", "C100", "1234 Park Ave", "alice@example.com", 15000.0)
    bob = Guest("Bob Smith", 29, "1991-07-23", "G7654321", "G200", "5678 Elm Street", "bob@example.com")
    catering = Supplier("S300", "Delicious Catering", "Catering", "contact@deliciouscatering.com")

    # Create an event
    guest_list = [bob]
    suppliers = [catering]
    event = Event("E400", "Wedding", "Classic", "2022-09-15", "15:00", 5.0, "1234 Park Ave", alice.client_id, guest_list, suppliers, "Inv1000")

    # Print details to showcase functionality
    print(f"Event {event.event_id} organized by {alice.name} includes guests like {bob.name} and services from {catering.name}.")
