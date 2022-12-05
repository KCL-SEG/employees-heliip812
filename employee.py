"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def contract(self, type, salary, hours):
        self.contract =type
        self.salary = salary
        self.hours = hours

    def commission(self, type, bonus, noOfContract):
        self.commission=type
        self.bonus=bonus
        self.noOfContract=noOfContract


    def get_pay(self):
        if self.contract == 'monthly':
            pay=self.salary
        else:
            pay=self.salary*self.hours
        if self.commission == 'contract':
            pay = pay+ self.bonus * self.noOfContract
        elif self.commission =='fix':
            pay = pay+self.bonus
        return pay

    def __str__(self):
        txt = self.name + ' works on a '
        if self.contract == 'monthly':
            txt += 'monthly salary of '+str(self.salary)
        else:
            txt += 'contract of '+str(self.hours)+ ' hours at '+str(self.salary)+'/hour'
        
        if self.commission == 'contract':
                txt += ' and receives a commission for ' + str(self.noOfContract) + ' contract(s) at ' + str(self.bonus) + '/contract.'
        elif self.commission == 'fix':
            txt += ' and receives a bonus commission of ' + str(self.bonus) + '.'
        else:
            txt += '.'
        txt += '  Their total pay is ' + str(self.get_pay()) + '.'
        return txt


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.contract('monthly', 4000, 0)
billie.commission('NONE', 0, 0)
billie.get_pay()
print (str (billie))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.contract('hourly', 25, 100)
charlie.commission('NONE', 0, 0)
charlie.get_pay()
print (str (charlie))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.contract('monthly', 3000, 0)
renee.commission('contract', 200, 4)
renee.get_pay()
print (str (renee))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')
jan.contract('hourly', 25, 150)
jan.commission('contract', 220, 3)
jan.get_pay()
print (str (jan))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')
robbie.contract('monthly', 2000, 0)
robbie.commission('fix', 1500, 0)
robbie.get_pay()
print (str (robbie))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
ariel.contract('hourly', 30, 120)
ariel.commission('fix', 600, 0)
print (str (ariel))


# # Billie works on a monthly salary of 4000.  Their total pay is 4000.
# billie = Employee('Billie')

# # Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
# charlie = Employee('Charlie')

# # Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
# renee = Employee('Renee')

# # Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
# jan = Employee('Jan')

# # Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
# robbie = Employee('Robbie')

# # Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
# ariel = Employee('Ariel')
