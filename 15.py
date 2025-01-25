#Write a python program to find the sum of the cosine series 1 - x^2/2! + x^4/4!-.......
sum=1
fact=1
n=int(input("enter the number of terms :"))
x=int(input("enter the value of x :"))
for i in range(1,n+1):
    fact*=i*2
    sum+=((-1)**i)*(x**(2*i))/fact
print(sum)
