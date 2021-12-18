
# write a inheritance using vehicle and car
# class Vehicle:
#     speed = 60
#     passenger = 2
#     fuel_type = "petrol"
#
#
#     def go(self):
#         print("vehicle is going")
#
#     def stop(self):
#         print("vehicle is stoped")
#
#     def changedirection(self):
#         print("taking direction")
#
# class Car(Vehicle):
#     model_type = "KIA Seltos"
#     doors = 5
#     automaker = "KIA India"
#
#     def radio(self):
#         print("no audio available")
#         super().stop()
#
#     def windshieldwiper(self):
#         print("only works while raining")
#
#     def changedirection(self):
#         print("taking 2nd right direction")
#
#
# a = Car()
# a.changedirection()
# a.radio()
########################################################################################################################


# class Product:
#
#
#     def __init__(self, name, price, discountpercent):
#         self.name = name
#         self.price = price
#         self.discountpercent = discountpercent
#
#     def discountamount(self):
#         print("10% discount")
#
#     def getdicountprice(self):
#         print("100 rs discount")
#
#     def description(self):
#         print("thanks for bying our product")
# class Book(Product):
#
#     def __init__(self, author):
#         self.author = author

#     def description(self):
#         print("thanks for bying baahubali new book")
#
# class Movie(Product):
#
#     def __init__(self, year):
#         self.year = year
#
#     def description(self):
#         print("interval")
#
# obj = Book("Krushik")
# obj1 = Movie(2017)
# obj.description()
