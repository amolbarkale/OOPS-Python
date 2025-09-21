# creating class

class Students:
    college =  "Apna College"
    name = "anonymous" # class attr

    def __init__(self, name, marks): # obj attr > class attr
        self.name = name
        self.marks = marks
        # print('self:', self)

    def welcome(self):
        print('Welcome -', self.name)

    # name= "Amol S Barkale"
    
# creating object (instance)

s1 = Students("Amol S Barkale", 97)

s2 = Students("Amol", 79)

# print('s1:', s1.name)
# print('s2:', s2.name)
# print('Students:', Students.college)
# print('Method:', s1.welcome())

#  _____________________________________________________________________

# Q1] Create student cass that takes name and marks of 3 sbjects as argumetns in constructor.
# tHen create a method to print the average

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        sum = 0
        for val in self.marks:
            sum += val

        print(f"Your avg is", sum/len(self.marks))
    
    @staticmethod
    def hello():
        print('hello:')
    
student = Student("AmolSB", [35,36,37])

student.calculate_average()

# print('student.name:', student.name)

student.name = "Nakul"

# print('student.name:', student.name)
# student.hello()

#  _____________________________________________________________________
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print('car started...')

# car1 = Car()
# car1.start()

#  _____________________________________________________________________

# Q2] Create Account class with 2 attributes - balance and account number
# Create methods for debit, credit and printing the balance

class Account:
    def __init__(self, balance, acc_numebr):
        self.balance = balance
        self.acc_numebr = acc_numebr
    
    def debit_amt(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debits")
        print("Total balance.", self.check_balance())

    
    def credit_amt(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credites")
        print("Total balance.", self.check_balance())


    
    def check_balance(self):
        return self.balance
        

acc1 = Account(10000, 123)
acc1.credit_amt(5000)
acc1.credit_amt(5000)
acc1.credit_amt(5000)
acc1.debit_amt(2000)


