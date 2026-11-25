from typing import Self


class Customer:
    def __init__(self, last_name, customer_id, phone_number):
        self.last_name = last_name
        self.customer_id = customer_id
        self.phone_number = phone_number

    def display(self):
        print(f"Last Name: {self.last_name}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Phone Number: {self.phone_number}")


class Rental:
    snowboard_price = 10
    ski_price = 15

    def __init__(self, rental_id, customer_id, skis_rented, snowboards_rented, rental_length):
        self.rental_id = rental_id
        self.customer_id = customer_id
        self.skis_rented = skis_rented
        self.snowboards_rented = snowboards_rented
        self.rental_length = rental_length
        self.total_charge = (self.ski_price * self.skis_rented * self.rental_length) + (self.snowboard_price * self.snowboards_rented * self.rental_length)
        self.IsClosed = False

    def display(self):
        print(f"Rental ID: {self.rental_id}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Skis_Rented: {self.skis_rented}")
        print(f"Snowboards Rented: {self.snowboards_rented}")
        print(f"Rent Time: {self.rental_length}")

class Shop:
    rental_number = 0
    customer_number = 0
    skis = 0
    snowboards = 0
    skis = 0
    snowboards = 0
    customer_list = []
    rental_list = []
    total_income = 0
    total_customers = 0
    total_rentals = 0

    def __init__(self):
        self.setup_inventory(self.skis, self.snowboards)

    def find_customer(self, customer_id):
        for Customer in self.customer_list:
            if Customer.customer_id == customer_id:
                Customer.display()
                print("")

    def find_rental(self, rental_id):
        for Rental in self.rental_list:
            if Rental.rental_id == rental_id:
                return Rental
            return None

    def find_rentals_for_customer(self, customer_id):
        customer_rental_list = {}
        for Rental in self.rental_list:
            if Rental.customer_id == customer_id:
                customer_rental_list.append(Rental)
            for Rental in customer_rental_list:
                Rental.display()
                print("")

    def add_customer(self, last_name, phone_number):
        self.customer_number += 1
        customer_id = self.customer_number
        customer = Customer(last_name, customer_id, phone_number)
        self.customer_list.append(customer)
        print(f"Your Customer ID is {customer_id}")
        self.total_customers += 1

    def new_rental(self, customer_id, skis_rented, snowboards_rented, rental_length):
        if skis_rented > self.skis or snowboards_rented > self.snowboards:
            print("Not enough inventory.")
        else:
            self.rental_number += 1
            rental_id = self.rental_number
            self.skis -= skis_rented
            self.snowboards -= snowboards_rented
            rental = Rental(rental_id, customer_id, skis_rented, snowboards_rented, rental_length)
            self.rental_list.append(rental)
            print(f"Your Rental ID is {rental_id}")
            self.total_rentals += 1

    def complete_rental(self, rental_id):
        for Rental in self.rental_list:
            if Rental.rental_id == rental_id:
                if Rental.IsClosed == False:
                    Rental.IsClosed = True
                    self.skis += Rental.skis_rented
                    self.snowboards += Rental.snowboards_rented
                    self.total_income += Rental.total_charge
                    print(f"Your total charge is {Rental.total_charge}")
                else:
                    print("That rental is already closed.")
            else:
                print("No such rental exists.")

    def setup_inventory(self, skis, snowboards):
        self.skis = 1000
        self.snowboards = 1000

    def testing_demo(self):
        self.add_customer("Kristoff", 5036792076)
        self.add_customer("1234567890", 0000000000)
        self.add_customer("<>/-|\{}[]()=+", 9999999999)
        self.new_rental(2,500, 1000, 999)
        self.new_rental(1, 250, 0, 0)
        self.new_rental(3, 500, 1, 10)
        self.complete_rental(1)
        self.complete_rental(2)
        self.complete_rental(3)



