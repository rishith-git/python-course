#Creating a mirrored right angle triangle

rows = 5
for i in range(1,rows + 1):
 print(" " * (rows - i) + "*" * i)
rows = 5
for j in range(rows-1, 0, -1):
 print(" " * (rows - j) + "*" * j)