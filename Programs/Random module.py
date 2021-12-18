import re
dates = ["2019-01-02", "2019-13-08", "2021-12-26", "2022-01-32"]
# count = 0
# with open(f_path) as file:
#     for line in file:
#         count += 1
#         if count <= 3:
#             print(line)

# read random line
import itertools

def random_line(file_path, line_no):
    with open(file_path) as file:
        res = itertools.islice(file, line_no-1, line_no)
        print(list(res))

# random_line(f_path, 5)

# read last 2 lines

def last_2_lines(filepath):
    with open(filepath) as file:
        lines = 0
        for _ in file:
            lines += 1      # 7
        file.seek(0)
        res = itertools.islice(file, lines-2, lines)
        print(list(res))

# last_2_lines(f_path)

from collections import deque
def last_n_lines(filepath, n):
    with open(filepath) as file:
        res = deque(file, n)
        print(list(res))

last_n_lines(f_path, 2)

