# #prime number way 1
num=int(input("enter the number:"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count +=1
if count==2:
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")

#prime number way 2
num=int(input("enter the number:"))

for i in range(2,num):
    if num%i==0:
        print("not prime")
        break
else:
    print("prime")

# prime number way 3
