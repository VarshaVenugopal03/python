#youngest and eldest of 3 individuals
ind1=int(input("enter the age of 1st person:"))
ind2=int(input("enter the age of 2nd person:"))
ind3=int(input("enter the age of 3rd person:"))
if ind1>ind2 and ind1>ind3:
    print("person 1 is the oldest!!!!")
elif ind2>ind1 and ind2>ind3:
    print("person 2 is the oldest!!!!")
else:
    print("person 3 is the oldest!!!!")
