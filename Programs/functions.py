# WRITE A FUNCTION TO COUNT THE NUMBER OF POSITIONAL AND KEYWORD ARGUMENTS PASSED TO IT
# def func(*args, **kwargs):
#     return len(args), len(kwargs)
#
#
# print(func(1, 2, 5, c = 3, d = 4))
########################################################################################################################
# WRITE A FUNCTION TO PRINT MESSAGE "HAI EVERYONE" IF THE USER INPUT IS NOT PRESENT

# def greet(name = "hai everyone"):
#     return(f"{name}")
#
#
# print(greet())
########################################################################################################################
# A FUNCTION TAKES VARIABLE NUMBER OF POSITIONAL ARGUMENTS AS INPUT, HOW TO CHECK IF ARGUMENTS THAT ARE PASSED ARE MORE THAN 5

# def func(*args):
#     if len(args) > 5:
#         print("args are > 5")
#     else:
#         print("args are < 5")
#
#
# func(1, 2, 3, 4)
########################################################################################################################
# PRINT NUMBERS FROM 10 TO 1

# count = 10
#
# while count> 0:
#     print(count)
#     count -= 1


# USING RECURSION

# def countdown(count):
#     if not count > 0:
#         return
#
#     print(count)
#     countdown(count - 1)
#
#
# countdown(10)
########################################################################################################################
# WAP TO FIND FACTORIAL OF A NUMBER USING WHILE LOOP

# n = 5
# fact = 1
#
# while n != 0:
#     fact = fact * n
#     n -= 1

# def factorial_(n, fact):
#     if n == 0:
#         return fact
#     fact *= n
#     return factorial_(n-1, fact)
#
#
# print(factorial_(5, 1))
########################################################################################################################
 # WRITE A RECURSION PROGRAM TO CALCULATE THE SUM OF FIRST 10 NUMBERS

# n = 10
# sum = 0
# while n > 0:
#     sum += n
#     n -= 1
# print(sum)

# OR

# def sum_10(n, sum=0):
#
#     if n == 0:
#         return sum
#     sum += n
#     return sum_10(n-1, sum)
#
# print(sum_10(10))
########################################################################################################################
#' WRITE A RECURSION PROGRAM TO REVERSE THE STRING

# s = "hai"
# i = 0
# res = ''
# while i < len(s):
#     res = s[i] + res
#     i += 1
# print(res)

# OR

# def reverse_(s, i=0, res=''):
#     if i == len(s):
#         return res
#
#     res = s[i] + res
#     return reverse_(s, i+1, res)
#
# print(reverse_("hai"))
########################################################################################################################
# WAP TO PRINT 10 FIBONACCI SERIES

# n1 = 0
# n2 = 1
# count = 10
#
# while count > 0:
#     print(n1)
#     temp = n1 + n2
#     n1 = n2
#     n2 = temp
#     count -= 1

# OR

# def fib_(n1=0, n2=1, count=10):
#     if count == 0:
#         return
#     print(n1)
#     temp = n1 + n2
#     n1 = n2
#     n2 = temp
#
#     return fib_(n1, n2, count - 1)
#
# fib_()
########################################################################################################################
# WRITE A RECURSION PROGRAM TO FIND THE  NUMBER OF DIGITS IN A NUMBER

# n= 234
# s = str(n)
# i = 0
# count = 0
# while i < len(s):
#     count += 1
#     i += 1
# print(count)

# OR

# def dig_(n, i=0, count=0):
#     if i > len(str(n)):
#         return count
#     i += 1
#
#     return dig_(n,i, count + 1)
# print(dig_(234))
########################################################################################################################
# WRITE A LAMBDA FUNCTION TO SQUARE ANY NUMBER

# square = lambda a: a**2
# print(square(5))
########################################################################################################################
# WRITE A LAMBDA FUNCTION TO GET LAST ELEMENT OF AN ITERABLE

