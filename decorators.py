# basics of decoratores:

#  # nested_function....
# def fun1(x):
#     def fun2(y):
#         return x+y
#     return fun2
# var1 = fun1(5)
# var2 = var1(5)
# print(var2)

# # function pass as a argument....
# def add(x,y):
#     return x+y

# def cal(func,x,y):
#     return func(x,y)

# var1 = cal(add,4,5)
# print(var1)

# # function that returns a function.......
# def fun1(num):
#     def fun2(x):
#         x=num+x
#         return x
#     return fun2

# var1 = fun1(5)
# var2 = var1(10)

# print(var2)

# Decorators:---
# # first method for decorator.......
# def decorator(fun):
#     def wrapper():
#         print("Work started.......")
#         fun()
#         print("Work completed......")
#     return wrapper

# def original_fun():
#     print("Original function work....")

# x = decorator(original_fun)
# x()

# # Second method for decorator.......
# def decorator(fun):
#     def wrapper():
#         print("Work started.......")
#         fun()
#         print("Work completed......")
#     return wrapper
# @decorator
# def original_fun():
#     print("Original function work....")

# original_fun()