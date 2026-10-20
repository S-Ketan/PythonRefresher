x=input("Enter number 1: ")
y=input("Enter number 2: ")

try:
    z=int(x)/int(y)
    print(z)
except ZeroDivisionError:
    z=None
    print("Division by 0 not Possible")
except TypeError:
    z=None
    print("Both Numbers should be integers")
