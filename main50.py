#Calculating the cube number upon a condition

def cube(num):
    return num * num * num
def by_three(num):
    if num % 3 == 0:
         print(cube(num))
    else:
        print(False)

by_three(6)
by_three(7)
