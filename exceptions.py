
x=2
try:
    print(x/0)
except NameError:
    print("Something is not defined")
except ZeroDivisionError:
    print("You cannot divide by zero")
else:
    print("no errors")