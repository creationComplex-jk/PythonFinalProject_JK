import classes

shop = classes.Shop()

def add_customer():
    customer_id = int(print(classes.Customer.customer_id))
    classes.Customer.customer_id += 1
    last_name = str(input("last Name? "))
    phone_number = str(input("Phone Number? "))
    customer = classes.Customer(last_name, customer_id, phone_number)
    shop.customer_list.append(customer)

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