# ele = lambda a : a[-1]
# print(ele("hai"))
########################################################################################################################
# WRITE A FUNCTION TO GET THE OUTPUT a^2 + b^2 + 2ab

# op = lambda a, b: a ** 2 + b ** 2 + 2 * a * b
# print(op(1,2))
########################################################################################################################
# WRITE A LAMBDA FUNCTION TO CHECK WHETHER THE GIVEN NUMBER IS EVEN OR ODD

# ed = lambda a :"even" if a % 2 == 0 else "odd"
# print(ed(3))
########################################################################################################################
# WRITE A LAMBDA FUNCTION IF THE GIVEN STRING IS PALINDROME OR NOT
# pal = lambda a:"palindrome" if a[: : -1] == a else "not a palindrome"
# print(pal("mom"))
########################################################################################################################
# l = [1, 2, 3, 4]
# res = lambda a : a % 2 == 0
# b = map(res, l)
# print(list(b))
########################################################################################################################
# WAP TO SQUARE AND CUBE EVERY NUMBER IN A GIVEN LIST OF INTEGERS

# l = [1, 2, 3]
# # sq = lambda a : a ** 2
# # res = map(sq, l)
# # print(list(res))
#
# # OR
# cube = lambda a : a ** 3
# res = map(cube, l)
# print(list(res))
########################################################################################################################
# WRITE A PYTHON PROGRAM TO RETURN THE LIST OF ELEMENTS RAISED TO THE POWER OF THEIR INDICES USING MAP
# l = [1, 2, 3]
# pow = lambda a : a[1] ** a[0]
# s = map(pow,enumerate(l))
# print(list(s))
########################################################################################################################
# WRITE A PYTHON PROGRAM TO CONVERT NEGATIVE NUMBERS IN THE GIVEN LIST TO POSITIVE NUMBERS

# l = [-1, -2, -3]
# np = lambda a : abs(a)
# s = map(np, l)
# print(list(s))
########################################################################################################################
# WRITE A MAP FUNCTION TO ADD ELEMENTS IN BOTH THE LIST

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# add = lambda a : a[0] + a[1]
# re = map(add, zip(l1, l2))
# print(list(re))
########################################################################################################################
#hh WAP TO FILTER OUT ONLY EVEN NUMBERS FROM THE LIST

# l = [1, 2, 3]
# odd = lambda a : a % 2 == 0
# res1 = filter(odd, l)
# print(list(res1))
########################################################################################################################
# WAP TO FILTER OUT ONLY ODD NUMBERS FROM THE LIST

# l = [1, 2, 3]
# odd = lambda a : a % 2
# res1 = filter(odd, l)
# print(list(res1))
########################################################################################################################
# BUILD A LIST WITH ONLY EVEN LENGTH STRING USING FILER FUNCTION

# l = ['hai', 'hell']
# eve = lambda a : len(a) % 2 == 0
# res1 = filter(eve, l)
# print(list(res1))

# OR

# print(list(filter(lambda a : len(a) % 2 == 0, l)))
########################################################################################################################
# WAP TO RETURN  THE STRING IF STRING IS STARTING WITH VOWEL

# s = ["hai", "how", "are", "you"]
# ret = lambda a : a[0] in "aeiouAEIOU"
# res = filter(ret, s)
# print(list(res))
########################################################################################################################
# WAP TO EXTRACT ONLY NEGATIVE NUMBERS IN THE LIST
# l = [-1, -2, 3, 4]
# neg = lambda a : a < 0
# res = filter(neg, l)
# print(list(res))
########################################################################################################################
# WAP TO PRINT PRIME NUMBERS FROM 1 -50 USING FILTERS
# def is_prime(n):
#     if n > 1:
#         for i in range(2, n):
#             if n % i == 0:
#                 return 0
#         else:
#             return 1
#
# prime = filter(is_prime, range(50))
# print(list(prime))
########################################################################################################################
# WAP TO CALCULATE THE SUM OF POSITIVE AND NEGATIVE NUMBERS IN THE GIVEN LIST

