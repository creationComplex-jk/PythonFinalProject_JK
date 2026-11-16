class Customer:
    def __init__(self, last_name, customer_id, phone_number):
        self.last_name = last_name
        self.customer_id = customer_id
        self.phone_number = phone_number

    def display(self):
        print(self.last_name, self.customer_id, self.phone_number)


class Rental:
    snowboard_price = 10
    ski_price = 15

    def __init__(self, rental_id, customer_id, skis_rented, snowboards_rented, rental_length):
        self.rental_id = rental_id
        self.customer_id = customer_id
        self.skis_rented = skis_rented
        self.snowboards_rented = snowboards_rented
        self.rental_length = rental_length
        self.total_charge = (ski_price * self.skis_rented * self.rental_length) + (snowboard_price * self.snowboards_rented * self.rental_length)
        self.IsClosed = False

    def display(self):
        print(self, rental_id, self.customer_id, self.skis_rented, self.snowboards_rented, self.rental_length)

class Shop:
    rental_number = 0
    customer_number = 0

    def __init__(self):
        self.skis = 0
        self.snowboards = 0
        self.customer_list = {}
        self.rental_list = {}
        self.total_income = total_income = 0
        self.total_customers = total_customers = 0
        self.total_rentals = total_rentals = 0
        self.setup_inventory(self.skis, self.snowboards)

    def find_customer(self, customer_id):
        for Customer in shop.customer_list:
            if Customer.customer_id == customer_id:
                return Customer
            return None

    def find_rental(self, rental_id):
        for Rental in shop.rental_list:
            if Rental.rental_id == rental_id:
                return Rental
            return None

    def find_rentals_for_customer(self, customer_id):
        customer_rental_list = {}
        for Rental in shop.rental_list:
            if Rental.customer_id == customer_id:
                customer_rental_list.append(Rental)
        return customer_rental_list

    def add_customer(self, last_name, phone_number, customer_list):
        customer_number += 1
        customer_id = customer_number
        customer = Customer(last_name, customer_id, phone_number)
        customer_list.append(customer)
        print(f"Your Customer ID is {customer_id}")

    def new_rental(self, customer_id, skis_rented, snowboards_rented, rental_length, rental_list):
        rental_number += 1
        rental_id = rental_number
        rental = Rental(customer_id, skis_rented, snowboards_rented, rental_length)
        rental_list.append(rental)
        print(f"Your Rental ID is {rental_id}")
        #This should only succeed if there are enough skis and snowboards currently in our inventory to complete the transaction.

    def complete_rental(self, rental):
        if rental.IsClosed == False:
            rental.IsClosed = True
            print(f"Your total charge is {rental.total_charge}")
        else:
            print("That rental is already closed.")
        #Rented skis and snowboards should be returned to inventory.
        #Income from the rental is added to the total income.

    def setup_inventory(self, skis, snowboards):
        skis = 1000
        snowboards = 1000


