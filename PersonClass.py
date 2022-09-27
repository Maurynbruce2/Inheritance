class Person:
    def __init__(self,persons_name,persons_address,telephone_number):
        self.__name = persons_name
        self.__address = persons_address
        self.__phone = telephone_number


    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def printperson(self):
        print('Name: ', self.__name)
        print('Address: ', self.__address)
        print('Telephone Number: ', self.__phone)


class Customer(Person):
    def __init__(self,persons_name,persons_address,telephone_number,cust_number,on_list):

        Person.__init__(self,persons_name,persons_address,telephone_number)

        self.__cust_number = cust_number 
        self.__on_list = on_list

    def printperson(self):
        Person.printperson(self)

        print('Customer Number: ',self.__cust_number)
        if self.__on_list:
            print('On Mailing List: Yes')

        else:
            print('On Mailing List: No')