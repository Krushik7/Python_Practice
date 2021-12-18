# WAP TO CHECK GREATEST OF 3 NUMBERS

# a = 10
# b = 20
# c = 2
# if a > b and b > c:
#     print("a is greatest")
# elif b>c:
# #     print("b is greatest")
# else:
#     print("c is greatest")
# # OR
# if a > b:
#     if a > c:
#         print("a is greatest")
#     else:
#         print("c is greatest")
# elif b > c:
#     print("b is greatest")
# else:
#     print("c is greatest")
########################################################################################################################
# WAP TO CHECK WHETHER STRING IS EMPTY OR NOT

# s = "hai"
# if s:
#     print("string is not empty")
# else:
#     print("string is empty")

# OR
# s = ""
# # if bool(s):
# #     print("string is not empty")
# # else:
# #     print("string is empty")
#
# # OR
# print("string is not empty") if bool(s) else print("string is empty")
########################################################################################################################
# WAP TO CHECK WHETHER LIST IS EMPTY OR NOT
# l = []
# if l:
#     print("list is not empty")
# else:
#     print("list is empty")

# OR
# l = []
# # if bool(l):
# #     print("list is not empty")
# # else:
# #     print("list is empty")
#
# # OR
# print("list is not empty") if bool(l) else print("list is empty")
########################################################################################################################
# WAP TO CHECK WHETHER GIVEN CHARACTER IS VOWEL OR NOT

# char = input("input a character")
# # if char. lower() in "aeiou":
# #     print("character is a vowel")
# # else:
# #     print("character is not a vowel")
#
# # OR
# print("character is a vowel")if char. lower() in "aeiou" else print("character is not a vowel")
########################################################################################################################
# WAP TO CHECK WHETHER THE GIVEN VALUE IS A STRING OR NOT

# a = [1, 2, 3]
# if type(a) == str:
#     print("value is a string")
# else:
#     print("value is not a string")

# OR
# if isinstance(a, str):
#     print("value is string")
# else:
#     print("value is not a string")

# OR
# print("value is string")if isinstance(a, str) else print("value is not a string")
########################################################################################################################
# WAP TO CHECK IF THE USER INPUT IS EVEN OR NOT
# a = int(input("enter the number"))
# if a % 2 == 0:
#     print("the number is even")
# else:
#     print("the number is not odd")

# OR

# a = int(input("enter the number"))
# if a % 2 == 0:
#     print(f"the number {a} is even")
# else:
#     print(f"the number {a} is odd")

# OR

# print(f"the number {a} is even")if a % 2 == 0 else print(f"the number {a} is odd")
########################################################################################################################
# WAP TO CHECK WHETHER THE GIVEN STRING IS A PALINDROME OR NOT

# s = input("enter the string")
# # if s[: : -1] == s:
# #     print("the string is palindrome")
# # else:
# #     print("the string is not a palindrome")
#
# # OR
#
# print("the string is palindrome")if s[: : -1] == s else print("the string is not a palindrome")
########################################################################################################################
# WAP TO CHECK WHETHER THE GIVEN INTEGER IS A PALINDROME OR NOT

# s = input("enter the integer")
# if s[: : -1] == s:
#     print("the integer is palindrome")
# else:
#     print("the integer is not a palindrome")

# OR

# print("the string is palindrome")if s[: : -1] == s else print("the string is not a palindrome")
########################################################################################################################
# CHECK WHETHER THE GIVEN YEAR IS A LEAP YEAR OR NOT

# a = int(input("enter the year"))
# if a % 4 == 0 and a % 100 != 0:
#     print("year is a leap year")
# elif a % 400 == 0:
#     print("year is a leap year")
# else:
#     print("year is not a leap year")

# OR

# import calendar
# print(calendar.isleap(2020))
########################################################################################################################
# WAP TO CHECK WHETHER THE GIVEN NUMBER IS PERFECT SQUARE OR NOT

# a = int(input("enter a number"))
# b = round(a ** 0.5)
# if b ** 2 == a:
#     print("number is a perfect square")
# else:
#     print ("number is not a perfect square")

# OR
# print("number is a perfect square")if b ** 2 == a else print ("number is not a perfect square")
########################################################################################################################
# WAP TO CHECK WHETHER THE GIVEN CHARACTER IS A NUMBER OR ALPHABET OR SPECIAL CHARACTER

# a = input("enter the character")
# if "a" <= a <= "z" or "A" <= a <= "Z":
#     print("character is an alphabet")
# elif "0" <= a <= "9":
#     print("character is a number")
# else:
#     print("character is special character")

# OR

# if a.isalpha():
#     print("character is a alphabet")
# elif a.isnumeric():
#     print("character is a number")
# else:
#     print("character is a special character")
########################################################################################################################
# WAP TO CHECK WHETHER THE GIVEN STRING IS STARTING WITH VOWEL OR NOT

