def isWordValid(phrase):
    """
    input: a list of strings, groups of alpha characters
    output: False if any string is repeated in the phrase; True otherwise
    """
    checker = []
    for i in phrase:
        if i in checker:
            return False #rule out the phrase if it contains a duplicate string
        elif not i.isalpha():
            return False #rule out the phrase if it contains anything but alpha characters
        checker.append(i)
#    print(phrase, 'is valid')
    return True

def phraseConverter(string):
    """
    input: a string of characters delineated by ' '
    output: a list of strings, split on the ' '
    """
    return string.split(' ')

f = open('sethday4input.txt', 'r')
phrases = f.read()
phrases = phrases.split('\n')
if phrases[-1] == '': #this gets rid of the final line break. there's probably a better way to do this
    del(phrases[-1])

counterValid = 0 #this is my answer for a, the number of valid passphrases

for line in phrases:
    if isWordValid(phraseConverter(line)):
        counterValid += 1

print('number of valid pass phrases for solution a is', counterValid)

"""
part b
"""

def getDict(word):
    """
    input: a string
    output: a dictionary of (character : frequency)
    """
    d = {}
    for i in word:
        d.setdefault(i, 0)
        d[i] += 1
    return d

def hasNotAnagram(l):
    """
    input: a list of strings
    output: False if a string is an anagram of any other string
    """
    dictList = [] #a list of dictionaries for words in our phrase
    for s in l:
        wordDict = getDict(s)
        print(wordDict)
        if wordDict in dictList:
            return False #reject the phrase if a word's dictionary matches another's
        else:
           dictList.append(getDict(s))
           print(dictList)
    return True

counterAnagram = 0 #this in my answer for part b

for line in phrases:
    if hasNotAnagram(phraseConverter(line)):
        counterAnagram += 1
        
print('number of valid phrases for solution b is', counterAnagram)
        
    