import json
data = open("data.json", "r")
words = json.load(data)

word = input("enter a word: ")

if word in words:
    result = words[word]
    print(result)
elif word.title() in words:
    result = words[word.title()]
    print(result)
elif word.upper() in words:
    result = words[word.upper()]
    print(result)
elif word.upper() not in words:
    result = words[word.lower()]
    print(result)
else:
    print("Not exist")
