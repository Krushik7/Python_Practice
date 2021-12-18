# WAP TO PRINT THE NUMBER OF WORDS INSIDE A FILE
# f_path = r"C:\Users\hp\PycharmProjects\Python_Practice\files\samp.txt"
# with open(f_path) as f:
#     count = 0
#     for line in f:
#         a = line.split()
#         count += len(a)
#     print(count)
########################################################################################################################
# COUNT THE NUMBER OF LINES PRESENT IN A FILE

# f_path = r"C:\Users\hp\PycharmProjects\Python_Practice\files\samp.txt"
# with open(f_path) as f:
#     count = 0
#     for line in f:
#         count += 1
#     print(count)
########################################################################################################################
# WAP TO READ THE LINES ALONG WITH THE LINE NUMBER

# f_path = r"C:\Users\hp\PycharmProjects\Python_Practice\files\samp.txt"
# with open(f_path) as f:
#     for line_no, line in enumerate(f, start = 1):
#         if line.strip():                     #checks for empty lines
#             print(line_no, line)

# OR

# f_path = r"C:\Users\hp\PycharmProjects\Python_Practice\files\samp.txt"
# with open(f_path) as f:
#     line_no = 0
#     for line in f:
#         if line.strip():
#             line_no += 1
#             print(line_no, line)
########################################################################################################################
# WAP TO READ THE FILE IN REVERSED ORDER

# f_path = r"C:\Users\hp\PycharmProjects\Python_Practice\files\samp.txt"
# with open(f_path) as f:
#     for line in reversed(list(f)):
#         print(line)
########################################################################################################################
# WAP TO READ 10 CHARACTERS AT A TIME

# f_path = r"C:\Users\hp\PycharmProjects\Python_Practice\files\samp.txt"
# with open(f_path) as f:
#     data = f.read(10)
#     print(data)
########################################################################################################################
# WAP TO FIND THE NUMBER OF CHARACTERS IN EACH LINE

# f_path = r"C:\Users\hp\PycharmProjects\Python_Practice\files\samp.txt"
# with open(f_path) as f:
#     count = 0
#     for line in f:
#         print(len(line))
#         count += 1
#     print(count)


########################################################################################################################
# WAP TO EXTRACT IP ADDRESS FROM ACCESS LOG TXT FILE

# f_path = r"C:\Users\hp\PycharmProjects\Python_Practice\files\access-log.txt"
# with open(f_path) as f:
#     for line in f:
#         if line.strip():
#             a = line.split()
#             print(a[0])
########################################################################################################################
# WAP TO GET UNIQUE IP ADDRESS FROM ACCESS LOG TXT FILE

# f_path = r"C:\Users\hp\PycharmProjects\Python_Practice\files\access-log.txt"
# with open(f_path) as f:
#     ip_address = []
#     for line in f:
#         if line.strip():
#             a = line.split()
#             ip_address.append(a[0])
#     print(ip_address)
#
# print(set(ip_address))

########################################################################################################################
# CREATE A DICTIONARY OF IP ADDRESS AND ITS COUNT PAIR

# f_path = r"C:\Users\hp\PycharmProjects\Python_Practice\files\access-log.txt"
# with open(f_path) as f:
#     ip_address = []
#     for line in f:
#         if line.strip():
#             a = line.split()
#             ip_address.append(a[0])
#
# a = {}
# for i in ip_address:
#     a[i] = ip_address.count(i)
# print(a)
########################################################################################################################
# IN THE ABOVE DICTIONARY PRINT THE MOST OCCURED AND LEAST OCCURED IP ADDRESS

# least, *rest, most = sorted(a.items(), key=lambda item: item[-1])
# print(least)
# print(most)
########################################################################################################################
# WAP TO EXTRACT THE MESSAGES FROM SAMPLE.log

# f_path = r"C:\Users\hp\PycharmProjects\Python_Practice\files\sample.log"
# with open(f_path) as f:
#     for line in f:
#         if line.strip():
#             a = line.split()
#             print(a[2])
#######################################################################################################################
# WAP TO COUNT THE NUMBER OF OCCURENCES OF IP ADDRESS IN ACCESS LOG USING DEFAULT DICT AND ALSO WITHOUT USINNG COUNT METHOD

# f_path = r"C:\Users\hp\PycharmProjects\Python_Practice\files\access-log.txt"
#  WITH OUT USING COUNT METHOD
# d = {}
# with open(f_path) as f:
#     for line in f:
#         if line.strip():
#             a = line.split()
#             if a[0] not in d:
#                 d[a[0]] = 1
#             else:
#                 d[a[0]] += 1
#     print(d)

# USING DEFAULT DICT
# from collections import defaultdict
# with open(f_path) as f:
#     b = defaultdict(int)
#     for line in f:
#         if line.strip():
#             a = line.split()
#             b[a[0]] += 1
#     print(b)

########################################################################################################################
# WAP TO PRINT THE MOST OCCURING AND LEAST OCCURING MESSAGE IN THE LOG FILE

# f_path = r"C:\Users\hp\PycharmProjects\Python_Practice\files\sample.log"
# d = {}
# with open(f_path) as f:
#     for line in f:
#         if line.strip():
#             a = line.split()
#             if a[2] not in d:
#                 d[a[2]] = 1
#             else:
#                 d[a[2]] += 1
#     print(d)

