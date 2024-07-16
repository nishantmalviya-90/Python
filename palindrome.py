a=int(input("enter any name: "))
n,digit=a,0
while a>0:
    rev=a%10
    digit=digit*10+rev
    a=a//10
if digit==n:
    print("it is a palindrome no.")
else:
    print("it is not a palindrome no.")