# l = [-1, -2, 3, 4]
# sum1 = lambda a : a < 0
# sum2 = lambda a : a > 0
#
# res1 = filter(sum1, l)
# res2 = filter(sum2, l)
# print(sum(res1), sum(res2))
########################################################################################################################
# WRITE A FUNCTION TO SEARCH FOR A CHARACTER IN A GIVEN STRING AND RETURN ITS CORRESPONDING INDEX, IF THE CHARACTER IS DUPLICATED RETURN ITS FIRST OCCURENCE INDEX

# s = "hai hello how are you"
# ch = "i"
#
# def index_(string, ch):
#     return (string.index(ch))
#
#
# print(index_(s, ch))

# OR

# s = "hai hello how are you"
# def index_of_char(string, char):
#
#     for index, item in enumerate(string):
#         if item == char:
#             return index
#
# print(index_of_char(s, "z"))

########################################################################################################################
# WAP TO SEARCH FOR A CHARACTER INA A GIVEN STRING AND RETURN THE CORRESPONDING INDEX IF CHARACTER IS DUPLICATED RETURN ALL THE INDICES

# s = "hai hello how are you"
#
#
# def index_of_char(string, char):
#     for index, item in enumerate(string):
#         if item == char:
#             s.index(char)
#             print(index)
#
#
# index_of_char(s, "h")
########################################################################################################################
# WRITE A FUNCTION TON PRINT THE BELOW OUTPUT
# func("TRACXN", 0) #Should print RCN
# func("TRACXN", 1) #Should print TAX

# def func(string, n):
#     if n == 0:
#         return string[1 : : 2]
#     elif n == 1:
#         return string[:: 2]
#
#
# print(func("TRACXN", 0))
# print(func("TRACXN", 1))
########################################################################################################################
# WRITE A FUNCTION THAT RETURNS THE LAST DIGIT OF AN INTEGER

# def func(s):
#     a = str(s)
#     return a[-1]
#
#
# print(func("123"))
########################################################################################################################o
# WAP TO CREATE A LIST OF TUPLES OF THE FIRST CHARACTER AND THE WORDS STARTING WITH IT IN THE GIVEN STRING

# s = "hello good morning"
# l1 = s.split()
# li = []
# for i in l1:
#     li.append((i[0], i))
#
# print(li)
########################################################################################################################o
# CREATE A DICTIONARY OF THE WORD OF ITS LENGTH PAIR

# s = "Python is programming language"
# d = s.split()
# di = {}
# for i in d:
#     di[i] = len(i)
# print(di)
########################################################################################################################
# WAP TO CREATE A LIST OF DUPLICATES VALUE IN THE STRING
# s = "hello good morning"
# l = []
# for i in s:
#     if s.count(i) > 1:
#         l.append(i)
# print(l)
########################################################################################################################
# WAP TO CREATE A LIST OF NON DUPLICATES VALUE IN THE STRING

# s = "hello good morning"
# l = []
# for i in s:
#     if s.count(i) == 1:
#         l.append(i)
# print(l)
########################################################################################################################
# WAP TO CREATE A DICT OF WORD AND CHAR PAIR ONLY IF THE LAST CHARACTER IS A VOWEL

# s = "hai how are you"
# a = s.split()
# d = {}
# for i in a:
#     if i[-1] in "aeiouAEIOU":
#         d[i] = i[-1]
# print(d)
########################################################################################################################
# WAP TO CREATE A LIST TO REMOVE DUPLICATES VALUE IN THE STRING
# it wont work
# s = "hello good morning"
# res = ""
# for i in s:
#     if s.count(i) == 1:
#         res += i
# print(res)

# OR

