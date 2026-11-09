test_dict = {"Codingal": 2, "Is": 2, "The": 2, "Best": 2, "For": 2, "Coding": 1}

print("The original dictionary is:", test_dict)

K = 2

res = 0

for key in test_dict:
    if test_dict[key] == K:
        res += 1


print("The number of keys with value", K, "is:", res)