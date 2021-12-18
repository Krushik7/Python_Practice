# create a class which can return one element at a time from the list
# or
# create a class which has iteration capability

# names = ["ravi", "prudvi", "shashi", "sathish"]
#
# class Sample:
#
#     def __init__(self, iterable):
#         self.names = iterable
#
#     def __iter__(self):
#         return iter(self.names)
#
# s = Sample(names)
#
# for name in s:
#     print(name)

# create a class which acts as both iterable and iterator
# names = ["ravi", "prudvi", "shashi", "sathish"]
# class Sample:
#     def __init__(self, iterable):
#         self.names = iterable
#         self.iter_ = iter(self.names)
#
#     def __iter__(self):
#         return iter(self.names)
#
#     def __next__(self):
#         try:
#             return next(self.iter_)
#         except StopIteration:
#             print("no elements")
#
# s = Sample(names)
#
# print(next(s))
# print(next(s))


# create a iterator to print the numbers from 10 to 1

# class Numbers:

#     def __init__(self):
#         self.start = 11
#         self.end = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#
#         if self.start > self.end:
#             self.start -= 1
#             return self.start
#         else:
#             raise StopIteration
#
# a = Numbers()
#
# for item in a:
#     print(item)

# create a custom iterator to print numbers from 10 to 1

# class Numbers:
#
#     def __init__(self):
#         self.start = 11
#         self.end = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start > self.end:
#             self.start -= 1
#             return self.start
#         else:
#             raise StopIteration
#
# a = Numbers()
#
# for item in a:
#     print(item)

# createe a custom iterator to print the elements in reversed order

# names = ["ravi", "prudvi", "shashi", "sathish"]
#
# class Reverse:
#
#     def __init__(self, names):
#         self.names = names
#         self.index = len(self.names)-1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#
#         if self.index == -1:
#             raise StopIteration
#         else:
#             x = self.index
#             self.index -= 1
#             return self.names[x]

# a = Reverse(names)
#
# for item in a:
#     print(item)


# create a custom iterator to print squares of the list of given numbers

# l = [1, 2, 3, 4, 5]
#
# class Suares:
#
#
#     def __init__(self, l):
#         self.l = l
#         self.index = 0
#         self.item = len(self.l)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < self.item:
#             res = self.index
#             self.index += 1
#             return self.l[res] ** 2
#         else:
#             raise StopIteration
# a = Suares(l)
#
# for i in a:
#     print(i)


# create a custom iterator to print prime numbers from 1 to 50

# class Prime:
#
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#
#     def __iter__(self):
# #         return self
#
#     def __next__(self):
#
#         if self.start < self.end:
#             x = self.start
#             self.start += 1
#
#             if x > 1:
#                 for i in range(2, x):
#                     if x % i == 0:
#                         break
#                 else:
#                     return x
#
#         else:
#             raise StopIteration
#
# a = Prime(1, 50)
#
# for item in a:
#     if item:
#         print(item)

# CREATE A CUSTOM ITERATOR TO PRINT FIBONACCI SERIES FROM RANGE 1 - 50

# class Fibonacci:
#
#     def __init__(self, first, last):
#         self.first = first
#         self.next = first + 1
#         self.last = last
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         f = self.first
#         if self.first < self.last:
#             temp = self.first + self.next
#             self.first = self.next
#             self.next = temp
#             return f
#         else:
#             raise StopIteration
#
# a = Fibonacci(1, 50)
#
# for item in a:
#     if item:
#         print(item)



















