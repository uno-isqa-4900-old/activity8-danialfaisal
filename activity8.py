import activity8_db
from activity8_business import CustomerInfo


def display_message():
    print("Customer Viewer")
    print()


def viewer():
    customers = activity8_db.get_customer(CustomerInfo)
    customerid = int(input("Enter customer ID: "))
    print()
    if customerid >=101 and customerid <=600:
        customer = customers[customerid-100]
        print(customer.fname, customer.lname)
        if customer.cname == '':
            pass
        else:
            print(customer.cname)
        print(customer.address)
        print(customer.city, ",", customer.state, customer.zipcode)
        print()
    else:
        print("No customer with that ID")
        print()


def main2():
    question = input("Continue (y/n)")
    if question == "n" or question == "N":
        print("Bye!")
    elif question == "y" or question == "Y":
        print()
        viewer()
        main2()
    else:
        print("Invalid Input-Enter either y or n")
        main2()


def main():
    display_message()
    viewer()
    main2()

if __name__ == '__main__':
    main()
