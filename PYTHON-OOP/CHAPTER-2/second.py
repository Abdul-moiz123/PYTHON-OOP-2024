# class Empolyee:

#     @staticmethod
#     def info():
#         print("Hello! Welcome to the python coding")

# class Programmar(Empolyee):
    
#     @staticmethod
#     def moiz():
#         print("Hello moiz How are you")

# mo = Programmar()

# mo.info()
# mo.moiz()

###################################

# class Empolyee:

#     @staticmethod
#     def info():
#         print("Hello! Welcome to the python coding")

# class Programmar:
    
#     @staticmethod
#     def moiz():
#         print("Hello moiz How are you")

# class Coder(Empolyee , Programmar):
#     @staticmethod
#     def haseeb():
#         print("Hello my name is abdul haseeb")

# c = Coder()
# c.haseeb()
# c.info()
# c.moiz()

###################################

# class Empolyee:

#     @staticmethod
#     def info():
#         print("Hello! Welcome to the python coding")

# class Programmar(Empolyee):
    
#     @staticmethod
#     def moiz():
#         print("Hello moiz How are you")

# class Coder(Programmar):
#     @staticmethod
#     def haseeb():
#         print("Hello my name is abdul haseeb")

# c = Coder()
# c.haseeb()
# c.info()
# c.moiz()

# p = Programmar()
# p.info()
# p.moiz()

# e = Empolyee()
# e.info()

###################################

# class Empolyee:

#     name = "abdul moiz"

#     def __init__(self):
#         print("The constructor of the Empoiyee")

#     @staticmethod
#     def info():
#         print("Hello! Welcome to the python coding")

# class Programmar(Empolyee):

#     def __init__(self):
#         super().info()
#         print(super().name)
#         print("The constructor of the Programmer")

#     @staticmethod
#     def moiz():
#         print("Hello moiz How are you")

# class Coder(Programmar):

#     def __init__(self):
#         super().__init__()
#         print("The constructor of the Coder")

#     @staticmethod
#     def haseeb():
#         print("Hello my name is abdul haseeb")

# c = Coder()

# p = Programmar()

# e = Empolyee()

###################################

# class Employee:
#     name = "abdul moiz"

#     def info(self):
#         print(f"The name is {self.name}")

# e = Employee()
# e.name = "abdulllah"
# e.info()


# class Employee:
#     name = "abdul moiz"

#     @classmethod
#     def info(cls):
#         print(f"The name is {cls.name}")

# e = Employee()
# e.name = "abdulllah"
# e.info()

###################################

# class Employee:
    # name = "abdul moiz"

    # @classmethod
    # def info(cls):
    #     print(f"The name is {cls.name}")

#     @property 
#     def name(self):
#         return f"{self.fname} {self.lname}" 

#     @name.setter
#     def name(self,value):
#         self.fname = value.split(" ")[0]
#         self.lname = value.split(" ")[1]

# e = Employee()
# e.name = "abdul moiz"
# e.info()

# print(e.fname , e.lname)
# print(e.fname)


###################################

# class Number:

    

#     def __init__(self , n):
#         self.n = n    

#     def __add__(self , num):
#         return self.n + num.n
    
#     def __mul__(self , num):
#         return self.n * num.n

# n = Number(10)        
# m = Number(20) 

# print(n + m)
# print(n * m)

###################################
