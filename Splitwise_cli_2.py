

def main():
    import sys
    import argparse
    import csv

    #addd=[]
    #amount=[]
    initi = ['Name','Amt']

    #def cli_add():
    #    parser = argparse.ArgumentParser()
    #    parser.add_argument("-a", "--add", help="add expense by mentioning name and payemnt",nargs=2)
    #    parser.add_argument("-l", "--list", help="list out all expenses", action="store_true")

        #parser.add_argument("-a","--amount",help="please put the amount paid",type=int)
    #    args = parser.parse_args()
    #    global addd
    #    if args.add:
    #        addd = args.add
    #    elif args.list:
    #        print(initi)
    #        read_data()
        
        #print(addd)

    #def cli_exp():
    #    parser = argparse.ArgumentParser()
    #    parser.add_argument("-l", "--list", help="list out all expanses")
    #    #parser.add_argument("-a","--amount",help="please put the amount paid",type=int)
    #    args = parser.parse_args()
    #    if args.list:
    #        print(initi)
    #        read_data()
        

    #list2 = [lst[0]]
    #amount = args.add[1]
    


    #def add_new_csv():
    #    with open("users.csv",'a+',newline='') as file:
    #        writer = csv.writer(file)
    #        writer.writerow(initi)
    #        #addd.clear()
        
    def add_data():
        with open('users.csv', 'a+',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(addd)
            
            #writer.writerow(amount) 
    
    def read_data():
        with open('users.csv', 'r+', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    def dict_read():
        with open('users.csv','r+',newline='') as file:
            dictreader = csv.DictReader(file) 
            for row in dictreader:
                print()

    def csv_cal(i): #defining new function for calculating sum of each column as per (user)
        with open("users.csv","r+", newline='') as dic_file: #opening csv in read mode
            dictreader = csv.DictReader(dic_file) #using dict reader function as it maked it easier to process column data
            for row in dictreader: #going through each row
                global e #defininf e as global variable
                e += (int(row[list_users[i]]))

    def conv():
        with open("users.csv",'r+',newline='') as file: #csv file is opened for reading the file mainly to covert list data from str to int 
            reader = csv.reader(file) #using reading function for csv file 
            for row in file: #running loop for each row
                #row = [int(i) for i in row]
                print(row[2])
                #row[2] = map(int, row[2])
                #list(map(int, row))
                #print(row[2])
                #print(c)
                #print(len(c))
                #for i in range(0, len(row)): #running loop through each row element 
                    #try: #using try function as 1st data is str (user names)
                        #row[i] = int(row[i]) #converting data from str to int (payments)
                        #map(int, row)
                        #row = [int(i) for i in row]
                    #except Exception: #using exception
                    #    pass
        #print(row)

    
    #cli_add()
    #add_data()
    #read_data()

    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--add", help="add expense by mentioning name and payemnt",nargs=2, type=str)
    parser.add_argument("-l", "--list", help="list out all expenses", action="store_true")
    parser.add_argument("-s", "--summary", help="summarize the expanses", action="store_true")

        #parser.add_argument("-a","--amount",help="please put the amount paid",type=int)
    args = parser.parse_args()
    global addd
    if args.add:
        addd = args.add
        add_data()
        read_data()
    elif args.list:
        print(initi)
        read_data()
    elif args.summary:
        conv()
        read_data()


    #print(addd)
    
    #add_data()       
    #read_data()
    #print(initi)





if __name__ == "__main__":
    main()