# a = input("enter the string")
# if a[0]. lower() in "aeiou":
#     print("string is starting with vowel")
# else:
#     print("string is not starting with a vowel")

# OR

# print("string is starting with vowel")if a[0]. lower() in "aeiou" else print("string is not starting with a vowel")

# OR

# if a.lower().startswith("a") or a.lower().startswith("e") or a.lower().startswith("i") or a.lower().startswith("o") or a.lower().startswith("u"):
#     print("string is starting with vowel")
# else:
#     print("string is not starting with a vowel")
########################################################################################################################
# WAP TO CHECK WHETHER THE GIVEN STRING IS ENDING WITH VOWEL OR NOT

# a = input("enter the string")
# if a[-1]. lower() in "aeiou":
#     print("string is ending with vowel")
# else:
#     print("string is not ending with a vowel")

# OR

# print("string is ending with vowel")if a[0]. lower() in "aeiou" else print("string is not ending with a vowel")

# OR

# if a.lower().endswith("a") or a.lower().endswith("e") or a.lower().endswith("i") or a.lower().endswith("o") or a.lower().endswith("u"):
#     print("string is ending with vowel")
# else:
#     print("string is not ending with a vowel")
########################################################################################################################
# TAKE A LIST [1, 2, 3, 4, 5] AND CHECK IF LIST HAS EVEN NUMBER OF ELEMENTS IN IT

# a = [1, 2, 3, 4, 5, 6]
# if len(a) % 2 == 0:
#     print("the list has even number of elements")
# else:
#     print("the list has odd number of elements")

# OR

# print("the list has even number of elements")if len(a) % 2 == 0 else print("the list has odd number of elements")
########################################################################################################################
# TAKE A NUMBER AND CHECK WHETHER FIRST DIGIT IS EVEN OR NOT

# s = 123
# a = str(s)
# if int(a[0]) % 2 == 0:
#     print("first digit is even")
# else:
#     print("first digit is odd")

# OR

# print("first digit is even")if int(a[0]) % 2 == 0 else print("first digit is odd")
########################################################################################################################
# TAKE A NUMBER AND CHECK WHETHER SECOND LAST DIGIT IS ODD OR NOT

# s = 1234
# a = str(s)
# if int(a[-2]) % 2 != 0:
#     print("second last digit is odd")
# else:
#     print("second last digit is even")

# OR

# print("second last digit is odd")if int(a[-2]) % 2 != 0 else print("second last digit is even")
########################################################################################################################
# WAP TO CREATE A DICTIONARY WITH THE USER INPUT WHERE THE FIRST CHARACTER OF USER INPUT SHOULD BE KEY AND THE WORD SHOULD BE VALUE

# d = {}
# key = input("enter the key")
# d[key[0]] = key
# print(d)


########################################################################################################################
# IN THE BELOW DICTIONARY CHECK WHETHER THE VALUE IS A STRING , IF IT IS A STRING REVERSE IT OR ELSE PRINT THE SAME

# d = {"a" : 'apple', "f" : 'facebook', "c" : 10, "d" : 125}
# key = input("enter a key {a, f, c, d} ")
# value = d[key]
# if isinstance(value, str):
#     print("the value of a key is string and it has been reversed and updated in the dict")
#     d[key] = value[: : -1]
# else:
#     print("value is not a string")
# print(d)
########################################################################################################################
# WAP TO CHECK NUMBER OF KEYS IN A DICTIONARY , IF NUMBER IS EVEN PRINT DICTIONARY AS IT IS OR ELSE ADD A KEY VALUE PAIR AND PRINT DICTIONARY
#
# dict = {"apple" : 1, "mango": 2, "banana" : 25}
# if len(dict) % 2 == 0:
#     print(dict)
# else:
#     dict["dif"] = 35
# print(dict)
########################################################################################################################
# WAP IF IT IS A VOWEL CREATE KEY VALUE PAIR OR ELSE PRINT ITS NOT A VOWEL

# char = input("enter a character")
# if char.lower() in " aeiou ":
#     print(dict([(char, ord(char))]))
# else:
#     print("is not a vowel")
# OR
# print(dict([(char, ord(char))])) if char.lower() in "aeiou" else print("not a vowel")
########################################################################################################################
# WAP TO CHECK CHARACTER IS IN LOWERCASE OR UPPERCASE
#
# ch = (input("enter the character: "))
#
# if "a" <= ch <= "z":
#     print(chr(ord(ch) - 32))
#
# elif "A" <= ch <= "Z":
#     print(chr(ord(ch) + 32))
# else:
#     print("It is not a alphabet")
# OR
# a = input("enter")
# print(a.swapcase())
# OR
# a = input("enter")
# print(a.upper())
# OR
# a = input("enter")
# print(a.lower())
########################################################################################################################
# WAP TO CHECK IF THE ENTERED MARKS IS GREATER THAN 35, PRINT PASS ELSE PRINT FAIL. IF THE MARKS IS ABOVE 60 PRINT FIRST CLASS

