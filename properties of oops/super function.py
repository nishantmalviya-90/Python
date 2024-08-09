class A:
    def display(self):
        print("This is from class A")

class B(A):
    def display(self):
        print("This is from class B")
    def show(self):
        super().display()

obj=B()
obj.display()
obj.show()                   