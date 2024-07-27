class Passenger:
    name = "Abdul moiz" # this a class attributes
    age = 20
    salary = 1200000
    language = "python"

    def info (self):
        print(f"""Hello! My name is {self.name} and i an {self.age} years old and\ni love to code in {self.language} language and i earn about {self.salary} from it.....""")

    
    def greet(self):   # we have to give every method self if we used it or not 
        print("Good Morning")

    @staticmethod
    def welcome():
        print("Hello!! Welcome to the coding life of python")

    def __init__(self , name , age , salary , language):
        self.name = name
        self.age = age
        self.salary = salary
        self.language = language

content = Passenger( "moiz" , 23 , 22000000 , "python")
print(content.name.title() , content.language.title() , content.age, content.salary , sep="\n")
content.name = "Abdul wahab" # this is an instance attributes
content.info()
content.greet()
content.welcome()