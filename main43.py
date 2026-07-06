#Printing using diamond pattern
rowsize = int(input("Enter the number of rows: "))
if rowsize%2 == 0:
   halfdiamrow = int(rowsize/2)
else:
   halfdiamrow = int((rowsize+1)/2)
space = halfdiamrow - 1

for i in range(1, halfdiamrow+1):
    for j in range(1, space+1):
       print(" ", end="")
    space = space - 1
    number = 1
    for j in range(1, 2*i):
        print(number, end="")
        number = number +1
    print()
space = 1
for i in range(1, halfdiamrow):
    for j in range(1, space+1):
      print(" ",end="")
    space = space +1    
    number = 1
    for j in range(1, 2*(halfdiamrow-i)):
      print(number, end="")
      number = number+1
    print()
