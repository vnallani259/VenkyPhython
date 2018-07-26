class Test:
    def __init__(self):
        self.a=1000
        self.b=2000
    def display(self):
        print(self.a)
        print(self.b)
        
t1=Test()
t1.display()
t1.c=3000
print(t1.a)
print(t1.b)
print(t1.c)
t2=Test()
t2.c=4000
print(t2.a)
print(t2.b)
print(t2.c)
t3=Test()
print(t3.a)
print(t3.b)
print(t3.c)
