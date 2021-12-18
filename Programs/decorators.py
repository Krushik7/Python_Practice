# write a decorator to print function name before executing the function
# def log(func):
#     def wrapper(*args, **kwargs):
#         print(func.__name__)
#         res = func(*args, **kwargs)
#         return res
#     return wrapper
#
# @log
# def add(a, b):
#     return a + b
# print(add(1, b=2))

# OR

# class logging:
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print(func.__name__)
#             res = func(*args, **kwargs)
#             return res
#
#         return wrapper
#
# @logging()
# def add(a, b):
#     return a + b
# print(add(1, b=2))


########################################################################################################################
# to count the number of functions
# d = {}
# def log(func):
#     def wrapper(x, y):
#         f_name = func.__name__
#         if f_name not in d:
#             d[f_name] = 1
#         else:
#             d[f_name] += 1
#         res = func(x, y)
#         return res
#     return wrapper
# @log
# def add(a, b):
#     return a + b
#
# @log
# def sub(a, b):
#     return a - b
#
# print(add(5, 5))
# print(add(5, 5))
# print(sub(6, 5))
# print(d)

# using default dict
# from collections import defaultdict
#
# dd = defaultdict(int)
#
# def log(func):
#     def wrapper(*args, **kwargs):
#         f_name = func.__name__
#         dd[f_name] += 1
#         res = func(*args, **kwargs)
#         return res
#     return wrapper
#
# @log
# def add(a, b):
#     return a + b
#
# @log
# def sub(a, b):
#     return a - b
#
# print(add(5, 5))
# print(add(5, 5))
# print(sub(6, 5))
# print(dd)

# OR

# from collections import defaultdict
# class Logging:
#     dd = defaultdict(int)
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             f_name = func.__name__
#             self.dd[f_name] += 1
#             res = func(*args, **kwargs)
#             return res
#
#         return wrapper
#
# @Logging()
# def add(a, b):
#     return a + b
#
# @Logging()
# def sub(a, b):
#     return a - b
#
# print(add(5, 5))
# print(add(5, 5))
# print(sub(6, 5))
# print(Logging.dd)

########################################################################################################################
#  wa decorator function to convert any number into postive number(imp for exp)
#
# def log(func):
#     def wrapper(*args):
#         res = func(*args)
#         return abs(res)
#     return wrapper
# @log
# def add(a, b):
#     return a + b
# print(add(5, 8))
#
# @log
# def sub(a, b):
#     return a - b
# print(sub(5, 8))

# OR

# class logging:
#     def __call__(self, func):
#         def wrapper(*args):
#             res = func(*args)
#             return abs(res)
#
#         return wrapper
#
# @logging()
# def add(a, b):
#     return a + b
#
# print(add(5, 8))
#
# @logging()
# def sub(a, b):
#     return a - b
#
# print(sub(5, 8))

########################################################################################################################
# wa decorator function which executes the function for n number of times
# def n_times(n):
#     def repeat(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 res = func(*args, **kwargs)
#                 print(res)
#         return wrapper
#     return repeat
# @n_times(3)
# def add(a, b):
#     return a + b
#
# @n_times(2)
# def sub(a, b):
#     return a - b
#
# add(2, 3)
# sub(5, 3)

# OR
# class Ntimes:
#
#     def __init__(self, n):
#         self.n = n
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             for _ in range(self.n):
#                 res = func(*args, **kwargs)
#                 print(res)
#         return wrapper

# @Ntimes(3)
# def add(a, b):
#     return a + b
#
# @Ntimes(2)
# def sub(a, b):
#     return a - b
#
# add(2, 3)
# sub(5, 3)

########################################################################################################################
# using time delay while executing the function
import time

# def delay(n):
#     def log(func):
#         def wrapper(*args, **kwargs):
#             time.sleep(n)
#             res = func(*args, **kwargs)
#             return res
#         return wrapper
#     return log
#
# @delay(5)
# def add(a , b):
#     return a + b
# @delay(1)
# def sub(a, b):
#     return a - b
#
# print(add(2, 5))
# print(sub(5, 2))

