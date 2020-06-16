#Project 10
#Jana Backman
#CIS 106

class Employee:
    def __init__(self, name, hours):
        self.name= name
        self.pay = 0
        self.hours = hours

    def get_name(self):
        return self.name

    def get_pay(self):
        return self.pay

    def get_hours(self):
        return self.hours

    def set_name(self, n):
        self.name= n

    def set_pay(self, p):
        self.pay = p

    def set_hours(self, h):
        self.hours = h

    def emppay(self):
        pay_rate= 80.00
        self.pay = self.hours * pay_rate

class Newemp(Employee):
    def __init__(self, name, hours):
        Employee.__init__(self, name, hours)
        self.pay_rate= 100

    def get_pay_rate(self):
        return self.pay_rate
    
    def set_pay_rate(self, pr):
        self.pay_rate = pr

    #overrides the super class method emppay()
    def emppay(self):
        self.pay = self.hours * self.pay_rate
        

    

#main()

#input
name= input("Enter empleyee name: ")
hours= int(input("Enter hours worked: "))
Emp = Newemp(name, hours)

#process
Emp.emppay()
#output
print ("Name:", Emp.get_name())
print ("Hours:", format (Emp.get_hours(),".2f"))
print ("Payment: %.2f" %Emp.get_pay())

    