# a = int(input("enter the marks"))
# if 35 <= a < 60:
#     print("pass")
# elif a >= 60:
#     print("first class")
# else:
#     print("fail")
########################################################################################################################
# WAP TO PRINT THE STATEMENT HELLO WORLD FOR 5 TIMES

# for i in range(5):
#     print("Hello world")
########################################################################################################################
# WAP TO PRINT THE EVEN NUMBERS FROM 1 - 10

# for i in range(0,11,2):
#     print(i)

# OR

# for i in range(1,11):
#     if i % 2 == 0:
#         print(i)
########################################################################################################################
# WAP TO PRINT THE ODD NUMBERS BETWEEN THE RANGE 20 - 40
# for i in range(20,41):
#     if i % 2 != 0:
#         print(i)
########################################################################################################################
# WAP TO PRINT THE NUMBERS WHICH ARE DIVISIBLE BY 4 IN THE RANGE 1 - 50
# for i in range(50):
#     if i % 4 == 0:
#         print(i)
########################################################################################################################
# WAP TO PRINT THE NUMBERS WHICH ARE DIVISIBLE BY BOTH 4 AND 7

# for i in (range(1,51)):
#     if i % 4 == 0 and i % 7 == 0:
#         print(i)
########################################################################################################################
# WAP TO CHECK WHETHER THE NUMBER GIVEN BY THE USER IS PRIME OR NOT
# n = 5
# flag = 0
# for i in range(2,n):
#     if n % i == 0:
#         flag = 1
#         break
# if flag == 0:
#     print("it is prime")
# else:
#     print("it is not a prime")

# OR

# n = 5
# flag = 0
# for i in range(2,n):
#     if n % i == 0:
#         flag = 1
#         break
#     else:
#         continue
# if flag == 0:
#     print("it is prime")
# else:
#     print("it is not a prime")
 
# OR

# n = 5
# flag = 0
# for i in range(2,n):
#     if n % i == 0:
#         flag = 1
#         break
#     else:
#         pass
# if flag == 0:
#     print("it is prime")
# else:
#     print("it is not a prime")

# OR

# n = 5
# for i in range(2,n):
#     if n % i == 0:
#         print("it is not a prime")
#         break
# else:
#     print("it is a prime")

# OR

# for n in range(2, 50):
#     for i in range(2,n):
#         if n % i == 0:
#
#             break
#
#     else:
#         print(n, end=" ")


########################################################################################################################
# WAP TO PRINT FIRST 10 EVEN NUMBERS

# i = 0
# count = 0
#
# while count < 10:
#     if i % 2 == 0:
#         print(i)
#         count += 1
#
#     i += 1

########################################################################################################################
# WAP TO PRINT FIRST 10 PRIME NUMBERS

# i = 2
# count = 0
#
# while count < 10:
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=" ")
#         count += 1
#
#     i += 1
########################################################################################################################
# WAP TO PRINT STRING CHARACTER AS WELL AS INDEXES
# s = "hello"*0
# for item in range(len(s)):
#     print(item, s[item])

#
# # OR
#
# for item in s:
#     print(s.index(item), end=" ")
#     print(item)
########################################################################################################################
# WAP TO PRINT EVEN AND ODD NUMBERS

# for i in range(0, 21, 2):
#     print(i)
# OR
# for i in range(1, 21, 2):
#     print(i)
# OR
# i = 0
# while i < 21:
#     if i % 2 ==0:
#         pass
#     else:
#         print(i)
#     i +=1
# OR
# i = 0
# while i < 21:
#     if i % 2 ==1:
#         pass
#     else:
#         print(i)
#     i +=1
########################################################################################################################
# WAP TO PRINT PRIME NUMBERS FROM 1 - 30

# for n in range(2, 30):
#     for i in range(2,n):
#         if n % i == 0:
#             break
#
#     else:
#         print(n, end=" ")

# OR

# i = 2
# while i < 31:
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i)
#     i += 1
########################################################################################################################
# WAP TO PRINT NUMBERS FROM -10 TO -1

# for n in range(-10, 0, 1):
#     print(n)
#
# # OR
#
# i = -10
# while i < 0:
#     print(i)
#     i += 1
########################################################################################################################
# WAP TO PRINT NUMBERS FROM 0 TO 4

# for n in range(0, 5, 1):
#     print(n)
#
# # OR
#
# i = 0
# while i < 5:
#     print(i)
#     i += 1

########################################################################################################################
# PRINT NUMBERS FROM 10 TO 1

# for n in range(10, 0, -1):
#     print(n)

# OR

