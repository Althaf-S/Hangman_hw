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
  
def test_wrong_guess_masked_word():
  guessed = ['u']
  word = "aeroplane"
  masked_word = hangman.get_masked_word(word,guessed)
  assert masked_word == "---------"
  
def test_two_correct_guess_masked_word():
  word = "aeroplane"
  gussed = ['r','p']
  masked_word = hangman.get_masked_word(word,gussed)
  assert masked_word == "--r-p----"
  
def test_single_word_multiple_occurence_masked_word():
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
    assert gussed == "caje"
    assert attempts_left == 20
  
def test_repeating_same_entry():
   secret_word = "aeroplane"
   gussed = ["h","k"]
   guess = "h"
   attempts_left = 5
   
   gussed, attempts_left, action = hangman.game_play(secret_word, gussed, guess, attempts_left) 
   
   assert gussed == ["h","k"]
   assert attempts_left == 5
   assert action == 'next'
  
def test_correct_guess_game_not_over():
   secret_word = "aeroplane"
   gussed = []
   guess = "a"
   attempts_left = 5
   
   gussed, attempts_left, action = hangman.game_play(secret_word, gussed, guess, attempts_left)
  
   assert gussed == ['a']
   assert attempts_left == 5 
   assert action == "next"
   
def test_wrong_guess():
   secret_word = "aeroplane"
   gussed = ["x"]
   guess = "j"
   attempts_left = 5
   
   gussed, attempts_left, action = hangman.game_play(secret_word, gussed, guess, attempts_left)
   
   assert gussed == ["x","j"]
   assert attempts_left == 4
   assert action == "next"
   
def test_guess_game_over():
   secret_word = "plane"
   gussed = ["a","e","r","o","l","a","n","e"]
   guess = "p"
   attempts_left = 1
   
   gussed, attempts_left, action = hangman.game_play(secret_word, gussed, guess, attempts_left)
     
   assert action == "game won"   
   
def test_wrong_guess_game_over():
   secret_word = "aeroplane"
   gussed = ["x"]
   guess = "j"
   attempts_left = 1
   
   gussed, attempts_left, action = hangman.game_play(secret_word, gussed, guess, attempts_left)
   
  
   assert action == "game over"
    
   
   


    

    


  
  

