import classes

shop = classes.Shop()

def loop(value):
    valid = False
    while valid == False:
        print("")
        value = input("Exit? (Y/N): ")
        print("")
        if value != "y" and value != "Y" and value != "n" and value != "N":
            print("Invalid Answer")
            valid = False
        else:
            return value

def add_customer():
    last_name = str(input("Last Name? "))
    phone_number = str(input("Phone Number? "))
    shop.add_customer(last_name, phone_number)

def find_customer():
    customer_id = int(input("Customer ID? "))
    shop.find_customer(customer_id)

def find_customer_rentals():
    customer_id = int(input("Customer ID? "))
    shop.find_rentals_for_customer(customer_id)

def find_open_rentals():
    for Rental in shop.rental_list:
        if Rental.IsClosed == False:
            Rental.display()
            print("")

def new_rental():
    extant_customer = False
    while extant_customer == False:
        customer_id = int(input("Customer ID? "))
        for Customer in shop.customer_list:
                if Customer.customer_id != customer_id:
                    extant_customer = False
                else:
                    extant_customer = True
                    break
        if extant_customer == False:
            print("No customer under that ID.")
    skis_rented = int(input("Skis Rented? "))
    snowboards_rented = int(input("Snowboards Rented? "))
    rental_length = int(input("How many hours?? "))
    shop.new_rental(customer_id, skis_rented, snowboards_rented, rental_length)

def close_rental():
    rental_id = int(input("Rental ID? "))
    shop.complete_rental(rental_id) 

def see_inventory():
    print(f"Skis: {shop.skis}")
    print(f"Snowboards: {shop.snowboards}")

def see_statistics():
    print(f"Total Income: {shop.total_income}")
    print(f"Total Customers: {shop.total_customers}")
    print(f"Total Rentals: {shop.total_rentals}")

def application():
    print("")
    Exit = "n"
    while Exit == "N" or Exit == "n":
        print("Add new customer? (A)")
        print("Get customer info? (B)")
        print("Get customer rentals? (C)")
        print("Get open rentals? (D)")
        print("Open new rental? (E)")
        print("Return rental? (F)")
        print("Current inventory? (G)")
        print("Aggregate statistics. (H)")
        choice = str(input(""))
        if choice == "A" or choice == "a":
            done = "n"
            while done == "n" or done == "N":
                add_customer()
                done = loop(done)    
        elif choice == "B" or choice == "b":
            done = "n"
            while done == "n" or done == "N":
                find_customer()
                done = loop(done)
        elif choice == "C" or choice == "c":
            done = "n"
            while done == "n" or done == "N":
                find_customer_rentals()
                done = loop(done)
        elif choice == "D" or choice == "d":
            done = "n"
            while done == "n" or done == "N":
                find_open_rentals()
                done = loop(done)
        elif choice == "E" or choice == "e":
            done = "n"
            while done == "n" or done == "N":
                new_rental()
                done = loop(done)
        elif choice == "F" or choice == "f":
            done = "n"
            while done == "n" or done == "N":
                close_rental()
                done = loop(done)
        elif choice == "G" or choice == "g":
            done = "n"
            while done == "n" or done == "N":
                see_inventory()
                done = loop(done)
        elif choice == "H" or choice == "h":
            done = "n"
            while done == "n" or done == "N":
                see_statistics()
                done = loop(done)
        print("")
        print("Would you like to exit the program?")
        Exit = loop(Exit)

DEBUG = True
if DEBUG == True:
    shop.testing_demo()

application()