# i = 10
# while i >= 1:
#     print(i)
#     i -= 1
########################################################################################################################
# PRINT NUMBERS FROM 10 TO 0

# for n in range(10, -1, -1):
#     print(n)

# OR

# i = 10
# while i >= 0:
#     print(i)
#     i -= 1
########################################################################################################################
# PRINT NUMBERS FROM 10 TO -1

# for n in range(10, -2, -1):
#     print(n)

# OR

# i = 10
# while i >= -1:
#     print(i)
#     i -= 1
########################################################################################################################
# WAP TO PRINT ALTERNATE NUMBERS FROM 10 - 0

# for n in range(10, -1, -2):
#     print(n)

# OR

# i = 10
# while i >= 0:
#     print(i)
#     i -= 2
########################################################################################################################
# PRINT EVERY ALTERNATE NUMBER STARTING WITH 0
# for n in range(0, 11, 2):
#     print(n)

# OR

# i = 0
# while i < 11:
#     print(i)
#     i += 2
########################################################################################################################
# PRINT STRING 5 TIMES HELLO WORLD

# for n in range(5):
#     print("Hello world")

# OR

# i = 0
# while i < 5:
#     print("Hello world")
#     i += 1
########################################################################################################################
# WAP TO FIND THE SUM OF FIRST 10 EVEN NUMBERS(0 INCLUDED)

# sum = 0
# for n in range(0, 20, 2):
#     sum = sum + n
# print(sum)


# i = 0
# count = 0
# sum = 0
# while count < 10:
#         if i % 2 == 0:
#             sum += i
#             count += 1
#         i +=1
# print(sum)
########################################################################################################################
# ITERATE OVER THE ITERABLE ONLY IF ITERABLE HAS ATLEAST ONE ITEM ELSE ADD A ITEM TO THAT ITERABLE

# s = "hai"
# if len(s) >= 1:
#     for i in s:
#         print(i)
# else:
#     s += 'hello'
#     print(s)

# OR

# l = []
# if l:
#     for i in l:
#         print (i)
# else:
#     l.append('krushik')
#     print(l)

# OR

# s = {1, 2, 3}
# if bool(s):
#     for i in s:
#         print(i)
# else:
#     s.add('hello')
#     print(s)

# OR

# t = ()
# if t:
#     for i in t:
#         print(i)
# else:
#     t += tuple('125')
#     print(t)

# OR

# d = {'a' : 1, 'b' : 2}
# if d:
#     for i in d:
#         print(i, d[i])
# else:
#     d['c'] = 3
#     print(d)

#######################################################################################################################
# WAP TO CONVERT UPPER CASE TO LOWER CASE USING LOOP

# s = "Hai Hello"
# a = ""
# for i in s:
#     if 'A' <= i <= 'Z':
#         a += chr(ord(i) + 32)
#     elif 'a' <= i <= 'z':
#         a += chr(ord(i) - 32)
#     else:
#         a += i
# print(a)
########################################################################################################################
# WAP TO CHECK WHETHER A CHARACTER IS A VOWEL OR NOT AND SWAP ITS CASE IN THE SENTENCE
# I/P = "hAI goOd mornIng"
# O/P = "hai gOod mOrning"

# s = "hAI goOd mornIng"
# out = ''
# for i in s:
#     if i in "AEIOU":
#         out += i.swapcase()
#     elif i in "aeiou":
#         out += i.swapcase()
#     else:
#         out += i
# print(out)

# OR

# s = "hAI goOd mornIng"
# i = 0
# out = ''
# while i < len(s):
#     if s[i] in "AEIOU":
#         out += chr(ord(s[i]) + 32)
#     elif s[i] in "aeiou":
#         out += chr(ord(s[i]) - 32)
#     else:
#         out += s[i]
#     i += 1
# print(out)
########################################################################################################################
# WAP TO PRINT ONLY VOWELS IN A STRING "PYTHON SELENIUM"

# s = "python selenium"
# for i in s:
#     if i in "aeiou":
#         b = i
#         print(b)
########################################################################################################################
# WAP TO PRINT ONLY CONSONANTS IN A STRING "PYTHON SELENIUM"

# s = "python selenium"
# for i in s:
#     if i not in "aeiou":
#         b = i
#         print(b)
########################################################################################################################
# WAP TO PRINT INDEX AS WELL AS ELEMENT OF AN ITERABLE

# a = "hello"
# for item in range(len(a)):
#     print(item, a[item])

# OR

# for item in enumerate(a):
#     print(item[0], item[1])

# OR

# for index, item in enumerate(a):
#     print(index, item)
########################################################################################################################
# WAP TO PRINT ONLY THE VOWELS IN THE STRING ALONG WITH THEIR INDICES

a = "hello"
# for i in range(len(a)):
#     if a[i].lower() in "aeiou":
#         print(a, a[i])

