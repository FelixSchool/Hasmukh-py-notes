#code for splitwise using CSV

#add users
list_users = []
num_users = int(input("please enter the number of users for this group\n"))
for user in range(0,num_users):
    x = str(input("please enter the name of user:\n".format(user+1)))
    list_users.append(x)
print('The entered users are:\n',list_users)

pay_users = []
#pay_users = int(input("please enter the amount paid by the user for this group\n"))
for user in range(0,num_users):
    print("please enter the amount paid by user",list_users[user],":\n")
    u = int(input())
    #print(list_users[user])
    pay_users.append(u)
    user = user+1
print('The entered payments are:\n',pay_users)

import csv
with open("userss.csv",'w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(list_users)
    writer.writerow(pay_users)
    pay_users.clear()
    
with open("userss.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#asking if user wants to add more data



def data_entry():
    if z==str('yes'):
        for user in range(0,num_users):
            print("please enter the amount paid by user",list_users[user],":\n")
            u = int(input())
            #print(list_users[user])
            pay_users.append(u)
            user = user+1
        print('The entered payments are:\n',pay_users)

        with open("userss.csv",'a',newline='') as file:
            writer = csv.writer(file)
            #writer.writerow(list_users)
            writer.writerow(pay_users)
            #append_list_as_row('userss.csv', pay_users)
            pay_users.clear()

        with open("userss.csv","r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

z = input("Do you want to add more data - Yes/no?\n")
while z=='yes':
    data_entry()
    z = input("Do you want to add more data - Yes/no?\n")
else:
    pass

a1=int()

with open("userss.csv",'r',newline='') as file:
    reader = csv.reader(file)
    #data = [eval(row()) for row in data]
    #writer.writerow(list_users)
    for row in file:
        
        for i in range(0, len(row)): 
            try:
                row[i] = int(row[i])
            except Exception:
                pass
        print(row)
    #tot = sum()
    #print(tot)

total = int(0)

with open("userss.csv","r+", newline='') as dic_file:
    dictreader = csv.DictReader(dic_file)
    for row in dictreader:
        for i in range(0, len(row)):
            #if i==0:
            total += int(row[list_users[i]])
            print(total)
        #i=int(0)
        #for i in list_users:
        #total = sum(row[i])
    print(total)



#with open("userss.csv",'r+',newline='') as o_file:   
    #dictreader = csv.DictReader(o_file)
    #has_header = csv.Sniffer().has_header(file.read(1024))
    #file.seek(0)  # Rewind.
    #reader = csv.reader(file)
    #row = 1
    #for row in dictreader:
    #    print(row['a'])
        #i = int(1)
        #total = sum((row[list_users[i]]))
        #print(total)
        #i=int(1)
        #if ((row).isdecimal()) == False:
        #try:
            #for row in reader:
            #for i in range(0,len(row)):
                #if i.isalpha() == False:
            #    total += int(row[list_users[i]])
            #    print(total)
            #else:
            #    pass
        #except Exception:
        #    pass
        

#print(total)
    
     
    



#file = open("userss.csv",'r')
#reader = csv.reader(file)
#for row in reader:
#    print(row)

#file.close()

#enter the name of the person who paid


#with open('userss.csv','a'newline='') as file:
#    writer.writerow({input("")})
