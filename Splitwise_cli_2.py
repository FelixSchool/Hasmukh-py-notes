

def main():
    import sys
    import argparse
    import csv

    addd=[]
    amount=[]
    global pay
    pay=[]
    initi = ['Name','Amt']
    global tota
    tota = int()
    #global x
    global l
    l=int()
    
    def reset_csv(): #used for reseting the csv
        with open('users.csv','w',newline='') as file:
            writer = csv.writer(file)
            
        
    def add_data(): #used for adding new data to csv
        with open('users.csv', 'a+',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(addd)
    
    def read_data(): #used for reading the data from the csv
        with open('users.csv', 'r+', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    def dict_read(): #just useless func
        with open('users.csv','r+',newline='') as file:
            dictreader = csv.DictReader(file) 
            for row in dictreader:
                print()

    def convert(s): #another useless func
        str1=''
        return(str1.join(s))

    def totale(): #for calculating total of all the payments
        global tota
        with open('users.csv','r+',newline='') as file:
            reader = csv.reader(file)
            
            for row in reader:
                tota += int(row[1])

    def per_p_tot():#used for finding out the list of uniquse user names from the csv file
        uni=[]
        global x
        global l
        with open('users.csv','r+',newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                uni.append(row[0])
            #print(uni)
            x = list(set(uni))
            #print(x)
            l = int(len(x))

    def tot_per_p(): #used for calculating payment done by each unique user
        global pay
        pay=[]
        global paym
        paym=int()
        userfiles=[]
        #global i
        i=0
        with open('users.csv','r+') as file:
            reader = csv.reader(file)
            while i<(len(x)):
                for row in reader:
                    if x[i]==row[0]:
                        paym = paym + int(row[1])
                i=i+1
                pay.append(paym)
                paym=0
                file.seek(0)
                
        #print(pay)
    
    #useing parser for taking cli commands
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--add", help="add expense by mentioning name and payemnt",nargs=2, type=str)
    parser.add_argument("-l", "--list", help="list out all expenses", action="store_true")
    parser.add_argument("-s", "--summary", help="summarize the expanses", action="store_true")
    parser.add_argument("-c","--clear", help="clear the csv file",action="store_true")

    args = parser.parse_args()
    
    #condition for activation of code based on a input by used in cli
    if args.add: #if user puts -a and data
        addd = (args.add) #addd taked the data in list form
        add_data() #adds the data to csv
        read_data() #reads the data back to user 
    elif args.list: #if user puts -l then it returns the list of all entires
        print(initi) #for putting heading - name and payment
        read_data() #for reading the data from csv
    elif args.clear: # if user puts -c in cli for clearing the data
        reset_csv() #resets the csv
    elif args.summary: # if user purs -s in cli for final summary of payments
        try:
            read_data() # reads data off csv
            totale() #calculates total of all payments
            #print(tota) 
            per_p_tot() #calculates unique number of users
            #print(x)
            avrg=int((tota/l)) #here is length of list returned by per_p_tot
            #print(avrg) 
            tot_per_p() #calcaultes the total payment done by each user
            #print(pay)
            diff = [] #defining new list for storinf the difference between avg and the total payment by each user
            for i in range(0,len(x)): #running loop for each user calculation
                dif = avrg - pay[i] #calculating the diff for each user
                diff.append(dif)
            
            for i in range(0,len(x)): #running a loop to declare who needs to pay and who needs to receive
                if diff[i] > 0: # checking if the diff is +ve which means the user needs to pay 
                    print(x[i],"need to pay",diff[i],"INR") #printing what amount the user needs to pay
                else: #if not positive, -ve means the user needs to reacive the diff
                    print(x[i],"need to receive",(-diff[i]),"INR")#printing the amount that user needs to recieve
        except Exception:
            print("Sorry, no entries found")


if __name__ == "__main__":
    main()