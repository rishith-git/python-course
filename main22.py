#Using is operator

x = 5
if type(x) is int :
    print("True")
else :
    print("False")

y = 6.6
if type(y) is not float :
    print("True")
else :
    print("False")

x = 15
y = 15

if x == y :
    print("x is equal to y")

if x is y :
    print("x is y")