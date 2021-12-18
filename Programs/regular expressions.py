s = "hello"
import re
# re.findall("hello", s)
#
# s = "hello how are you how are you doing"
# re.findall("how", s)
#
# s = "hello how are you How are you doing"
# re.findall("how", s)
#
# re.findall("how", s, re.IGNORECASE)

print(re.findall(".", "ana"))

print(re.findall("a.", "ana"))

print(re.findall("a..", "ana"))

print(re.findall("a.a", "ana"))

print(re.findall("a.a", "aba"))

print(re.findall(".a", "aba"))

print(re.findall("a.a", "a a"))

print(re.findall("an.a", "anna"))

print(re.findall("an.a", "anba"))

print(re.findall("a.+a", "anna"))

print(re.findall("a.+a", "annna"))

print(re.findall("a.+a", "aa"))

print(re.findall("a.+a", "anba"))

print(re.findall("an+a", "anna"))

print(re.findall("an+a", "annna"))

print(re.findall("an+a", "annba"))

print(re.findall("a+a", "anna"))

print(re.findall("a+a", "aa"))

print(re.findall("a.+a", "aa"))

print(re.findall("a.*a", "aa"))

print(re.findall("a*a", "anna"))

print(re.findall("he*o", "hello"))

print(re.findall("he*o", "heeeo"))

print(re.findall("he*o", "heo"))

print(re.findall("he*o", "ho"))

print(re.findall("he+o", "ho"))

print(re.findall("h*eo", "hello"))

print(re.findall("h*e.*o", "hello"))

print(re.findall("h*eo", "eo"))

print(re.findall("^hello", "hello world"))

print(re.findall("^hello", "world hello"))

print(re.findall("hello$", "hello world"))

print(re.findall("hello$", "world hello"))

print(re.findall("an?a", "anna"))

print(re.findall("an?a", "ana"))

print(re.findall("an?a", "aa"))

print(re.findall("colou?r", "colour"))

print(re.findall("colou?r", "color"))
########################################################################################################################
# WAP TO COUNT THE NUMBER OF VOWELS IN A STRING
# s = "hello world"
# l = (re.findall("[aeiou]", s))
# print(len(l))
########################################################################################################################
# WAP TO MATCH ONLY DIGITS INSIDE STRING
s = "This pen is Rs. 100"
print(re.findall("[0123456789]", s))

print(re.findall("[0123456789]+", s))

print(re.findall("[0-9]+", s))

print(re.findall("\d", s))

print(re.findall("\d+", s))

print(re.findall("\D", s))

print(re.findall("\D+", s))

print(re.findall("\D*", s))
########################################################################################################################
# s = "Hi How are you"
#
# print(re.findall(".*", s))
#
# print(re.findall(".", s))
#
# print(re.findall(".+", s))
#
# print(re.findall("[a-z]+", s))
#
# print(re.findall("[a-zA-Z]+", s))
#
# print(re.findall("[a-zA-Z]+", s))
#
# print(re.findall("[a-zA-Z ]+", s))
#
# print(re.findall("\w+", s))
########################################################################################################################
s = "Hi_How are you"
print(re.findall("\w+", s))

s = "Hi_How are you, It is 3 PM"
print(re.findall("\w+", s))

print(re.findall("\W+", s))
########################################################################################################################
s = "Hi How are you"

print(re.findall(" ", s))

print(re.findall("\s", s))

print(re.findall("\S", s))
########################################################################################################################
# WAP TO PRINT THE WORDS STARTIN WITH h
s = "hai how are you, hello"
# l = []
# a = s.split()
# for i in a:
#     if i[0] == "h":
#         l += [i]
# print(l)

# OR

# print(re.findall("h\w+", s))

# print(re.findall("h[a-z]+", s))
########################################################################################################################
# WAP TO MATCH THE WORDS ENDING WITH Y
# s = "Happy birthday to you"

# print(re.findall("\w+y", s))
########################################################################################################################
# WAP TO ADD THE NUMBERS

