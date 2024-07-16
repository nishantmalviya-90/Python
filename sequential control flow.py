# my_list=[10,20,30,40]
# print(len(my_list))
# print(max(my_list))
# print(min(my_list))
# print(sum(my_list))
# print(my_list.append(10)) 
n=int(input("enter the range of no. "))
a=1
i=n
while(n>=1):
    if(n==1):
        print(n,end="=")
    else:
        print(n,end="x")
    a=a*n
    n=n-1
print(a)