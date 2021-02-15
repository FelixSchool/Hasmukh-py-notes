class Rom:
    def funcc(self, a=0):
        if a==1:
            print("I")
        elif a==2:
            print("II")
        elif a==3:
            print("III")
        else: 
            print("null")

w = Rom()
z = input("please put the num\n")
print(z)
w.funcc(z)
