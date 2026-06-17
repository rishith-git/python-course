a = 15
b = 6
c = 0

if a and b and c:
   print("All the numbers havng boolean values as True")
else:
   print("All the numbers not having boolean values as True")

a = 10
b = 6
c = 0

if a or b and c:
   print("either a or b having boolean values as True")
else:
   print("c not having boolean values as True")

a = 15
b = 10
c = 0

if a and b or c:
   print("a and b having boolean values as True")
else:
   print("All the numbers not having boolean values as False")

a = 26
b = 6
c = 10

if not a or b and c:
   print("All the numbers having boolean values as True")
else:
   print("All the values not having boolean values as False")