#all prime numbers till 1000
print("the prime numbers till 1000 are:")
print(2)
for i in range(2,1001):
    count=0
    for j in range(2,i):
        if i%j==0:
            count+=1
            break
    if count==0:
        print(i)
