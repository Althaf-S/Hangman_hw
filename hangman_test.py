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
    f.writelines(["Grape's\n", "Mang-oes\n", "apple"])
    
  for _ in range(100):
    assert hangman.get_a_word(fname) == "apple"
    
  os.unlink(fname)


  
  