# OR

import time

# class Delay:
#
#     def __init__(self, n):
#         self.n = n
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             time.sleep(self.n)
#             res = func(*args, **kwargs)
#             return res
#         return wrapper

#
# @Delay(5)
# def add(a, b):
#     return a + b
# @Delay(3)
# def sub(a, b):
#     return a - b
#
# print(add(2, 5))
# print(sub(5, 2))

########################################################################################################################
# print the time delay between between starting and ending execution of function
import time
#
# def log(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         print(res)
#         end = time.time()
#         print(end-start)
#     return wrapper
# @log
# def add(a, b):
#     return a + b
#
# @log
# def mul(a, b):
#     return a * b

# add(2, 5)
# mul(2, 4)
########################################################################################################################
# write a decorator to validate the type of arguments given to the main function with the user input data type(assignment)
# def type(*types):
#     def data(func):
#         def wrapper(*args, **kwargs):
#             for value, type_ in zip(args, types):
#                 if isinstance(value, type_):
#                     print(f"{value} is the type {type_}")
#                 else:
#                     print(f"{value} is not type{type_}")
#             func(*args, **kwargs)
#
#         return wrapper
#     return data
#
# @type(int, int)
# def add(a, b):
#     return a + b
# add(1, 5)

########################################################################################################################
# wa decorator to reverse the string

# def reverse(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return res[::-1]
#     return wrapper
#
# @reverse
# def rev(a):
#     return a
#
# print(rev("abcd"))

# OR
# class Reverse:
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             return res[::-1]
#         return wrapper
#
# @Reverse()
# def rev(a):
#     return a
#
# print(rev("abcd"))

########################################################################################################################
# wa decorator that counts the number of arguments given to main functions

# def argss(func):
#     def wrapper(*args):
#
#         num = len(args)
#         print("no of args", num)
#         res = func(*args)
#         return res
#
#     return wrapper
#
# @argss
# def add(a, b, c):
#     return a + b + c
# print(add(1, 2, 3))

# OR
# class Arguments:
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#
#             num = len(args) + len(kwargs)
#             print("no of args", num)
#             res = func(*args, **kwargs)
#             return res
#
#         return wrapper
#
# @Arguments()
# def add(a, b, c):
#     return a + b + c
# print(add(1, 2, 3))

########################################################################################################################
# wa decorator function which checks, if the parameters are of integer data type

# def type_(func):
#     def wrapper(*args, **kwargs):
#         for i in args:
#             if not isinstance(i, int):
#                 break
#             else:
#                 print("args are integer")
#
#                 res = func(*args, **kwargs)
#                 return res
#     return wrapper
# @type_
# def add(a, b):
#     return a + b
# #
# print(add(2, 2))

# OR
# class Integer:
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             for i in args:
#                 if not isinstance(i, int):
#                     break
#             else:
#                 print("args are integer")
#
#                 res = func(*args, **kwargs)
#                 return res
#         return wrapper
# @Integer()
# def add(a, b):
#     return a + b
#
# print(add(2, 2))

########################################################################################################################
## PARAMETERISED DECORATOR(imp for exp)

# print a decorator to call main function with user input number of times(imp)
# def n_times(n):
#     def f_name(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 print(func(*args, **kwargs))
#         return wrapper
#     return f_name
#
#
# @n_times(10) # === f_name
# def add(a, b):
#     return a + b
#
# @n_times(5)
# def spam():
#     return "hello"
#
# add(2, 5)
# spam()

# OR
# class Ntimes:

    # def __init__(self, n):
    #     self.n = n
    #
    # def __call__(self, func):
    #     def wrapper(*args, **kwargs):
    #         for _ in range(self.n):
    #             print(func(*args, **kwargs))
    #     return wrapper

# @Ntimes(10) # === f_name
# def add(a, b):
#     return a + b

# @Ntimes(5)
# def spam():
#     return "hello"

# add(2, 5)
# spam()
########################################################################################################################

