import os

import hangman

def test_random_word_lowercase():
   fname = "/tmp/sample_wordlist"
   with open(fname, "w") as f:
       f.writelines(["Grape\n", "apple\n", "Mango\n"])
        
   for _ in range(100):
       assert hangman.get_a_word(fname) == "apple"

   os.unlink(fname)
    
def test_random_word_isalphabet():
  fname = "/tmp/simple_wordlist"
  with open(fname,"w") as f:
    f.writelines(["Grape's\n", "mang-oes\n", "apple\n"])
    
  for _ in range(100):
    assert hangman.get_a_word(fname) == "apple"
    
  os.unlink(fname)
  
def test_random_word_length():
  fname = "/tmp/simplewords"
  with open(fname,"w") as f:
    f.writelines(["Grape\n", "apple\n", "mang-o's\n", "he\n", "she\n"])
    
  for _ in range(100):
    assert hangman.get_a_word(fname) == "apple"
    
  os.unlink(fname)
  
def test_no_guess_masked_word():
  word = "aeroplane"
  gussed = []
  masked_word = hangman.get_masked_word(word,gussed)
  assert masked_word == "---------"
  
def test_one_correct_guess_masked_word():
  sample = ['r']
  word = "aeroplane"
  masked_word = hangman.get_masked_word(word,sample)
  assert masked_word == "--r------"
  
def test_wrong_guess():
  guessed = ['u']
  word = "aeroplane"
  masked_word = hangman.get_masked_word(word,guessed)
  assert masked_word == "---------"
  
def test_two_correct_guess():
  word = "aeroplane"
  gussed = ['r','p']
  masked_word = hangman.get_masked_word(word,gussed)
  assert masked_word == "--r-p----"
  
def test_single_word_multiple_occurence():
  word = "aeroplane"
  gussed = ['a','e','o','n']
  masked_word = hangman.get_masked_word(word,gussed)
  assert masked_word == "ae-o--ane"

def test_get_status():
    secret_word = "aeroplane"
    gussed = ["c","a","j","e"]
    attempts_left = 20
    
    masked_word, gussed, attempts_left = hangman.get_status(secret_word, attempts_left, gussed)
    
    assert masked_word == "ae----a-e"
    assert gussed == "c,a,j,e"
    assert attempts_left == 20
  


    

    


  
  

