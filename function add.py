def fun_add(x,y):
    return(x+y,x-y,x*y,x/y)
a=int(input("enter any no."))
b=int(input("enter any no."))
p,q,r,s=fun_add(a,b)
print(p,q,r,s)