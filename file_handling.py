x = open("test.txt","x")
x.close()
import os
import datetime
os.rename(r'.\test.txt',r'hasmukh.txt')

try:
    x = open("hasmukh.txt","a")
    x.write("23-05-1996\n")
    x.write("college VIT\n")
    x.flush()
finally:
    x.close()

try: 
    x = open("hasmukh.txt",'a')
    x.write("2018\n")
    x.flush()
finally:
    x.close()

x = open("hasmukh.txt")

print(x.readline())
print(x.readline())
print(x.readline())