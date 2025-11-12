#1
n=5
ans=1
while(n>0):
    ans*=n
    print(ans)
    n-=1
#2
n=5
ans=1
while(n>0):
    ans*=n
    print(ans)
    n-=1
#3
total=0
while True:
    num=int(input("Enter a no:"))
    total+=num
    if total>300:
        break
print("sum=", total)

#4
while True:
    s=input("enter a string:")
    if s=="bon":
        print("voyage")
        break