# for index, item in enumerate(a):
#     if item in "aeiouAEIOU":
#         print(index, item)
########################################################################################################################
# WAP TO PRINT KEYS IN DICTIONARY

# d = {'a' : "apple", 'b' : "ball" }
# for key in d:
#     print(key)

# OR

# for key in d.keys():
#     print(key)

# OR

# for key, value in d.items():
#     print(key)
########################################################################################################################
# WAP TO PRINT ONLY VALUES IN DICTIONARY

# d = {'a' : "apple", 'b' : "ball" }

# for key in d:
#     print(d[key])

# OR

# for value in d.values():
#     print(value)

# OR

# for key, value in d.items():
#     print(value)
########################################################################################################################
# WAP TO INDEX A DICTIONARY

# d = {'a' : "apple", 'b' : "ball" }
# # list(enumerate(d))
# # print(d)
#
# list(enumerate(d.items()))
# print(d)
########################################################################################################################
# CREATE A DICTIONARY TO GET INDEX AND VALUE PRINTED
# s = "hello"
# d = {}
# for index, item in enumerate(s):
#     d[index] = item
# print(d)

# OR

# for item in range(len(s)):
#     d[item] = s[item]
# print(d)

# OR

# d = dict(enumerate(s))
# print(d)
########################################################################################################################
# WAP TO CREATE A LIST OF ELEMENTS RAISED TO THE POWER OF THEIR INDICES

# l = [12, 3, 4, 5, 8]
# res = []
# for index, item in enumerate(l):
#     a = item ** index
#     res.append(a)
#
# print(res)

# OR

# for i in range(len(l)):
#     c = i ** l[i]
#     res.append(c)
# print(c)
########################################################################################################################
# WAP TO CREATE A DICTIONARY OF CHAR AND ITS COUNT PAIR
# s = "hello"
# d = {}
# for index, item in enumerate(s):
#     c = s.count(item)
#     d[item] = c
# print(d)

# OR

# for i in range(len(s)):
#     c = s.count(s[i])
#     d[s[i]] = c
# print(d)
########################################################################################################################
# WAP TP PRINT VOWELS IN GIVEN STRING STRING = 'Python is awesome'
# s = "python is awesome"
# for i in s:
#     if i in "aeiouAEIOU":
#         b = i
#         print(b)
# OR

# i = 0
# while i < len(s):
#     if s[i] in 'aeiouAEIOU':
#         print(s[i])
#     i += 1
########################################################################################################################
# WAP TO PRINT ONLY THE NUMBERS IN THE STRING
# s = 'Sony123pvt45ltd76'
# for i in s:
#     if i.isnumeric():
#         print(i)

# OR

# i= 0
# while i < len(s):
#     if s[i].isnumeric():
#         print(s[i])
#     i += 1
########################################################################################################################
# WAP TO ADD ALL THE NUMBERS FROM THE STRING

# s = 'Sony123pvt45ltd76'
# total = 0
# for i in s:
#     if i.isnumeric():
#         total = total + int(i)

# print(total)

# OR

# i = 0
# sum = 0
# while i < len(s):
#     if s[i].isnumeric():
#         sum += int(s[i])
#     i += 1
# print(sum)
########################################################################################################################
# WAP TO COUNT THE NUMBER OF DIGITS IN A STRING

# s = 'Sony123pvt45ltd76'
# count = 0
# for i in s:
#     if i.isnumeric():
#         count += 1
# print(count)

# OR
# i = 0
# count = 0
# while i < len(s):
#     if s[i].isnumeric():
#         count += 1
#     i += 1
# print(count)
########################################################################################################################
# PRINT [(h, B), (a, y), (i, e)]

# s1 = 'hai'
# s2 = 'Bye'
# print(list(zip(s1, s2)))

# OR

# for index, item in zip(s1, s2):
#     print(index, item)
########################################################################################################################
# WAP TO PRINT CORRESPONDING VOWELS IN A GIVEN STRING

# s1 = 'hai world'
# s2 = 'Bye hello'
# for index, item in zip(s1, s2):
#     if index in "aeiouAEIOU" or item in "aeiouAEIOU":
#         print(index, item)
########################################################################################################################
# WAP TO PRINT THE INDEX AS WELL AS CHARACTER IN GIVEN STRING ONLY IF A CHARACTER IS PRESENT IN ODD INDICES

# s = "hello world"
# for index, item in enumerate(s):
#     if index % 2 != 0:
#         print(index, item)
########################################################################################################################
# WAP TO PRINT EACH CHARACTER IN A STRING IN REVERSE ORDER

# s = "hai"
# for i in reversed(s):
#     print(i)

# OR

# for i in s[: : -1]:
#     print(i)

# OR

