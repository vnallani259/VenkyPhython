class Test:
    def __init__(self):
        self.a=1000
        self.b=2000
    def display(self):
        print(self.a)
        print(self.b)
        
t1=Test()
t1.display()
del t1.b
print(t1.a)
#print(t2.b)
t2=Test()
print(t2.a)
print(t2.b)


