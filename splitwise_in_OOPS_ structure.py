#splitwise code in OOPS

class inputs: #class for taking inputs from users

    def user_input(self): #method for taking user names from cusotmer
        inputs.list_users = [] #list for adding user names
        
        inputs.num_users = int(input("please enter the number of users for this group\n")) #taking input of number of contributers
        for user in range(0,inputs.num_users): #running loop for taking input for name of the users
            x = str(input("please enter the name of user:\n".format(user+1)))
            inputs.list_users.append(x) #adding names to the list list_userss
        print('The entered users are:\n',inputs.list_users)
        

    def user_payments(self): #mehtod for taking payment info from user
        inputs.pay_users = [] #list for adding payments done by each users towards the group
        print(inputs.num_users)
        for i in range(0, inputs.num_users): #using for loop for taking input for the amounts for each users
            print("please enter the amount paid by user",inputs.list_users[i],":\n") #asking the amount
            u = int(input()) #putting it in input
            inputs.pay_users.append(u)
        print('The entered payments are:\n',inputs.pay_users)
    
    def data_ent(self): #method for taking further additional payment inputs
        for user in range(0,inputs.num_users): #running a loop to intake the data of payments by users
            print("please enter the amount paid by user",inputs.list_users[user],":\n") #asking user for data
            u = int(input()) #taking input as u for appending in lost
            inputs.pay_users.append(u) #this adds the data taken by the function to pay_user list
            user = user+1 #for taking next user data
        print('The entered payments are:\n',inputs.pay_users)

        #with open("userss.csv",'a',newline='') as file: #opening the csv for adding the payment data 
        #    writer = csv.writer(file) #using the writer function for writing new data to file
        #    writer.writerow(inputs.pay_users) #writing the data from pay_users to csv file
        #    inputs.pay_users.clear()

    
 

class csv_ops: #class for csv operations
    def open_new_csv(self): #method for opening fresh csv file
        import csv #importing csv file for storing data
        self.users_list = inputs.list_users
        self.payment_list = inputs.pay_users
        with open("userss.csv",'w',newline='') as file: #opening csv file for writing new data captured in lists
            writer = csv.writer(file) #using writer as a writing function for csv file
            writer.writerow(self.users_list) #writing data of user names to csv
            writer.writerow(self.payment_list) #writing data of payments done by users to csv file
            inputs.pay_users.clear() 

    def append_csv(self): #method for appending new data into csv
        import csv
        with open("userss.csv",'a+',newline='') as file: #opening the csv for adding the payment data 
            writer = csv.writer(file) #using the writer function for writing new data to file
            writer.writerow(inputs.pay_users) #writing the data from pay_users to csv file
            inputs.pay_users.clear()

    def read_csv(self): #method for reading the csv file
        import csv
        with open("userss.csv",'r+',newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    def convert_int(self): #mehtod for conversion of csv data from str to int
        import csv
        with open("userss.csv",'r',newline='') as file: #csv file is opened for reading the file mainly to covert list data from str to int 
            reader = csv.reader(file) #using reading function for csv file 
            for row in file: #running loop for each row
                for i in range(0, len(row)): #running loop through each row element 
                    try: #using try function as 1st data is str (user names)
                        row[i] = int(row[i]) #converting data from str to int (payments)
                    except Exception: #using exception
                        pass
                print(row)

    def total(self): #method for getting total of all payments
        import csv
        csv_ops.total_ele = int()
        with open("userss.csv","r+", newline='') as dic_file: #opening the csv file again for processing the data
            dictreader = csv.DictReader(dic_file)#opening as dictreader as it makes it easier to process the colum wise data
            for row in dictreader: #for loop for goig through each row
                for i in range(0, len(row)): #for loop for going through each element of each row
                    csv_ops.total_ele += int(row[inputs.list_users[i]]) #adding the all elemnts of all payments entered (i)
            print(csv_ops.total_ele) #printing the sum for checking

    def csv_cal(self,i): #defining new method for calculating sum of each column as per (user)
        import csv
        csv_ops.e = int()
        with open("userss.csv","r+", newline='') as dic_file: #opening csv in read mode
            dictreader = csv.DictReader(dic_file) #using dict reader function as it maked it easier to process column data
            for row in dictreader: #going through each row
                #global e #defininf e as global variable
                csv_ops.e += (int(row[inputs.list_users[i]]))

    
       




take_inpts=inputs() #obj for taking user names
payment_inputs=inputs() #object for taking payment info
open_csv=csv_ops() #obj for opening new csv
take_multiple_inputs=inputs() ##obj for taking additional payment data
append_data=csv_ops() #obj for appending new data received
read_data=csv_ops() #obj for reading the csv data
convert_to_int=csv_ops() #obj for converting list data into int
get_total=csv_ops() #obj for getting total of all payments


take_inpts.user_input() #takning user names
payment_inputs.user_payments() #takinf first payment data
open_csv.open_new_csv() #writing above data into new csv

ask = input("Would you like to enter more payments?\n") #asking user if they want to add more data
while ask == "yes": #of they answer yes run loop for more data
    take_multiple_inputs.data_ent() #calling object for taking multiple inputs
    append_data.append_csv() #appending data obj
    ask = input("Would you like to enter more payments?\n") #ask again for loop
else: #if answered no or anything else, pass
    pass

read_data.read_csv() #read the above put data from csv
convert_to_int.convert_int() # convert the list data into int
get_total.total() #obj for getting total of all payments

avg = csv_ops.total_ele/(len(inputs.list_users)) #gettting avg of all payments

tot_val=[] #defining list
for i in range(0, len(inputs.list_users)): #usinf for loop for calculating total payment by each user using the csv_cal function
    get_total.csv_cal(i) #calling the function for calculating total for each user
    tot_val.append(csv_ops.e) #appending the data into the list
    csv_ops.e = 0

print(tot_val)

diff = [] #defining new list for storinf the difference between avg and the total payment by each user
for i in range(0,len(inputs.list_users)): #running loop for each user calculation
    dif = avg - tot_val[i] #calculating the diff for each user
    diff.append(dif) #appendinf it into the list

#print(*diff, sep=",") #printing the data to check

for i in range(0,len(inputs.list_users)): #running a loop to declare who needs to pay and who needs to receive
    if diff[i] > 0: # checking if the diff is +ve which means the user needs to pay 
        print(inputs.list_users[i],"need to pay",diff[i],"INR") #printing what amount the user needs to pay
    else: #if not positive, -ve means the user needs to reacive the diff
        print(inputs.list_users[i],"need to receive",(-diff[i]),"INR")#printing the amount that user needs to recieve

print("\n") #line space

a=int() #declaring variable for below loop
for i in range(0,len(inputs.list_users)): #entering loop for checking who needs to pay whom what amount. 
    for a in range(0,len(diff)): # takinf new loop fro checking what data match -ve data in the diff list
        if diff[i]==-(diff[a]) and i!=a and diff[i]!=0 and a>i: #Conditions for checking if the number matches
            print(inputs.list_users[i],"need to pay",inputs.list_users[a],diff[i]) #printing the statement for who needs to pay whom to balance out
            #print(a)