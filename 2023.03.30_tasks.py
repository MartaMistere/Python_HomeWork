#-------------TASK 1----------------
#Create a class named Car that has the following attributes: make, model, and year. 
#It should also have a method called get_info() that returns a string with the car's make, model, and year.

#class Car:
 
    #def set_info (self, make, model, year):
        #self.make = make
        #self.model = model
        #self.year = year
    #def get_info(self):
        #print ("Car make is", self.make)
        #print ("Car model is", self.model)
        #print ("Car year is", self.year)
#myCar1 = Car()
#myCar1.set_info("Skoda","Enyaq",2022)
#myCar1.get_info()


#-------------TASK 2----------------
#Create a class named Rectangle that has the following attributes: width and height. 
#It should also have methods called area() and perimeter() that return the area and perimeter of the rectangle, respectively

#class Rectangle:
 
    #def init(self, width, height):
        #self.width = width
        #self.height = height
        
    #def area(self):
        #return self.width*self.height
    #def perimeter(self):
        #return (self.width+self.height)*2
        
#myRectangle = Rectangle(5,7)

#print (f"Rectangle area is {myRectangle.area()}")
#print (f"Rectangle perimeter is {myRectangle.perimeter()}")
        

#-------------TASK 3----------------
#Create a class named BankAccount that has the following attributes: account_number, balance, and owner_name. 
#It should also have methods called deposit() and withdraw() that update the balance accordingly

#class BankAccount:
 
    #def __init__(self, account_number, balance, owner_name) -> None:
        #pass
        #self.account_number = account_number
        #self.balance = balance
        #self.owner_name = owner_name
        
    #def deposit(self):
        #a = int(input("Enter the deposit amount: "))
        #balance1=self.balance + a
        #return balance1
    #def withdraw(self):
        #b = int(input("Enter the withdraw amount: "))
        #balance2=self.balance + b
        #return balance2
        
#myBankAccount = BankAccount("LV55 UNLA 0000 0001", 100, "Marta")
#print(f"The account balance with deposit is {myBankAccount.balance1()}")
#print(f"The account balance with withdraw is {myBankAccount.balance2()}")

#-------------TASK 4----------------
#Create a class named Person that has the following attributes: name, age, and address. 
#It should also have a method called get_info() that returns a string with the person's name, age, and address.

#class Person:
 
    #def set_info (self, name, age, address):
        #self.name = name
        #self.age = age
        #self.address = address
        
    #def get_info(self):
        #print(f"Persons name is {self.name}, person is {self.age} years old, and person lives in {self.address}.")

#myPerson = Person()
#myPerson .set_info("Marta",40,"Riga")
#myPerson .get_info()

#-------------TASK 5----------------
#Create a class named Animal that has the following attributes: name and species. 
#It should also have a method called speak() that returns a string with the animal's sound.

#class Animal:
    #def __init__(self, name, species):
        #self.name = name
        #self.species = species
    #def speak(self, sound):
        #return f"{self.name} species {self.species} says {sound}"
#Animal1=Animal("Dog","Malties")
#Animal2=Animal("Frog","Green")

#print(Animal1.speak("woof, woof"))
#print(Animal2.speak("ribbit, fibbit"))

#-------------TASK 6----------------
#Create a base class named Vehicle that has the following attributes: make, model, and year. It should also have a method called get_info() that returns a string with the vehicle's make, model, and year. 
#Then create two subclasses, Car and Truck, that inherit from Vehicle and add additional attributes and methods specific to each type of vehicle.

class Vehicle:
 
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def get_info(self):
        return f"Car make is {self.make}, this car model is {self.model} and {self.year} year."

class Car(Vehicle):
    def __init__(self, make, model, year, category):
        super().__init__(make, model, year)
        self.category=category
    def get_Car_info(self):
        print(f"Car make is {self.make}, this car model is {self.model}, {self.year} year and it is {self.category}.")

class Truck(Vehicle):
    def __init__(self, make, model, year, wheel_size):
        super().__init__(make, model, year)
        self.wheel_size=wheel_size
    def get_Truck_info(self):
        print(f"Truck make is {self.make}, this truck model is {self.model}, {self.year} year and it has wheel size {self.wheel_size}.")

