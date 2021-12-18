# wap to read a particular line from a file and check if that line is empty or not, if the line is empty, raise
# EmptyLineError or else print the line as it is. count the number of words in the line , even if it is empty or not

class EmptyLineError(Exception):
    pass

path = r"C:\Users\DELL\PycharmProjects\python_Practice\files\sample.txt"
line = int(input("enter the line number :"))
with open(path) as f:
    for index, item in enumerate(f, start=1):
        if line == index:
            print("number of words ", len(item.split()))
            if item.strip():
                print(item)

            else:
                raise EmptyLineError("line is empty")

    else:
        print("line number exceeded")















