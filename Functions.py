# type of argument
# positional argument
# def add(x,y):
#     return x+y

# add=add(4)
# print(add)

# default argument
# def add(x=0,y=0,z=0):
#     return x+y+z
# add=add()
# print(add)
# add=add(5)
# print(add)

# keyword argument
# def add(x,y,z):
#     return x+y+z

# add1=add(y=10,z=5,x=5)
# print(add1)

# variable length argument (*args) works only tuple
# def add(*n):
#     print(n)
#     sum=0
#     for i in n:
#         sum=sum+i
#     return sum

# x=add(5)
# print(x)
# y=add(5,6,7,8)
# print(y)

# key-word variable length argument
# def stu_detail(**kwargs):
#     print(kwargs)
#     for k,v in kwargs.items():
#         print(k,"=",v)

# stu_detail(name="nishant",age=20,qualification="Btech")        