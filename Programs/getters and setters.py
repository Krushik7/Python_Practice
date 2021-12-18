# create a class student and declare variables s_name, phy_marks, che_marks, and bio_marks

# class Student:
#
#     def __init__(self, s_name, phy_marks, che_marks, bio_marks):
#         self.s_name = s_name
#         self.__phy_marks = phy_marks
#         self.__che_marks = che_marks
#         self.__bio_marks = bio_marks
#
#     @property
#     def physics(self):
#         return self.__phy_marks
#
#     @property
#     def chemistry(self):
#         return self.__che_marks
#
#     @property
#     def biology(self):
#         return self.__bio_marks
#
#     def percentage(self):
#         print("phy :", self.__phy_marks)
#         print("che :", self.__che_marks)
#         print("bio :", self.__bio_marks)
#
#         res = self.__phy_marks + self.__che_marks + self.__bio_marks
#         print("total percentage is :", (res/300) * 100)
#
#     @physics.setter
#     def physics(self, a):
#         raise TypeError("phy marks cannot be changed")
#
#     @chemistry.setter
#     def chemistry(self, b):
#         raise TypeError("che marks cannot be changed")
#
#     @biology.setter
#     def biology(self, c):
#         raise TypeError("bio marks cannot be changed")
#
#
# a = Student("shashi", 45, 65, 85)
# print(a.chemistry)
# a.percentage()
#
# a.chemistry = 55


