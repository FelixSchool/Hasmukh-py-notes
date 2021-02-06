import re

strg = "welcome to the 29 Netherlands port of Europe"
y = re.findall("the 29 Netherlands",strg)
print ("found:",y)

num_str = "My number is 9876543210, obviously, its a 10 digit number and it cannot be 1023456789"
a = "\d{10}"
b = re.findall(a,num_str)
print(b[0])