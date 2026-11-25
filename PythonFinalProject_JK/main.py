import classes

shop = classes.Shop()

def add_customer():
    last_name = str(input("Last Name? "))
    phone_number = str(input("Phone Number? "))
    shop.add_customer(last_name, phone_number)

def find_customer():
    customer_id = int(input("Customer ID? "))
    shop.find_customer(customer_id)

def find_customer_rentals():
    customer_id = int(input("Customer ID? "))
    shop.find_rentals_for_customers(customer_id)

def find_open_rentals():
    for Rental in shop.rental_list:
        if Rental.IsClosed == False:
            Rental.display()

def new_rental():
    customer_id = int(input("Customer ID? "))
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
    Exit = "n"
    while Exit == "N" or Exit == "n":
        print("Add new customer? (A)")
        print("Get customer info? (B)")
        print("Get customer rentals? (C)")
        print("Get open rentals? (D)")
        print("Make new rental? (E)")
        print("Return rental? (F)")
        print("Current inventory? (G)")
        print("Aggregate statistics. (H)")
        choice = str(input(""))
        if choice == "A" or choice == "a":
            add_customer()
        elif choice == "B" or choice == "b":
            find_customer()
        elif choice == "C" or choice == "c":
            find_customer_rentals()
        elif choice == "D" or choice == "d":
            find_open_rentals()
        elif choice == "E" or choice == "e":
            new_rental()
        elif choice == "F" or choice == "f":
            close_rental()
        elif choice == "G" or choice == "g":
            see_inventory()
        elif choice == "H" or choice == "h":
            see_statistics()
        valid = False
        while valid == False:
            Exit = input("Exit? (Y/N): ")
            if Exit != "y" and Exit != "Y" and Exit != "n" and Exit != "N":
                print("Invalid Answer")
                valid = False
            else:
                valid = True

DEBUG = True
if DEBUG == True:
    shop.add_customer("Kristoff", 5036792076)
    shop.add_customer("Jackson", 9638023194)
    shop.add_customer("Maryam", 6420760014)

application()
