class My_Class:

    # name = ""
    # age = 0

    def __init__(self , name , age):
        self.name = name
        self.age = age

    def info(self):
        print(f"My name is {self.name} and i am {self.age} years old")

    def __str__(self) -> str:
        return f"{self.name} {self.age}"

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
obj1 = My_Class(user_name , user_age)
obj1.info()

user_age = 20
user_name="rafay"
obj2 = My_Class(user_name , user_age)
obj2.info()
del obj2.age
obj2.info() # give error as you have delete age

print(obj1)


