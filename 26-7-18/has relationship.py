class x:
    a=1000
    def __init__(self):
        self.b=2000
    def m1(self):
        print("in m1 of x")
    
class y:
    c=3000
    def __init__(self):
        self.d=4000
    def m2(self):
        print("in m2 of y")
    def display(self):
        print(y.c)
        print(self.d)
        self.m2()
        print(x.a)
        x1=x()
        print(x1.b)
        x1.m1()
        
y1=y()
y1.display()
