import PersonClass as p

def main(): 

    name = 'John'
    address = '1234 Main St'
    phone_number = '123-456-7890'
    cust_number = 1234
    on_list_flag = False 

    # Create an instance of the Person Class 
    person1 = p.Person(name, address, phone_number)

    # Create an instance of the Customer Class
    customer1 = p.Customer(name, address, phone_number, cust_number, on_list_flag)

    # Display information for the Person
    person1.printperson ()

    print()
    print()
    print()

    #Display information for the Customer 
    customer1.printperson()

main()