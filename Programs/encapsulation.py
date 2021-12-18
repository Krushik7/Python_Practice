# PUBLIC MEMBER

# class Public:
#     name = "ram"
#
#     def display(self):
#         print("in public display", self.name)
#
# # accessing outside the class
# p = Public()
# print(p.name)
# p.display()
#
# # accessing in child
# class Child(Public):
#
#     def spam(self):
#         print(self.name)
#         self.display()
#
# d = Child()
# print(d.name)
# d.spam()


# PROTECTED MEMBERS
#
# class Protected:
#     _name = "sita"
#
#     def display(self):
#         print("name is ", self._name)

  # accessing outside the class
# p = Protected()
# # print(p.name)   #AttributeError
# print(p._name)
# p.display()

# accessing in the child class

# class Child:
#
#     def spam(self):
#         print(self._name)
#         self._dispaly()
#
# c = Child()
# c.spam()


# PRIVATE MEMBERS

# class Private:
#     __name = "steve"
#
#     def display(self):
#         print("in private class display", self.__name)

# accessing outside the class
# p = Private()
# print(p.name)      #AttributeError
# print(p.__name)    #AttributeError

    # {'_private__name': 'steve', '_private__display': <function private.__display at 0*00}
# print(p._Private__name)
#
# # accessing in child
#
# class Child(Private):
#
#     def spam(self):
#         print(self.__name)
#
# c = Child()
# c.spam()




