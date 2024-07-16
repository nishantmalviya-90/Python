#positional argument 

# def add(x,y):
#     return x+y
# print(add(4,7))

# default argument

# def add(x=0,y=0,z=0):
#     return x+y+z
# print(add())
# print(add(5))
# print(add(5,4))

# keyword argument

# def add(x,y,z):
#     return(x+y+z)
# print(add(y=10,z=5,x=5))

# variable length argument
# 1> all the arguments are get in tuple type
# 2> this is used when we dont know the number of input a user send as parameters
# 3> *args means argument

# def add(*n):
#     print(n)
#     print(type(n))
#     s=0
#     for i in n:
#         s=s+i
#     return(s)
# print(add(5,6,7,8))

# keyword variable length argument

# def stu_detail(**n):
#     print(n) 
#     print(type(n))
#     for k,v in n.items():
#         print(k,"=",v)

# stu_detail(name="utkarsh",age=20,qualification="under graduate")