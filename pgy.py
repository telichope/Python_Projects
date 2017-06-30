pgy

pyg = 'ay'
original = raw_input('Enter a word:')
word=original.lower()
first=original[0]
new_word=word[1:len(word)]+first+pyg
if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'