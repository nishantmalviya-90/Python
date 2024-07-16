n=int(input("enter any no. "))
p=m=n
c=0
s=0
while n>0:
    c=c+1
    n=n//10
while m>0:
    digit=m%10
    s=s+digit**c
    m=m//10
if s==p:
    print("it is an armstrong no.")
else:
    print("it is not an armstrong no.")