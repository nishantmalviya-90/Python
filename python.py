# n=int(input("enter the number"))
# i=1
# while i<=n:
#     if i==n:
#      print(i)
#     else:
#      print(i,end=",") 
#     i=i+1

n=int(input("enter the number"))
i=1
sum=0
while i<=n:
    sum=sum+i
    if i<=n-1:
        print(i,end="+")
    else:
        print(i,end="=") 
    i=i+1
print(sum)
 
# n=int(input("enter the number"))
# i=1
# sum=1
# while i<=n:
#     sum=sum*n
#     if i<=n-1:
#         print(n,end="*")
#     else:
#         print(n,end="=")
#     n=n-1
# print(sum)

# n=int(input("enter the no"))
# i=0
# while i<n:
#     print(i*' '+(n-i)*'*')
#     i=i+1

# n=int(input("enter the no"))
# i=0
# while i<n:
#     print('*'*(n-i)+' '*i)
#     i=i+1

# n=int(input("enter the no"))
# i=0
# while i<n:
#     print(i*' '+(n-i)*' *')
#     i=i+1

# n=int(input("enter the no"))
# i=1
# j=0
# while i<=n:
#     print((n-i)*(' ')+(2*i-1)*'*')
#     i=i+1
# while i<n:
#     print(j*' '+(n-j)*' *')
#     j=j+1
