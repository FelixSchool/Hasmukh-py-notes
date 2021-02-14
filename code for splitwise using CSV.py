#code for splitwise using CSV

#add users
list_users = [] #list for adding user names
num_users = int(input("please enter the number of users for this group\n")) #taking input of number of contributers
for user in range(0,num_users): #running loop for taking input for name of the users
    x = str(input("please enter the name of user:\n".format(user+1)))
    list_users.append(x) #adding names to the list list_userss
print('The entered users are:\n',list_users) # for checking if the entry is correct

pay_users = [] #list for adding payments done by each users towards the group
for user in range(0,num_users): #using for loop for taking input for the amounts for each users
    print("please enter the amount paid by user",list_users[user],":\n") #asking the amount
    u = int(input()) #putting it in input
    pay_users.append(u) #adding data to pay_users list
    
#print('The entered payments are:\n',pay_users) #checking if the data is correctly entered

import csv #importing csv file for storing data
with open("userss.csv",'w',newline='') as file: #opening csv file for writing new data captured in lists
    writer = csv.writer(file) #using writer as a writing function for csv file
    writer.writerow(list_users) #writing data of user names to csv
    writer.writerow(pay_users) #writing data of payments done by users to csv file
    pay_users.clear() #clearing the payment data to enter more entries

#with open("userss.csv","r") as file: #opening csv file for checking the data entered
#    reader = csv.reader(file) #using reader as a function for readiung the csv file
#    for row in reader: #running for loop for rows in csv file
#        print(row) #this will print each row

def data_entry(): #defining function for multiple data entries of payments by same users
    #if z==str('yes'): #checking if user answers yes when asked if they want to enter more payments data
        for user in range(0,num_users): #running a loop to intake the data of payments by users
            print("please enter the amount paid by user",list_users[user],":\n") #asking user for data
            u = int(input()) #taking input as u for appending in lost
            pay_users.append(u) #this adds the data taken by the function to pay_user list
            user = user+1 #for taking next user data
        print('The entered payments are:\n',pay_users) #for checking if the payments entered are ok

        with open("userss.csv",'a',newline='') as file: #opening the csv for adding the payment data 
            writer = csv.writer(file) #using the writer function for writing new data to file
            writer.writerow(pay_users) #writing the data from pay_users to csv file
            pay_users.clear() #clearing the pay_users list for more data entries

        #with open("userss.csv","r") as file: #opening the file again for checking if the data entered by user is corrrect
        #    reader = csv.reader(file) #using reder function for reading the data
        #    for row in reader: #using for loop for printing each row
        #        print(row) #print function
#pay_users.clear()

#data_entry()

z = input("Do you want to add more data - Yes/no?\n") #asking if user wants to enter more data for payments
while z=='yes': #running while for multiple data enteries till user keep answering yes to above question
    data_entry() #calling data_entry function which takes input from user and put it into csv file
    z = input("Do you want to add more data - Yes/no?\n") #asking again 
else:
    pass #if user answers no then loop is closed

with open("userss.csv",'r',newline='') as file: #csv file is opened for reading the file mainly to covert list data from str to int 
    reader = csv.reader(file) #using reading function for csv file 
    for row in file: #running loop for each row
        for i in range(0, len(row)): #running loop through each row element 
            try: #using try function as 1st data is str (user names)
                row[i] = int(row[i]) #converting data from str to int (payments)
            except Exception: #using exception
                pass
        print(row) #printing the data again to check the conversion


total = int(0) #defining the total variable

with open("userss.csv","r+", newline='') as dic_file: #opening the csv file again for processing the data
    dictreader = csv.DictReader(dic_file)#opening as dictreader as it makes it easier to process the colum wise data
    for row in dictreader: #for loop for goig through each row
        for i in range(0, len(row)): #for loop for going through each element of each row
            total += int(row[list_users[i]]) #adding the all elemnts of all payments entered (i)
            #print(total) #printing the sum for checking
#print(total) #printing the data to check

avg = total/(len(list_users)) #calculating avg of total payments done
#print(avg) #printing the data to check if correct

e = int() #defining the variable e to be used in below function

def csv_cal(i): #defining new function for calculating sum of each column as per (user)
    with open("userss.csv","r+", newline='') as dic_file: #opening csv in read mode
        dictreader = csv.DictReader(dic_file) #using dict reader function as it maked it easier to process column data
        for row in dictreader: #going through each row
            global e #defininf e as global variable
            e += (int(row[list_users[i]])) #adding all the elements specific to coulmn i
            #e = 0
            #print(e)
                

#y = csv_cal(0)
#print(y)

#print('\n') #line space
lol = int() #defininf lol variable for using in below calculations
tot_val = [] #defining new list
#tot_val.clear()
for i in range(0, len(list_users)): #usinf for loop for calculating total payment by each user using the csv_cal function
    csv_cal(i) #calling the function for calculating total for each user
    tot_val.append(e) #appending the data into the list
    e = 0 #setting e to 0 as it carries sum of first column to next column calculations
    
#print(*tot_val, sep=",") #printing the tot_val list to check 
#print('\n') #line space

diff = [] #defining new list for storinf the difference between avg and the total payment by each user
for i in range(0,len(list_users)): #running loop for each user calculation
    dif = avg - tot_val[i] #calculating the diff for each user
    diff.append(dif) #appendinf it into the list

#print(*diff, sep=",") #printing the data to check

for i in range(0,len(list_users)): #running a loop to declare who needs to pay and who needs to receive
    if diff[i] > 0: # checking if the diff is +ve which means the user needs to pay 
        print(list_users[i],"need to pay",diff[i],"INR") #printing what amount the user needs to pay
    else: #if not positive, -ve means the user needs to reacive the diff
        print(list_users[i],"need to receive",(-diff[i]),"INR")#printing the amount that user needs to recieve

print("\n") #line space

a=int() #declaring variable for below loop
for i in range(0,len(list_users)): #entering loop for checking who needs to pay whom what amount. 
    for a in range(0,len(diff)): # takinf new loop fro checking what data match -ve data in the diff list
        if diff[i]==-(diff[a]) and i!=a and diff[i]!=0 and a>i: #Conditions for checking if the number matches
            print(list_users[i],"need to pay",list_users[a],diff[i]) #printing the statement for who needs to pay whom to balance out
            #print(a)
#else:
#    print("Nobody owes anyone anything")
            
        





 
