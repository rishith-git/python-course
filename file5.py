list = [8,11,9,10,15,20]

print("original list is : ", list)
count = 0
for i in list:
 count += i
print("sum of all the elements in the list is : ", count)

average = count / len(list)
print("The average of all the elements in the list is : ", average)

list.sort()
print("The smallest number in the list is : ", list[0])
print("The largest number in the list is : ", list[-1])