#Using Membership operator

print("Enter the marks of 5 subjects")

markone = int(input())
marktwo = int(input())
markthree = int(input())
markfour = int(input())
markfive = int(input())

total = markone + marktwo + markthree + markfour + markfive
average = int(total / 5)
print(average)

if average not in range (0,101) :
    print("Input is not valid")
elif average in range (91,101) :
    print("You have secured A1 Rank")
elif average in range (81,90) :
    print("You have secured A2 Rank")
elif average in range (71,80) :
    print("You have secured B1 Rank")
elif average in range (61,70) :
    print("You have secured B2 Rank")
elif average in range (51,60) :
    print("You have secured C1 Rank")
elif average in range (41,50) :
    print("You have secured C2 Rank")
elif average in range (31,40) :
    print("You have secured D1 rank")
elif average in range (21,30) :
    print("You have secured D2 Rank")
elif average in range (11,20) :
    print("You have secured E1 Rank")
elif average in range (0,10) :
    print("You have secured E2 Rank")