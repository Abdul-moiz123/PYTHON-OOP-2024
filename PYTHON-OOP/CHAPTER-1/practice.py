import math as ma
# class Programmer:

#     company = "Microsoft"

#     def __init__(self , name , salary , pin_code):
#         self.name = name
#         self.salary = salary
#         self.pin_code = pin_code

#     def info(self):
#         print(f"Hello! my name is {self.name} and my salary is {self.salary} and my pincode is {self.pin_code} and i work in {self.company}")    

# first = Programmer("abdul moiz" , 1200000 , 24001)
# first.info()
        
####

# class Calculator:
#     number = 0

#     def __init__(self , number):
#         self.number = number

#     def square(self) -> int:
#         print(f"The square of the {self.number} is {self.number * self.number}")

#     def cube(self) -> int:
#         print(f"The cube of the {self.number} is {self.number * self.number * self.number}")

#     def square_root(self) -> float:
#         print(f"The square root  of the {self.number} is {float(ma.sqrt(self.number))}")

# number = int(input("ENter the number: "))
# p = Calculator(number)
# p.square()
# p.cube()
# p.square_root()

####

# class Name:
#     a = 5
# o = Name()
# print(o.a)
# o.a= 0
# print(o.a)
# print(Name.a)
# print(o.a)

####

# class Greeting:

#     @staticmethod
#     def Greet():
#         print("Hello! Welcome to the python coding")
# moiz = Greeting()
# moiz.Greet()        


####

# from random import randint

# class Train:

#     def __init__(self , train_no):
#         self.train_no = train_no

#     def Book_Ticket(self , fro , to):
#         print(f"Ticket is book in train number: {self.train_no} from {fro} to {to}")

#     def Train_Status(self , train_no):
#         print(f"Train number: {self.train_no} is running on time")
    
#     def Train_Fare(self , train_no , fro , to):
#         print(f"Train Fare in train number: {self.train_no} from {fro} to {to} is {randint(222,5555)}")

# t = Train(234567)
# t.Book_Ticket("pakistan" , "india")


####

# class Moiz:

#     def __init__(self , name):
#         self.name = name 
    
#     def greet(harry):
#         print(f" Hello ! {harry.name}, How are you?")
# m = Moiz("abdulmoiz")
# m.greet()      