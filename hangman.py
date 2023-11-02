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

def masking_the_word(wrd = get_a_word()):        
   x = ""
   for _ in range(len(wrd)):
      x += "-"
   return x

get_a_word()
print(masking_the_word())
