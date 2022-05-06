list1 = [5, 10, 15, 20, 25, 50, 20]

print(list1)
index = list1.index(20)
list1.pop(index)
list1.insert(index, 200)
print(list1)

aTuple = (10, 20, 30, 40)

a, *b = aTuple
print(a)
print(b)
sentence = input('enter a sentence: ')
words = sentence.split()
words.reverse()
sentence_r = ' '.join(words)
print(sentence_r)

#write down your logic here

#

print(reversed)
