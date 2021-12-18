# WAP TO SORT THE LIST BASED ON LENGTH OF EACH ELEMENT
# CUSTOM SORTING
# names = ["john", "nikhil", "mahesh"]
# print(sorted(names, key=len, reverse =True))
########################################################################################################################
# WAP TO SORT BASED ON THE LAST CHARACTER OF EACH ELEMENT

# names = ("john", "nikhil", "mahesh")
# print(sorted(names, key = lambda item: item(len[-1])))
########################################################################################################################
# WAP TO SORT BASED ON THE MIDDLE CHARACTER OF EACH ELEMENT

# names = ("john", "nikhil", "mahesh")
# res = (sorted(names, key = lambda item: item[len(item)//2]))
# print(res)

########################################################################################################################
# WAP TO SORT KEYS IN A DICTIONARY BASED ON FIRST CHARACTER

# d = {"apple" : 1, "banana" : 2}
# res = sorted(d)
# print(res)
#
# d = {"apple" : 1, "banana" : 2}
# res = sorted(d.keys())
# print(res)
#
# d = {"banana" : 1, "apple" : 2}
# res = sorted(d.items())
# print(dict(res))
########################################################################################################################
# WAP TO SORT KEYS IN A DICTIONARY BASED ON LAST CHARACTER

# d = {"banana" : 1, "apple" : 2}
# op1 = sorted(d, key = lambda item: item[-1])
# print(op1)

# d = {"banana" : 1, "apple" : 2}
# op1 = sorted(d.keys(), key = lambda item: item[-1])
# print(op1)

# d = {"banana" : 1, "apple" : 2}
# op1 = sorted(d.items(), key = lambda item: item[0][-1])
# print(op1)
########################################################################################################################
# WAP TO SORT VALUES IN A DICTIONARY BASED ON FIRST CHARACTER

# d = {"apple" : 1, "banana" : 2}
# res = sorted(d.values())
# print(res)

# d = {"banana" : 1, "apple" : 2}
# res = sorted(d.items(), key = lambda item: item[-1])
# print(dict(res))
########################################################################################################################
# SORT THE BELOW LIST BASED ON THE LAST CHARACTER OF EACH ELEMENT

# items = ['bv', 'aw', 'dt', 'cu']
# op1 = sorted(items, key = lambda item: item[-1])
# print(op1)
########################################################################################################################
# SORT THE BELOW LIST BASED ON TEMPERATURE OF EACH LIST

# temp = [('Bangalore', 25), ('Delhi', 35), ('Chennai', 37), ('Mumbai', 32)]
# op = sorted(temp, key = lambda item: item[-1])
# print(op)

# MIN AND MAX
# temp = [('Bangalore', 25), ('Delhi', 35), ('Chennai', 37), ('Mumbai', 32)]
# min_, *rest, max_ = sorted(temp, key = lambda item: item[-1])
# print(min_)
# print(max_)
########################################################################################################################
# SORT BASED ON THE FIRST VALUE OF THE INNER LIST

# items = [[2, 7], [7, 3], [3, 8], [8, 7], [9, 7], [4, 9]]
# op = sorted(items)
# print(op)
########################################################################################################################
# SORT BASED ON THE LAST VALUE OF THE INNER LIST

# op = sorted(items, key = lambda item: item[-1])
# print(op)
########################################################################################################################
# WAP TO SORT BELOW DICTIONARY BASED ON SHARE PRICE AND PRINT THE MAX SHARE PRICE AND ITS NAME

# prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75, }
# *rest, max_ = sorted(prices.items(), key = lambda item: item[-1])
# print(max_)
########################################################################################################################
# WAP TO SORT MAX REPEATED WORD ALONG WITH ITS LENGTH

# sentence = "hi how are you how is your health"
# a = sentence.split()
# d = {item: a.count(item) for item in a}
# print(d)
#
# min_, *rest, max_ = sorted(d.items(), key = lambda item: item[-1])
# print(max_)
########################################################################################################################
# WAP TO FIND THE LONGEST WORD ALONG WITH ITS LENGTH

# sentence = "python is a programming language and programming is fun"
# a = sentence.split()
# d = {item : len(item) for item in a}
# print(d)
# shortest, *rest, longest = sorted(d.items(), key = lambda item: item[-1])
# print(shortest)

########################################################################################################################
# WAP TO PRINT THE LONGEST NON REPEATED WORD IN THE SENTENCE

# sentence = "python is a programming language and programming is fun"
# a = sentence.split()
# d = {item : len(item) for item in a if a.count(item) == 1}
# print(d)
# *rest, longest = sorted(d.items(), key = lambda item: item[-1])
# print(longest)
########################################################################################################################
# SORTING LIST OF DICTIONARIES
# students = [{"name": "john", "grade": "A", "age": 26}, {"name": "jane", "grade": "B", "age": 28}, {"name": "dave", "grade": "B", "age": 22}]

# sorting based on age

# print(sorted(students, key=lambda item: item["age"]))

# sorting based on name

# print(sorted(students, key=lambda item: item["name"]))
########################################################################################################################