# s = "sony12pvt43ltd798"
# total = 0
# l = (re.findall("\d", s))
# for i in l:
#     total += int(i)
#     print(total)
########################################################################################################################
# WAP TO COUNT THE NUMBER OF WHITE SPACES IN THE GIVEN STRING

# s = "hai hello"
# count = 0
# for i in s:
#     if i == " ":
#         count += 1
# print(count)
#
# # OR
#
# print(len(re.findall("\s", s)))


########################################################################################################################
# WAP TO COUNT THE NUMBER OF WHITE SPACES IN THE FILE

# f_path = r"C:\Users\hp\PycharmProjects\Python_Practice\files\samp.txt"
# count = 0
# l = []
# with open(f_path) as f:
#     for line in f:
#         count += line.count(" ")
#         l += (re.findall(" ", line))
#
# print(len(l))
# print(count)
########################################################################################################################
# WAP TO COUNT NUMBER OF OCCURENCES OF A PARTICULAR WORD IN A STRING

# s = "hai hello how how are you"

# print(s.count("how"))

# OR

# print(len(re.findall("how", s)))

########################################################################################################################
# ASSIGNMENT

# WRITE A PROGRAM TO COUNT NUMBER OF OCCURENCES OF A PARTICULAR WORD IN A FILE
# WAP TO COUNT THE NUMBER OF OCCURENCES OF NON SPECIAL CHARACTERS IN THE GIVEN STRING
# s = "hello@world!! welcome!!! to& python***"
# FOR THE SAME STRING COUNT THE NUMBER OF SPECIAL CHARACTERS IN THE ABOVE STRING
# FILTER ONLY THOSE CHARACTERS EXCEPT DIGITS
# s = "sony@123pvt%%43ltd##798!!!"
# WAP TO COUNT THE NUMBER OF CHARACTERS IN EACH WORD AND CREATE A DICTIONARY OF WORD AND ITS LENGTH PAIR
# (ignore special characters)
# s = "hello@ world:) welcome!!! to python:):)"
# WAP TO COUNT THE NUMBER OF UPPERCASE AND LOWER CASE LETTERS IN THE GIVEN STRING
########################################################################################################################
 # wap to count the num of occererces of a particular word in a file
# f_path = r"C:\Users\hp\PycharmProjects\Python_Practice\files\samp.txt"
# with open(f_path) as f:
#     count= 0
#     for line in f:
#         a = line.split()
#         for i in a:
#             if i in "python":
#                 count += 1
#     print(count)
# import re
# with open(f_path) as f:
#     count= 0
#     for line in f:
#         x = re.findall("python", line)
#         count += len(x)
#     print(count)
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#wap to count the num of occurences of non special char in the given string
s = "hello@world_! welcome!!! to& python***"
# import re
# x = re.findall("\w[a-z]+", s)
# print(x)
# a = "".join(x)
# print(a)
# print(len(a))
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# #count the num of special chr in the above string
# import re
# x = re.findall(r"[\W_]+", s)
# a = "".join(x)
# print(len(a))
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#filter only those char except digits
# s = "sony123pvt%%431ltd##789!!!"
# import re
# x = re.findall(r"[a-z\W_]+", s)
# a = "".join(x)
# print(a)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# #wap to count the num of char in a each word and create a dict of word & its len pair(ignore spl chr)
# s = "hello world:) welcome!!! to python:):)"
# import re
# x = re.findall(r"[a-zA-Z]+", s)
# print(x)
# d ={}
# for i in x:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] = 1
# print(d)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#wap to count num of upper case and lower case letter in the given stringg
# s = "HELLO how are c YOU"
# import re
# x = re.findall(r"[A-Z]+", s)
# a = "".join(x)
# print(len(a))
# import re
# x = re.findall(r"[a-z]+", s)
# a = "".join(x)
# print(len(a))
########################################################################################################################
# WAP TO PRINT ONLY THE WORDS STARTING WITH VOWEL
# import re

# s = "python is a programming language and programming is fun"
# a = re.findall(r"\b[aeiou]\w*", s)
# print(a)