# for i in s:
#     if i not in res:
#         res += i
# print(res)
########################################################################################################################
# REPLACE A DUPLICATE IN A STRING WITH _
# s = "hello how are you"
# a = " "
# for i in s:
#     if s.count(i) > 1:
#         a = a + '_'
#     else:
#         a += i
# print(a)
########################################################################################################################
# WRITE A FUNCTION TO PRINT THE LENGTH OF ANY ITERABLE WITHOUT USING INBUILT FUNCTION

# def length_(s):
#     count = 0
#     for _ in s:
#         count += 1
#     return count
# print(length_("hai"))
########################################################################################################################
# WAP TO REVERSE A STRING WITHOUT USING ANY INBUILT FUNCTION
# def reve_(s):
#     rev = ""
#     for i in s:
#         rev = i + rev
#     return rev
#
# print(reve_("hai"))
########################################################################################################################
# WAP TO CONVERT A STRING TO A LIST AND VICEVERSA

# s = "hai"
# a = s.split()
# print(" ".join(a))

# OR WITHOUT INBUILT

# def convert_(l,s):
#     for i in l:
#         s += i
#
#     return(s)
# print(convert_(['h', 'e', 'l', 'l', 'o'], ""))

########################################################################################################################
# print(",".join(s)) # string to "," separated string
###################################################################################################################
# wap to creat a dict of char and it ascii values
# s ="hello"
# d = {}
# for i in s:
#     if i not in d:
#         d[i] = ord(i)
# print(d)
# print()
########################################################################################################################
#wa function to convert upercase to lower case string with out using in built function
# def conver_(s):
#     con = ""
#     for i in s:
#         if i not in con:
#             con += chr(ord(i)+32)
#     return con
#
#
# print(conver_("HELLO"))
########################################################################################################################
#wa function to check whether string is palandrome or not
# def pal_(s):
#     rev = ""
#     for i in s:
#             rev = i + rev
#     if rev == s:
#
#         print("palindrome")
#
# pal_("mom")


# OR


# def pal_(s):
#     if s[::-1] == s:
#      return ("palindrome")
#
#
# print(pal_("mom"))
########################################################################################################################
#wap to search for the char & return its coresponding index
# s = "hello"
# ch = "l"
# for index, item in enumerate(s):
#     if ch in item:
#         print(index)
########################################################################################################################
#wa function hich takes list of int , str, if the item is string it should print as it is , if the item is flaot or int it should reverse
# l = ['apple', 'ball', 1234, 100, 123.76, 2 + 3j]
# def rev_(s):
#     for i in s:
#         if isinstance(i, int):
#             print(str(i)[::-1])
#         elif isinstance(i,str):
#             print(i)
#         else:
#             print(str(i)[::-1])
# rev_(l)
########################################################################################################################
# s = 'hai how are you'
# # op1 = "uoy era woh iah"
# # op2 = "iah woh era uoy"
# r2 = []
# a = s.split()
# r = s[::-1]
# for i in a:
#     r2.append(i[::-1])
# print(" ".join(r2))
# print(r)
########################################################################################################################
#wap to reverse a value in dict if the value is string
# d ={"a": "hello", 'b':100, 'c':10.1, 'd': 'world'}
# res = {}
# for i, j in d.items():
#     if isinstance(j,str):
#         res[i] = j[::-1]
#     else:
#         res[i] = j
# print(res)
########################################################################################################################
#wap to count num of words present in a sentence
# s = "hai how are you"
# a = s.split()
# count = 0
# for i in a:
#     count += 1
# print(count)
########################################################################################################################
# op = 1234
# t = ('1','2','3','4')
# l = list(t)
# print(''.join(l))
########################################################################################################################
# s = "hai hello how are u"
# a = sorted(s)
# ''.join(a)
# print(a)
#
# s = {1, 2, 3}
# b = sorted(s)
#
# print(b)
#
#
#
# s = (1, 2, 3)
# a = sorted(s)
# # ''.join(a)
# print(a)
#
# s = {'s' : 1}
# b = sorted(s)
#
# print(b)
########################################################################################################################