# from collections import defaultdict
# with open(f_path) as f:
#     b = defaultdict(int)
#     for line in f:
#         if line.strip():
#             a = line.split()
#             b[a[2]] += 1
#     print(b)

# l = []
# with open(f_path) as f:
#     for line in f:
#         if line.strip():
#             a = line.split()
#             l.append(a[2])
#
#
# d ={i: l.count(i) for i in l}
# print(d)
########################################################################################################################
# PRINT THE MESSAGES AFTER COLON IN SAMPLE LOG FILE
# f_path = r"C:\Users\hp\PycharmProjects\Python_Practice\files\sample.log"
# l = []
# with open(f_path) as f:
#     for line in f:
#         if line.strip():
#             a = line.split(":.")
#             l.append(a[1])
#     print(l)


# OR

# f_path = r"C:\Users\hp\PycharmProjects\Python_Practice\files\sample.log"
# with open(f_path) as f:
#     for line in f:
#         if line.strip():
#             a = line.split(":.")
#             print(a[1])
########################################################################################################################
# WAP TO COUNT THE NUMBER OF SPACES IN SAMPLE.TXT FILE

# f_path = r"C:\Users\hp\PycharmProjects\Python_Practice\files\sample.txt"
# with open(f_path) as f:
#     count = 0
#     for line in f:
#         if line.strip():
#             a = line.split()
#             if " " in line:
#                 count += line.count(" ")
#     print(count)

# OR

# f_path = r"C:\Users\hp\PycharmProjects\Python_Practice\files\sample.txt"
# with open(f_path) as f:
#     count = 0
#     for line in f:
#         if line.strip():
#             a = line.split()
#             for ch in line:
#                 if ch == " ":
#                     count += 1
#     print(count)

# OR

# from collections import defaultdict
# count = 0
# with open(f_path) as f:
#     b = defaultdict(int)
#     for line in f:
#         if line.strip():
#             for ch in line:
#                 if ch in " ":
#                     b[" "] += 1
#     print(b)

# OR
# from collections import Counter
# f_path = r"C:\Users\hp\PycharmProjects\Python_Practice\files\sample.txt"
# with open(f_path) as f:
#     d = Counter()
#     for line in f:
#         if line.strip():
#             d += Counter(line)
#     print(d[" "])
########################################################################################################################
# WAP TO PRINT COUNTRY NAME IN FOOTBALL.TXT

# f_path = r"C:\Users\hp\PycharmProjects\Python_Practice\files\football.txt"
# with open(f_path, encoding = 'UTF-8') as f:
#     for line in f:
#         if line.strip():
#             a = line.split("\t")
#             print(a[1])
########################################################################################################################
# WAP TO PRINT MOST OCCURING COUNTRY NAME ALONG WITH ITS COUNT

# f_path = r"C:\Users\hp\PycharmProjects\Python_Practice\files\football.txt"
# with open(f_path, encoding = 'UTF-8') as f:
#     d = {}
#     for line in f:
#         if line.strip():
#             a = line.split()
#             if a[1] not in d:
#                 d[a[1]] = 1
#             else:
#                 d[a[1]] += 1
# print(d)
#
# least, *rest, most = sorted(d.items(), key = lambda item : item[-1])
# print(least)
########################################################################################################################
# WAP TO PRINT LINE NUMBER OF THE WORD GIVEN BY THE USER

# f_path = r"C:\Users\hp\PycharmProjects\Python_Practice\files\sample.txt"
# with open(f_path) as f:
#     word = input("enter the word")
#     for line_no, line in enumerate(f, start = 1):
#         if word in line:
#             print(line_no, line)
########################################################################################################################
# ANALYSIS OF VACCINATION DATA

# total vaccination of all countries
# path = r"C:\Users\hp\PycharmProjects\Python_Practice\csv_files\vaccination-data.csv"
#
# with open(path) as f:
#     l = []
#     total = 0
#     for i in f:
#         a = i.split(',')
#         l += [a[5]]
#     print(l)
#     for j in range(len(l)):
#         if l[j].strip():
#             if j != 0 and l[j].isnumeric():
#                 total += int(l[j])
#     print(total)
########################################################################################################################

# # total vaccination by country
#
# with open(path) as f:
#
#     d = {}
#     for i in f:
#         l = i.split(',')
#         d[l[0]] = l[5]
#     print(d)

########################################################################################################################

# COUNTRY AND PERSONS VACCINATED AND GET TOP 3 COUNTRIES WITH HIGHEST VACCINATES PEOPLE
# with open(path) as f:
#     d = {}
#     for i in f:
#         l = i.split(',')
#         if l[5].isnumeric():
#             d[l[0]] = l[5]
#     print(d)
#     *rest, m1, m2, m3 = sorted(d.items(), key=lambda item: int(item[-1]))
#     print(m1, m2, m3)
########################################################################################################################

# countries with less than 10k vaccinates people

# with open(path) as f:
#     d = {}
#     for i in f:
#         l = i.split(',')
#         if l[5].isnumeric() and int(l[5]) < 5:
#             d[l[0]] = l[5]
#     print(d)
########################################################################################################################





















