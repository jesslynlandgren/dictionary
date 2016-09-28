import operator

f = open('programmers_blues.txt')
txt = f.read()
txt = txt.replace('.', '').replace('(', '').replace(')', '')

words = txt.split()
wordDict = {}

for word in words:
    if word not in wordDict:
        wordDict[word] = 1
    else:
        wordDict[word] += 1

sortWords = sorted(wordDict.items(), reverse = True, key=lambda x: x[1])
print sortWords

for i in range(10):
    print sortWords[i][0]

f.close()
