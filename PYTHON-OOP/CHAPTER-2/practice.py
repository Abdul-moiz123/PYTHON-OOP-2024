# class TwoDVector:
#     def __init__(self , i ,j):
#         self.i=i
#         self.j=j

#     def show(self):
#         print(f"The vector is {self.i} and {self.j}")

# class ThreeDVector(TwoDVector):
#     def __init__(self , i ,j , k):
#         super().__init__(i,j)
#         self.k=k

#     def show(self):
#         print(f"The vector is {self.i} and {self.j} and {self.k}")    

# a = TwoDVector(1,2)            
# a.show()
# b = ThreeDVector(1,2,3)            
# b.show()



# class Animal:
#     def bark1(self):
#         print("moiz")

# class Pet(Animal):
#     def bark2(self):
#         print("haseeb")

# class Dog(Pet):
#     @staticmethod
#     def bark3(self):
#         print("bow bow")

# d = Dog()
# d.bark1()
# d.bark2()
# d.bark3()



# class Employee:

#     salray = 2300
#     increment = 20

#     @property
#     def SalaryAfterIncrement(self):
#         return (self.salray + self.salray * (self.increment / 100))

#     @SalaryAfterIncrement.setter
#     def SalaryAfterIncrement(self , salary):
#         self.increment = ((salary/self.salray)-1)*100    

# e = Employee()
# print(e.SalaryAfterIncrement)        
# e.SalaryAfterIncrement = 30
# print(e.increment)



# class Complex:

#     def __init__(self , real , imaginary):
#         self.real = real 
#         self.imaginary = imaginary

#     def __add__(self , c2):
#         return Complex(self.real + c2.real , self.imaginary + c2.imaginary)
        
#     def __str__(self):
#         return f" {self.real} + {self.imaginary}i"   

# c1 =  Complex(1,2)
# c2 =  Complex(2,4)
# print(c1 + c2)

