import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("value error")
    sys.exit(1)

try:
    result = x/y
except ZeroDivisionError:
    print("error")
    sys.exit(1)
print(result)