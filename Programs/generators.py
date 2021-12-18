# WRITE A GENERATOR EXPRESSION TO EXTRACT THE NAMES STARTING WITH VOWEL

# l = ['krushik', 'nikhil', 'sj']
# lis = [i for i in l if i[0] in 'aeiouAEIOU' ]
# print(list(l))
########################################################################################################################
#w a genaerator expression to extract the names which as even len
# s = ['nikhil', 'vidya', 'apple']
# l = (i for i in s if len(i) % 2 == 0)
# print(list(l))
# OR

# def even_(s):
#     for i in s:
#         if len(s) % 2 == 0:
#             yield i
#
# res = even_(s)
# print(list(res))
########################################################################################################################
# wa generator expression to create a list of names ending with vowel
# def end_(s):
#     for i in s:
#         if i[-1] in "aeiouAEIOU":
#             yield i
#
# res = end_(s)
# print(next(res))
#
# OR
#
# l = (i for i in s if i[0] in "aeiouAEIOU")
# print(list(l))
########################################################################################################################
#wa generator exprestion of word and its length pair
# s = ['rat', 'cat', 'apple']
# l = ((i,len(i)) for i in s)
# print(list(l))
#
#
# def pair(s):
#     for i in s:
#         yield (i, len(i))
#
#
# res = pair(s)
# print(list(next(res)))
# print(list(next(res)))
# print(list(next(res)))
########################################################################################################################
# WRITE A GENERATOR TO PRINT THE NUMBERS FROM 10 TO 1

# def count_():
#     for i in range(10, 0, -1):
#         yield i
#
# res = count_()
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
########################################################################################################################
# WRITE A GENERATOR EXPRESSION TO YIELD EVEN NUMBERS FROM 1 TO 50

# def count_():
#     for i in range(0, 50):
#         if i % 2 == 0:
#             yield i
#
# res = count_()
# print(next(res))

########################################################################################################################
# WRITE A GENERATOR EXPRESSION TO YIELD ONE LINE AT A TIME FROM THE FILE


# f_path = r"C:\Users\hp\PycharmProjects\Python_Practice\files\samp.txt"
# def read_line(f_path):
#     with open(f_path) as f:
#         for line in f:
#             yield line
#
# res = read_line(f_path)
# print(list(res))
########################################################################################################################
########################################################################################################################

# WRITE A PROGRAM TO CHECK WHETHER THE NUMBER IS PRIME OR NOT

# n = 11
# l = []
#
# for i in range(2, n):
#     if n % i != 0:
#         l.append(True)
#     else:
#         l.append(False)
#
# print(l)
# print(all(l))
# print(any(l))

# OR comprehension

# res = [True if n % i != 0 else False for i in range(2, n)]
# print(all(res))

# OR generator expression

# res = (True if n % i != 0 else False for i in range(2, n))
# print(all(list(res)))
########################################################################################################################
# WRITE A GENERATOR FUNCTION AND GENERATOR EXPRESSION FOR PRIME AND RETURN SQUARES
# generator function
# def prime_():
#     for num in range(1, 10):
#         if num > 1 and all([num % i != 0 for i in range(2, num)]):
#             yield num ** 2
#
#
# print(list(prime_()))

# OR
# generator expression
# gen_ex = (num ** 2 for num in range(1, 10) if num > 1 and all([num % i != 0 for i in range(2, num)]) )
#
# print(list(gen_ex))
########################################################################################################################
#  write a generator expression to extract the names starting with vowel
# list_ = ['mani', "rakesh", "nikhil", "ashwini"]
# l = (i for i in list_ if i[0] in "aeiouAEIOU")
# print(list(l))
########################################################################################################################
# # write a generater prog to extract the names which are of even length
# list_ = ['mani', "rakesh", "nikhil", "ashwini"]
# l = (i for i in list_ if len(i) % 2 == 0)
# print(list(l))
########################################################################################################################
# write a generator expression to create a list of names ending with vowels
# list_ = ['mani', "rakesh", "nikhil", "ashwini"]
# l = (i for i in list_ if i[-1] in "aeiouAEIOU")
# print(list(l))
########################################################################################################################
# write a generator expression to create list of tuple of word and its length pair
# list_ = ['mani', "rakesh", "nikhil", "ashwini"]
# l = ((i, len(i)) for i in list_)

# print(list(l))
########################################################################################################################
# print the numbers from 1 to 10
# res = (i for i in range(10, 0, -1))
# print(next(res))
########################################################################################################################
# even numbers in the range 1 - 50
# res = (i for i in range(0, 51) if i % 2 == 0)
# print(next(res))
########################################################################################################################