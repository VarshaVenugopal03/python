lb=int(input("enter the lower limit:"))
ub=int(input("enter the upper limit:"))
sum=0
if lb%2!=0:
    for i in range(lb,ub+1,2):
        sum=sum+i
else:
    for i in range(lb+1,ub+1,2):
        sum=sum+i
print(sum)
           
