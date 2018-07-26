class test:
    a=1000
    b=2000
    def display(self):
        print(test.a)
        print(test.b)
print(test.a)
print(test.b)
del test.b
t1=test()
t1.display()