# i = len(s) - 1
# while i >= 0:
#     print(s[i])
#     i += -1
########################################################################################################################
# WAP TP PRINT ITEM AND CORRESPONDING INDEX IN THE GIVEN LIST

# l = ['apple', 'google', 'flipkart', 'walmart', 'amazon']

# for index, item in enumerate(l):
#     print(index, item)
########################################################################################################################
# WAP TO PRINT THE ELEMENT AND ITS CORRESPONDING INDEX ONLY IF THE ELEMENT HAS EVEN LENGTH

# l = ['apple', 'google', 'flipkart', 'walmart', 'amazon']

# for index, item in enumerate(l):
#     if len(item) % 2 == 0:
#         print(index, item)
########################################################################################################################
# WAP TO PRINT THE ELEMENTS WHICH ARE STARTING WITH VOWELS
# l = ['apple', 'google', 'flipkart', 'walmart', 'amazon']
# for index, item in enumerate(l):
#     if item[0] in "aeiouAEIOU":
#         print(index, item)

# OR

# for i in l:
#     if i[0] in "aeiouAEIOU":
#         print(i)
########################################################################################################################
# WAP TO PRINT ONLY THE PALINDROMES FROM THE LIST

# l = ['apple', 'google', 'dad', 'mom', 'amazon']

# for i in l:
#     if i[: : -1] == i:
#         print(i)


########################################################################################################################
# WAP TO CREATE A LIST OF ELEMENTS SUCH THAT IF THE ELEMENT IS OF EVEN LENGTH STORE IT AS IT IS , IF IT IS NOT THEN REVERSE IT AND STORE IT

# l = ['apple', 'google', 'dad', 'mom', 'amazon']
# a = []
# for i in l:
#     if len(l) % 2 == 0:
#         a.append(i)
#     else:
#         a.append(i[::-1])
# print(a)
########################################################################################################################
# WAP TO PRINT ONLY THE INTEGER IN THE GIVEN LIST

# l = ["apple", 10, "flipkart", 20, "Amazon"]
# for i in l:
#     if isinstance(i, int):
#         print(i)
########################################################################################################################
# WAP TO PRINT THE VALUES OTHER THAN STRING IN THE GIVEN LIST

# l = ["apple", 10, "flipkart", 20, "Amazon", 3.2]
# for i in l:
#     if not(isinstance(i, str)):
#         print(i)
########################################################################################################################
# WAP TO PRINT ONLY THE EXTENSIONS IN THE GIVEN LIST

# l =["facebook.com", "gmail.text", "yahoo.pdf"]
# for i in l:
#     a = i.split('.')
#     print(a[-1])

########################################################################################################################
# WAP TO BUILD LIST OF TUPLES WITH ELEMENT AND ITS LENGTH AS PAIR
# l = ["facebook", "twitter"]
# res = []
# for i in l:
#     res.append((i, len(i)))
# print(res)
########################################################################################################################
# WAP TO CREATE LIST OF TUPLES OF THE FIRST CHARACTER AND ITS WORD PAIR

# l = ["amazon", "flipkart", "walmart", "google", "gmail", "yahoo"]
# res = []
# for i in l:
#     res.append((i[0], i))
# print(res)
########################################################################################################################
# WAP TO PRINT INDEX AND ITEM OF THE DICTIONARY
# d = {"apple" : 0}
# for index, (key, val) in enumerate(d.items()):
#     print(key, val, index)
########################################################################################################################
# WAP TO CREATE A DICTIONARY USING TWO LISTS WHERE FIRST LIST SHOULD BE THE KEY AND ELEMENTS OF SECOND LIST SHOULD BE THE VALUE

# l1 = ['a', 'b','c']
# l2 = [1, 2, 3]
# d = {}
# c = zip(l1, l2)
# di = dict(c)
# print(di)
########################################################################################################################
# WAP TO FLIP KEY AND VALUE IN A DICTIONARY

# d = {'a' : 1, 'b' : 2, 'c' : 3}
# d1 = {}
# for key, value in d.items():
#     d1[value] = key
# print(d1)
########################################################################################################################
# WAP TO CREATE A DICTIONARY OF CHARACTER AND ITS COUNT PAIR    WITHOUT USING INBUILT METHOD(VVIP QUESTION)
# a = "haii"
# d = {}
# for char in a:
#     if char not in d:
#         d[char] = 1
#     else:
#         d[char] += 1
# print(d)

# OR

# for char in d:
#     d[char] = a.count(char)
# print(d)
# OR

# from collections import defaultdict
# d = defaultdict(int)
# for char  in a:
#     d[char] += 1
########################################################################################################################
# WAP TO COUNT THE VOWELS IN THE STRING AND CREATE A DICTIONARY OF VOWEL AND ITS COUNT PAIR

# s = "hai"
# d = {}
# for item in s:
#     if item in "aeiouAEIOU":
#         if item not in d:
#             d[item] = 1
#         else:
#             d[item] = 1
# print(d)

