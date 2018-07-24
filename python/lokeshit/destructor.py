class x:
    def __init__(self):
        print("in constructor of x")
    def m1(self):
        print("in m1 of x")
    def __del__(self):
        print("in destructor of x")
x().m1()
x1=x()
print(x1)
x1.m1()
x1=x()
print(x1)
x1.m1()
