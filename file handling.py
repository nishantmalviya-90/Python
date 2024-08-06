# 1. Create
# 2. Open
# 3. Read/Write
# 4. Close
# Syntx:-
#   open(file name,'mode)
#                    |......x -> Create
#                    |......r -> Read
#                    |......w -> Write //if your have data already in your file so never run 'w' mode becz its delete all data
#                    |......a -> Append 
# Type of File :- 1. Text File 2. Bnary File 3. .csv file 
# f=open("new.txt",'x') 
# f=open('new1.txt','w')
# f=open('new2.txt','r')
# f=open('new3.txt','r')
# print(f.read())

# Method :- open()
#           readable()   
#           writeable()
#           closeable()
# f=open('n1.txt','x')
# f=open('n2.txt','x')
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed)
# print(f.writable())

# f=open("n1.txt","x")
# print(f.name)
# print(f.mode)
# print(f.encoding)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed)

# f=open("n1.txt","w+")
# print(f.name)
# print(f.mode)
# print(f.encoding)
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed)

#write
# f=open('n1.txt','w')
# f.write() #--->used for single string
# f.writelines() #--->used for multiple lines
# f.writable()

# f.write("hello, this is nishant malviya\n i am from bhopal")

# data=("thsi is python class","timming is 1:30 to 2:30")
# f.writelines(data)
# f.close()

#read()
# f=open('n1.txt','a')
# data=('hello\n','this is\n','nishant\n')
# f.writelines(data)
# print(f.readable())
# f1=open('n1.txt','r')
# data=f1.read()
# print(data)
# f1.close()
# f.close()

# f=open('n1.txt','a+')
# data=('hello a++\n','this is a++\n','nish a++\n')
# f.writelines(data)
# # print(f.readable())
# # f1=open('n1.txt','r')
# data=f.read()
# print(data)
# # f1.close()
# f.close()

# f=open('n1.txt','a')
# data=('hello\n','this is\n','nishant\n')
# f.writelines(data)
# print(f.readable())
# f1=open('n1.txt','r')
# data=f1.readlines()
# print(data)
# f1.close()
# f.close()
 
#tell()------>current positions and seek()----->curser moving for their requirement func

f=open('n1.txt','rb')
print(f.tell())
print(f.read(6))
print(f.tell())
# print(f.read(5))
f.seek(5,1)
print(f.tell())
print(f.read(10))
print(f.tell())
f.seek(-6,2)
print(f.read())

# seek(__,__)
#         |___0 -> defualt
#         |___1 ->
#         |___2 ->
# f=open('n10.txt','rb')
# data=("hello \n","im devanshu \n","full stack dev")
# f.writelines(data)
# print(f.tell())
# print(f.read(6))
# print(f.tell())
# print(f.seek(5,1))
# print(f.tell()) history
# print(f.read(10))
# print(f.tell())
# print(f.seek(-6,2))
# print(f.read())
# seek curser ko move krna li leya use krta hai
# tell curser ka current position check krna ki leya use hota ha