# OR

# d = {}
# for item in s:
#     if item.lower() in "aeiou":
#         d[item] = s.count(item)
# print(d)

# OR

# from collections import defaultdict
# d = defaultdict(int)
#
# for item in a:
#     if item.lower() in 'aeiou':
#         d[item] += 1
# print(d)
########################################################################################################################
# WAP TO CREATE A DICTIONARY WITH WORD AND ITS COUNT PAIR
# s = 'Python is a Programming language'
# d = {}
# a = s.split()
# for word in a:
#     if word not in d:
#         d[word] = 1
#     else:
#         d[word] += 1
# print(d)

# OR

# for word in a:
#     d[word] = a.count(word)
# print(d)

# OR

# from collections import defaultdict
# d = defaultdict(int)
# for word in a:
#     d[word] += 1
# print(d)
########################################################################################################################
# WAP TO PRINT THE BELOW OUTPUT
# o/p{'P': ['Python', 'Programming'], 'i': ['is'], 'a': ['a'], 'l': ['language']}
# s = 'Python is a Programming language'
# lis =  s.split()
# d = {}
# for word in list:
#     if word[0] not in d:
#         d[word[0]] = [word]
#     else:
#         d[word[0]] += [word]
# print(d)

# OR

# from collections import defaultdict
# dd = defaultdict(list)
# for word in lis:
#     dd[word[0]] += [word]
# print(dd)
########################################################################################################################
# WAP TO CREATE A LIST OF SQUARES FROM THE GIVEN LIST

# l =[1, 2, 3, 4]
# res = []
# for item in l:
#     res.append(item ** 2)

# OR

# res = [(item ** 2) for item in l]
# print(res)
########################################################################################################################
# WAP TO CREATE LIST OF EVEN NUMBERS FROM 1 TO 50
# evens = []
# for i in range(1, 50):
#     if i % 2 == 0:
#         evens.append(i)
# print(evens)

# OR

# evens = [i for i in range(1, 50) if i % 2 == 0 ]
# print(evens)
########################################################################################################################
# WAP TO CREATE A LIST OF WORDS STARTING WITH VOWEL

# s = "hello world how are you"
# l = []
# a = s.split()
# for i in a:
#     if i[0].lower() in "aeiou":
#         l.append(i)
# print(l)

# OR

# vowel = [i for i in a if i[0].lower() in "aeiou"]
# print(vowel)
########################################################################################################################
# WAP TO CREATE A LIST OF WORDS WITH EVEN LENGTH

# s = "hi hello world how are you"
# l = []
# a = s.split()
# for i in a:
#     if len(i) % 2 == 0:
#         l.append(i)
# print(l)

# OR

# evens = [i for i in a if len(i) % 2 == 0]
# print(evens)
########################################################################################################################
# WAP TO FILTER ALL THE LANGUAGES STARTING WITH P
# lang = ['python', 'java' ,'perl', 'php', 'python', 'js', 'c++']
# l = []
# for i in lang:
#     if i[0] == 'p':
#         l.append(i)
# print(l)

# OR

# start = [i for i in lang if i[0] == 'p']
# print(start)

# start = {i for i in lang if i[0] == 'p'}
# print(start)
########################################################################################################################
# WAP TO CREATE A LIST OF WORDS IF THE WORD IS OF EVEN LENGTH STORE IT AS IT IS ELSE REVERSE AND STORE IT

# s = "hi hello world how are you"
# l = []
# a = s.split()
# for i in a:
#     if len(i) % 2 == 0:
#         l.append(i)
#     else:
#         l.append(i[: : -1])
#
# print(l)

# OR

# rev = [i if len(i) % 2 == 0 else (i[: : -1]) for i in a]
# print(rev)
########################################################################################################################
# WAP TO CREATE LIST OF TUPLES OF WORD AND ITS LENGTH PAIR ONLY IF THE WORDS ARE OF ODD LENGTH
# s = "hello world"
# a = s.split()
# l = []
# for i in a:
#     if len(i) % 2 != 0:
#         l.append((i , len(i)))
# print(l)

# OR

# tup = [(i , len(i)) for i in a if len(i) % 2 != 0]
# print(tup)
########################################################################################################################
# CREATE A DICTIONARY OF WORD AS ITS LENGTH PAIR
s ="hai hello how are you"
# dict = {}
# a = s.split()
# for i in a:
#     dict[i] = len(i)
# print(dict)

# OR

dd = {i : len(i) for i in a}
print(dd)
########################################################################################################################
# WAP TO CREATE A DICTIONARY OF CHARACTER AND ITS COUNT
# s ="hai hello how are you hai"
# d = {}
# for i in s:
#     d[i] = s.count(i)
# print(d)

# OR
# for i in s:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)

# OR

