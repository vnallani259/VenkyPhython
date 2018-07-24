class cust:
    """cust app"""
    cbname="sbi"
    def __init__(self,cname,cadd,cacno,cbal):
        self.cname=cname
        self.cadd=cadd
        self.cacno=cacno
        self.cbal=cabl
    def deposite(self,damt):
        self.cbal=self.cbal+damt
    def withdraw(self,wamt):
        self.cbal=self.cbal-wamt
    def display(self):
        print(self.cname)
        print(self.cadd)
        print(self.cacno)
        print(self.cbal)
        print(self.cbname)
c1=cust("venky","muppalla",1001,100000.00)
print(c1)
c1.deposite(40000.00)
c1.withdraw(20000.00)
c1.display()

        
        
