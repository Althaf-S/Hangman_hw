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
   
def get_status(secret_word, attempts_left, gussed):
   masked_word = get_masked_word(secret_word, gussed)
   gussed = ",".join(gussed)
   return masked_word, gussed, attempts_left
   
def game_play(secret_word, gussed, guess, attempts_left):
   if guess in gussed:
     return gussed, attempts_left, "next"
   gussed.append(guess)
   if guess not in secret_word:
      attempts_left -= 1 
   return gussed, attempts_left, "next"
      
   
   


