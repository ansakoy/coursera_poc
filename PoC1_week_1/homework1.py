# POC 1, Week 0
# Homework

'''
1.
For the first question in this assignment, enter the type of the Python expression 3.14159 below.
Remember that capitalization is important.
'''
# float

'''
2.
An if statement can have how many elif parts?
'''
# Unlimited, i.e., 0 or more

'''
3.
Consider the following Python code snippet:
'''
def clock_helper(total_seconds):
    """
    Helper function for a clock
    """
    seconds_in_minute = total_seconds % 60
# 30

'''
4.
In Python, what character always appears at the end of the line before the start of an indented
block of code?
'''
# Nothing

'''
5.
Which of the following expressions returns the last character in the non-empty string my_string?
'''
# my_string[-1]

'''
6.
What is the primary difference between a list and a tuple?
'''
# Lists are mutable. Tuples are immutable.

'''
7.
Consider the following snippet of Python code. What is the value of val2[1] after executing this code?
'''
val1 = [1, 2, 3]
val2 = val1[1:]
val1[2] = 4
# 3

'''
8.
Which of the following Python expressions is a valid key in a Python dictionary?

'''
# 0
# ""
# False

'''
9.
Write a function in Python that takes a list as input and repeatedly appends the sum of the
last three elements of the list to the end of the list. Your function should loop for 25 times.
'''

def appendsums(lst):
    """
    Repeatedly append the sum of the current last three elements
    of lst to lst.
    """
    for dummy_x in xrange(25):
        sum_last_three = sum(lst[-3:])
        lst.append(sum_last_three)
    return lst

'''
If your function works correctly, the following code should print 230:
'''
# sum_three = [0, 1, 2]
# appendsums(sum_three)
# print sum_three[10]
'''
Enter the value of sum_three [20] below.
'''
# 101902

'''
10.
First, complete the following class definition:
'''


class BankAccount:
    """ Class definition modeling the behavior of a simple bank account """

    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self._balance = 0
        self._fee = 0
        self._balance += initial_balance

    def deposit(self, amount):
        """Deposits the amount into the account."""
        self._balance += amount

    def withdraw(self, amount):
        """
        Withdraws the amount from the account. Each withdrawal resulting
        in a negative balance also deducts a penalty fee of 5 dollars
        from the balance.
        """
        self._balance -= amount
        if self._balance < 0:
            self._fee += 5
            self._balance -= 5

    def get_balance(self):
        """Returns the current balance in the account."""
        return self._balance

    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self._fee

# my_account = BankAccount(10)
# my_account.withdraw(15)
# my_account.deposit(20)
# print my_account.get_balance(), my_account.get_fees()

my_account = BankAccount(10)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(20)
my_account.withdraw(5)
my_account.deposit(10)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(30)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(50)
my_account.deposit(30)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25)
my_account.withdraw(10)
my_account.deposit(20)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
print my_account.get_balance(), my_account.get_fees()

# -60 75