# ch = {i : s.count(i) for i in s}
# print(ch)
########################################################################################################################
# WAP TO CREATE A DICTIONARY OF CHAR AND ITS ASCII VALUE PAIR
# s ="hai hello how are you hai"
# d = {}
# for i in s:
#     d[i] = ord(i)
# print(d)

# OR

# Asc = {i :ord(i) for i in s}
# print(Asc)
########################################################################################################################
# WAP TO CREATE A DICTIONARY USING BELOW TWO LISTS

# a = ['hai', 'hello', 'how', 'are', 'you']
# b = [1, 2, 3, 4, 5]
# d = {}
# d = dict(zip(a, b))
# print(d)

# OR

# for i, j in zip(a, b):
#     d[i] = j
# print(d)

# OR

# dd = {i : j for i, j in zip(a, b)}
# print(dd)
########################################################################################################################
# WAP TO CREATE A DICTIONARY WITH WORD AS KEY IF THE WORD IS OF EVEN LENGTH USE THE SAME WORD AS VALUE ELSE REVERSE THE WORD AND STORE ITA S VALUE

# s = "hi hello world how are you"
# d = {}
# a = s.split()
# for i in a:
#     if len(i) % 2 == 0:
#         d[i] = i
#     else:
#         d[i] = i[: : -1]
# print(d)



# rev = {i : i if len(i) % 2 == 0 else (i[: : -1]) for i in a}
# print(rev)
########################################################################################################################
# WAP TO REVERSE INTEGER AND STRING AS IT IS

# d = {'apple': 12, 'cat': "what"}
# res = {}
# for x, y in d. items():
#     if isinstance (y, int):
#         s = str(y)
#         res[x] = s[: : -1]
#     else:
#         res[x] = y
# print(res)

# OR
# rev = {x : y if isinstance (y, str) else str(y)[: : -1] for x, y in d. items()}
# print(rev)
########################################################################################################################
# WAP TO ADD THE ITEMS OF TWO LISTS

# a = [1, 2, 3]
# b = [3, 5, 7]
# c = []
# for i, j in zip(a, b):
#     c.append(zip(a, b))
# print(c)

# ad = [i + j for i, j in zip(a, b)]
# print(ad)
########################################################################################################################
# WRITE A LIST COMPREHENSION TO PRINT FACTORIAL OF EACH NUMBER GIVEN IN THE LIST

# n = 5
# fact = 1
# for num in range(1, n +1):
#     fact *= num
# print(fact)

# OR

# l = [1, 2, 3]
# res = []
# for n in l:
#     fact = 1
#     for num in range(1, n+1):
#         fact *= num
#     res.append(fact)
# print(res)

# OR

# from math import factorial
# res = [factorial(n) for n in l]
# print(res)
########################################################################################################################
# WAP TO FLATTEN THE LIST

# l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# res = []
# for i in l:
#     for j in i:
#         res.append(j)
# print(res)

# OR

# res1 = [j for i in l for j in i ]
# print(res1)
########################################################################################################################
# *
# * *
# * * *
# * * * *

# for i in range(1, 5):
#     print("* " * i)
########################################################################################################################
# * * * *
# * * *
# * *
# *
# for i in range(4, 0, -1):
#     print("* " * i)
########################################################################################################################

#       *
#     * *
#   * * *
# * * * *
# for i in range(1, 5):
#     print(f'{"* " * i :>10}')
########################################################################################################################
      #     *
      #   *   *
      #  *  *  *
      # *  *  *  *
# for i in range(1, 5):
#     print(f'{"* " * i :^10}')
########################################################################################################################
# * * * *
#  * * *
#   * *
#    *

# for i in range(4, 0, -1):
#     print(f'{"* " * i :^8}')
# ########################################################################################################################
# 1
# 1 2
# 1 2 3
# 1 2 3 4

#         1
#      1  2
#  1   2  3
# 1 2  3  4

# pat = ""
# for i in range(1, 5):
#     pat += str(i) + " "
#     print(f'{pat :>10}')

# pat = ""
# for i in range(1, 5):
#     pat += str(i) + " "
#     print(pat)
########################################################################################################################
# a
# a b
# a b c
# a b c d
# a b c d e

# pat = ""
# for i in range(ord('a'), ord('e')+ 1):
#     pat += chr(i) + " "
#     print(pat)

# OR

# pat = ""
# for i in range(5):
#     x = ord("a") + i
#     pat += chr(x) + " "
#     print(pat)

# OR
# pat = ""
# for i in range(4, -1, -1):
#     for j in range(i + 1):
#         x = ord("a") + j
#         print(chr(x), end=" ")
#     print()
########################################################################################################################
# *
# *
# *
# * *
# *
# * * *
# *
# * * * *
# for i in range(1, 5):
#     print("*")
#     print("* " * i)
########################################################################################################################

