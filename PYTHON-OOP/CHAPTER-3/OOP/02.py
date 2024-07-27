# class parent:

#     @staticmethod
#     def info_parent():
#         print("THIS IS THE PARENTS CLASS")

# class grandfather:

#     @staticmethod
#     def info_grandfather():
#         print("THIS IS THE GRAND PARENTS CLASS")

# class child(parent):

#     @staticmethod
#     def info_child():
#         print("THIS IS THE CHILD CLASS")

# my_obj = child()
# my_obj.info_child()
# my_obj.info_parent()

#########################################################

class parent:

    @staticmethod
    def info_parent():
        print("THIS IS THE PARENTS CLASS")

class grandfather:

    @staticmethod
    def info_grandfather():
        print("THIS IS THE GRAND PARENTS CLASS")

class child(parent ,grandfather):

    def __init__(self , name , age):
        super().__init__(name ,age)


    @staticmethod
    def info_child():
        print("THIS IS THE CHILD CLASS")

my_obj = child()
my_obj.info_child()
my_obj.info_grandfather()
my_obj.info_parent()

#################################################