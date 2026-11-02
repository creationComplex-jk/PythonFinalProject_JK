class Customer:
    def __init__(self, lastname, customer_id, phone_number):
        self.lastname = lastname
        self.customer_id = customer_id
        self.phone_number = phone_number

    def display(self):
        print(self.lastname, self.customer_id, self.phone_number)


class Rental:
    def __init__(self, rental_id, customer_id, skis_rented, snowboards_rented, rental_length):
        self.rental_id = rental_id
        self.customer_id = customer_id
        self.skis_rented = skis_rented
        self.snowboards_rented = snowboards_rented
        self.rental_length = rental_length
        self.IsClosed = False

    def display(self):
        print(self, rental_id, self. customer_id, self.skis_rented, self. snowboards_rented, self.rental_length)



class Shop:
    def __init__(self, skis, snowboards, customer_list, rental_list, total_income, total_customers, total_rentals):
        self.skis = skis
        self.snowboards = snowboards
        self.customer_list = customer_list
        self.rental_list = rental_list
        self.total_income = total_income
        self.total_customers = total_customers
        self.total_rentals = total_rentals

    def find_rental():

    def find_rentals_for_customer():

    def add_customer():

    def new_rental():

    def complete_rental():

    def setup_inventory():

