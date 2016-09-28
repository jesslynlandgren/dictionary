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

for key, value in wordDict.items():
    print "{0}:  {1}".format(key, value)

f.close()
