

class AnagramChecker:
  def __init__(self, ) :
    self.words = '' 
    with open("sowpods.txt", "r") as f:
       self.words = f.readlines()
    lastword = self.words[-1]
    self.words = [self.words[i][:-1] for i in range(len(self.words)-1)] + [lastword]
  def is_valid_word(self,word):
    if word in self.words:
      return True
    return False

  def get_anagrams(self,word):
    word_list = sorted(word)
    anagrams = []
    for item in self.words:
      if word_list == sorted(item):
        anagrams.append(item)
    if word in anagrams:
      anagrams.pop(anagrams.index(word))
    return anagrams

    
  def is_anagram(self,word1, word2):
    if sorted(word1) == sorted(word2):
        return False
    return True

a = AnagramChecker()
word = 'bonjou'
word_dict = {str(i):word[i]for i in range(len(word))}
copie = word_dict.copy()
print(a.get_anagrams('ZYZZYVAS'))