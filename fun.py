def Square(num):
    for i in range(1,num+1):
        yield(i)
data=Square(10)
print(next(data)+5)
print(next(data)+5)
print(next(data)+5)
print(next(data)*2)
print(next(data)*2)
print(next(data)*2)
print(next(data)-2)
print(next(data)-2)
print(next(data)+3)
print(next(data)+3)