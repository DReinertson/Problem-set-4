# Problem-set-4
Caesar Shift
Includes:
  - PDF file with instructions for problem set. 
  - ps4.py file with my solution to the problem set
  - .txt file that contains list of words used to check if word is valid.
  
  *.py files may contain "helper code" section. Work that I completed will be outside the helper code section*

Ultimate goal is to decipher the end text given by professor. Two dicts are created, one for upper-case and lower-case. Will shift the text, check for a space, concatenate all the letters before found space and check to see if it is a valid word using is_word. This is where my code deviates from the pseudo. 
Psuedo code:
  Once word is found, store word in a sentence, shift everything after that word(space included) starting from shift 0 at that index. 
My code: 
  Once word is found, store shift value, shift text after that word(space included) and make sure there is actually a word at this index. If there isn't a word following original word, continue to shift in original index (before the word was found) and continue until a word is found. 
  Essentially this is an error check to ensure that you're not finding a word that happens to occur in a shift that doesn't produce the rest of the text correctly. 
