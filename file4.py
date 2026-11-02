def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    return ctr, lst

print("List of words to check : ['abc', 'bob', 'lol', 'xyz', 'pop']")
ctr, lst = match_words(['abc', 'bob', 'lol', 'xyz', 'pop'])
print("Number of words that match the condition are : ",ctr)
print("List of words that match the condition are : ",lst)
