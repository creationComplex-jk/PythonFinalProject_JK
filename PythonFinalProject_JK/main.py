import classes

shop = classes.Shop()

def add_customer():
    last_name = str(input("Last Name? "))
    phone_number = str(input("Phone Number? "))
    shop.add_customer(last_name, phone_number)
    shop.customer_list.append(customer)

def show_customer():


def application():
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

    elif choice == "C" or choice == "c":

    elif choice == "D" or choice == "d":

    elif choice == "E" or choice == "e":

    elif choice == "F" or choice == "f":
        
    elif choice == "G" or choice == "g":

    elif choice == "H" or choice == "h":


