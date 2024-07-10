# Scope
# global and local Scope

# x=10 ----->Global define
# def show():
#     x=20----->local define
#     return x
    
# y=show()
# print(y)
# print(x)

x=10
def show():
    global x
    x=20
    return x

print(x)    
y=show()
print(y)
print(x)