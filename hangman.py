import random

def get_a_word(wordlist="/usr/share/dict/words"): 
    good_words = []
    with open(wordlist) as f:
        words = [x.strip() for x in f]
        for word in words:
            if not word.islower(): 
                continue
            if not word.isalpha():
              continue
            if len(word) < 5:
              continue
            good_words.append(word)
    return random.choice(good_words)


   
def get_masked_word(word,gussed):
   sample = []
   for i in word:
     if i in gussed:
       sample.append(i)
     else:
       sample.append("-")
   return "".join(sample)
   

