# 6.00 Problem Set 4
#
# Caesar Cipher Skeleton
#
import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print "  ", len(wordlist), "words loaded."
    return wordlist

wordlist = load_words()

def is_word(wordlist, word):
    """
    Determines if word is a valid word.

    wordlist: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordlist.

    Example:
    >>> is_word(wordlist, 'bat') returns
    True
    >>> is_word(wordlist, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in wordlist

def random_word(wordlist):
    """
    Returns a random word.

    wordlist: list of words  
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

def random_string(wordlist, n):
    """
    Returns a string containing n random words from wordlist

    wordlist: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([random_word(wordlist) for _ in range(n)])

def random_scrambled(wordlist, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordlist: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words


    NOTE:
    This function will ONLY work once you have completed your
    implementation of apply_shifts!
    """
    s = random_string(wordlist, n) + " "
    shifts = [(i, random.randint(0, 26)) for i in range(len(s)) if s[i-1] == ' ']
    return apply_shifts(s, shifts)[:-1]

def get_fable_string():
    """
    Returns a fable in encrypted text.
    """
    f = open("fable.txt", "r")
    fable = str(f.read())
    f.close()
    return fable


# (end of helper code)
# -----------------------------------

#
# Problem 1: Encryption
#
def build_coder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: -27 < int < 27
    returns: dict

    Example:
    >>> build_coder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)
    """
    ### TODO.

    start_dict_upper = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H',
                  'I': 'I', 'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P',
                  'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
                  'Y': 'Y', 'Z': 'Z', ' ': ' '}
    start_dict_lower = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e',
                  'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k', 'l': 'l', 'm': 'm',
                  'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u',
                  'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z', ' ' : ' '}
    cipher_dict_upper = {-26: 'A', -25: 'B', -24: 'C', -23: 'D', -22: 'E', -21: 'F', -20: 'G', -19: 'H',
                  -18: 'I', -17: 'J', -16: 'K', -15: 'L', -14: 'M', -13: 'N', -12: 'O', -11: 'P',
                  -10: 'Q', -9: 'R', -8: 'S', -7: 'T', -6: 'U', -5: 'V', -4: 'W', -3: 'X',
                  -2: 'Y', -1: 'Z', 0: ' '}
    cipher_dict_lower = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm',
                  14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u',
                  22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: ' '}
    new_dict = {}
    for number in cipher_dict_upper:
        shift_number = (number+shift)
##        print "number: ", number, "cipher_dict[number]: ", cipher_dict[number]
        if shift_number > 0:
            new_number = -27 + (shift+number)%27
##            print "number: ", number, "new_number: ", new_number
            new_dict.update({cipher_dict_upper[number]: cipher_dict_upper[new_number]})
        elif shift_number < -26 :
            new_number = 0 + shift_number%-27
##            print "shift: ", shift, "number: ", number, "shift%: ", ((shift_number)%-26)
##            print "new_number: ", new_number, "(shift+number): ", shift_number
            new_dict.update({cipher_dict_upper[number]: cipher_dict_upper[new_number]})
        else:
            new_dict.update({cipher_dict_upper[number]: cipher_dict_upper[number + shift]})
##        print new_dict
    for number in cipher_dict_lower:
        shift_number = (number+shift)
##        print "number: ", number, "cipher_dict[number]: ", cipher_dict_lower[number]
        if shift_number > 27:
            new_number = 0 + (shift+number)%27
##            print "number: ", number, "new_number: ", new_number
            new_dict.update({cipher_dict_lower[number]: cipher_dict_lower[new_number]})
        elif shift_number < 1 :
            new_number = 27 + shift_number%-27
##            print "shift: ", shift, "number: ", number, "shift%: ", ((shift_number)%-26)
##            print "new_number: ", new_number, "(shift+number): ", shift_number
            new_dict.update({cipher_dict_lower[number]: cipher_dict_lower[new_number]})
        else:
            new_dict.update({cipher_dict_lower[number]: cipher_dict_lower[number + shift]})
##        print new_dict
    return new_dict

def build_encoder(shift):
    """
    Returns a dict that can be used to encode a plain text. For example, you
    could encrypt the plain text by calling the following commands
    >>>encoder = build_encoder(shift)
    >>>encrypted_text = apply_coder(plain_text, encoder)
    
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_encoder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)

    HINT : Use build_coder.
    """
    ### TODO.
    return build_coder(shift)

def build_decoder(shift):
    """
    Returns a dict that can be used to decode an encrypted text. For example, you
    could decrypt an encrypted text by calling the following commands
    >>>encoder = build_encoder(shift)
    >>>encrypted_text = apply_coder(plain_text, encoder)
    >>>decrypted_text = apply_coder(plain_text, decoder)
    
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_decoder(3)
    {' ': 'x', 'A': 'Y', 'C': ' ', 'B': 'Z', 'E': 'B', 'D': 'A', 'G': 'D',
    'F': 'C', 'I': 'F', 'H': 'E', 'K': 'H', 'J': 'G', 'M': 'J', 'L': 'I',
    'O': 'L', 'N': 'K', 'Q': 'N', 'P': 'M', 'S': 'P', 'R': 'O', 'U': 'R',
    'T': 'Q', 'W': 'T', 'V': 'S', 'Y': 'V', 'X': 'U', 'Z': 'W', 'a': 'y',
    'c': ' ', 'b': 'z', 'e': 'b', 'd': 'a', 'g': 'd', 'f': 'c', 'i': 'f',
    'h': 'e', 'k': 'h', 'j': 'g', 'm': 'j', 'l': 'i', 'o': 'l', 'n': 'k',
    'q': 'n', 'p': 'm', 's': 'p', 'r': 'o', 'u': 'r', 't': 'q', 'w': 't',
    'v': 's', 'y': 'v', 'x': 'u', 'z': 'w'}
    (The order of the key-value pairs may be different.)

    HINT : Use build_coder.
    """
    ### TODO.
    return build_coder(-shift)
    
 

def apply_coder(text, encode_dict):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text

    Example:
    >>> apply_coder("Hello, world!", build_encoder(3))
    'Khoor,czruog!'
    >>> apply_coder("Khoor,czruog!", build_decoder(3))
    'Hello, world!'
    """
    ### TODO.
    new_string = ""
    for letter in range (0, len(text)):
##        print "letter: ", letter
##        print "text[letter]: ", text[letter]
##        print "encode_dict[text[letter]]:", encode_dict[text[letter]]
        if text[letter] not in encode_dict:
            new_string += text[letter]
        else:
            new_string += (encode_dict[text[letter]])
##    new_string = ''.join(new_string)
    return new_string
  

def apply_shift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. The empty space counts as the 27th letter of the alphabet,
    so spaces should be replaced by a lowercase letter as appropriate.
    Otherwise, lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.
    
    text: string to apply the shift to
    shift: amount to shift the text
    returns: text after being shifted by specified amount.

    Example:
    >>> apply_shift('This is a test.', 8)
    'Apq hq hiham a.'
    """
    ### TODO.
    return apply_coder(text, build_coder(shift))
   
#
# Problem 2: Codebreaking.
#
def find_best_shift(wordlist, text):
    """
    Decrypts the encoded text and returns the plaintext.

    text: string
    returns: 0 <= int 27

    Example:
    >>> s = apply_coder('Hello, world!', build_encoder(8))
    >>> s
    'Pmttw,hdwztl!'
    >>> find_best_shift(wordlist, s) returns
    8
    >>> apply_coder(s, build_decoder(8)) returns
    'Hello, world!'
    """
    ### TODO
    n = -27
    shift_dict = {}
    decode_string = ""
    word_count = 0
    ##Will go through each iteration of build_decoder. This will give each outcome
    ##After each iteration of shift, will detect how many words in decoded string
    ##For each word found, word_count will increase by 1
    ##Will add to dictionary, shift_dict, shift:word_count
    ##Will then return the value of the key assoc. with max value of dict.
    while n < 27:
##        print 'n: ', n
        n += 1
        decode_string = ''
        word = ''
        word_count = 0
        decode = apply_coder(text, build_decoder(n))
##        print 'decode: ', decode
        for x in decode:
            if x == ' ' or x == ',' or x == '.' or x == "!":
                decode_string += word
##                print 'decode_string: ', decode_string
                word = word.lower()
                if word in wordlist:
##                    print 'word: ', word
                    word_count +=1
##                    print 'word_count: ', word_count
                word = ''
            else:
                word += x

        shift_dict.update({n:word_count})
##        n += 1
##        print decode
##    print "shift_dict: ", shift_dict
    v = list(shift_dict.values())
    k = list(shift_dict.keys())
    return k[v.index(max(v))]
        
   
#
# Problem 3: Multi-level encryption.
#
def apply_shifts(text, shifts):
    """
    Applies a sequence of shifts to an input text.

    text: A string to apply the Ceasar shifts to 
    shifts: A list of tuples containing the location each shift should
    begin and the shift offset. Each tuple is of the form (location,
    shift) The shifts are layered: each one is applied from its
    starting position all the way through the end of the string.  
    returns: text after applying the shifts to the appropriate
    positions

    Example:
    >>> apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    """
    ### TODO.
    encode_string = ''
    location = [x[0] for x in shifts]
    n = 0
    for i in shifts:
        text = apply_coder(text, build_encoder(i[1]))
        if n+1 >= len(shifts):
            encode_string += text[location[n]:]
        else:
            encode_string += text[location[n]: location[n+1]]
        n += 1
    return encode_string
 
#
# Problem 4: Multi-level decryption.
#


def find_best_shifts(wordlist, text):
    """
    Given a scrambled string, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: Make use of the recursive function
    find_best_shifts_rec(wordlist, text, start)

    wordlist: list of words
    text: scrambled text to try to find the words for
    returns: list of tuples.  each tuple is (position in text, amount of shift)
    
    Examples:
    >>> s = random_scrambled(wordlist, 3)
    >>> s
    'eqorqukvqtbmultiform wyy ion'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> shifts
    [(0, 25), (11, 2), (21, 5)]
    >>> apply_shifts(s, shifts)
    'compositor multiform accents'
    >>> 
    >>> s
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> print apply_shifts(s, shifts)
    Do Androids Dream of Electric Sheep?    
    """
    return find_best_shifts_rec(wordlist, text, 0)

def find_best_shifts_rec(wordlist, text, start):
    """
    Given a scrambled string and a starting position from which
    to decode, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: You will find this function much easier to implement
    if you use recursion.

    wordlist: list of words
    text: scambled text to try to find the words for
    start: where to start looking at shifts
    returns: list of tuples.  each tuple is (position in text, amount of shift)
    """
    ### TODO.
    shifts = []
    shift = 0
    decode_text = text[:]
    next_word = ''
    word = ''
    start_orig = start
    check = True
    word_check = False
    while shift < 27:

        s = apply_coder(decode_text, build_decoder(shift))
##        print "shift#: ", shift
##        print "s: ", s

        ##Will start from shift 0 at beginning of text.
        ##Will add letters, until a space or special character is recognized, to a word that will be checked with is_word
        
        for x in s[start:]:
            word += x
##            print "word: ", word
##            print "s[start:] ", s[start:]
##            print "start: ", start
##            print "shift#: ", shift
            if x == ' ' or word == s[start:]:
##                print "s[start:]before is_word: ", s[start:]
##                print "checking is_word"
##                print "word: ", word

                ##If is_word will find location of word and append it to variable "shifts" with the shift value in tuple
                
                if is_word(wordlist, word):
##                    print "valid word: ", word
                    shifts.append((start, -shift))
                    start += len(word)
                    word = ''
                    if word == s[start:]:
                        shifts.append((start, -shift))
##                        print "Last word, returning shifts"
                        return shifts

                    ##Will change the "start" variable to the end of the word including the space and use that value for recursion
                    
                    
                    check = True
                    word_check = False
##                    print "start after is_word: ", start

                    ##This section checks if is one or more word(s) associated with the same shift value following initally found word
                    ##Will use new start position and check the next set of letters to see if word.
                    ##If another word is found, will only change "start" value which will be used for recursion
                    
                    while check == True:
##                        print "checking next word"
                        l = s[start:]
##                        print "l: ", l
                        for x in l:
                            next_word += x
                            if x == ' ' or next_word == l:
##                                print "x in newword: ", x
##                                print "newword: ", next_word
                                if is_word(wordlist, next_word):
##                                    print "valid newword: ", next_word
##                                    print "finding word: ", word, "@index", s.find(word[-1]) + 1
                                    start += len(next_word)
                                    if s[start:] == '':
                                        return shifts
                                    next_word = ''
                                ##If next word doesn't pass is_word. Will go through every shift at this start position
                                ##To make sure there is actually a word to be found. If a word isn't found at this position
                                ##Will continue through shift values at original location instead of new start position.
                                    
                                else:
##                                    print "Did not find word, will check if word"
                                    new_shift = 0
                                    while word_check == False:
##                                        print "checking all shifts"
##                                        print "new_shift: ", new_shift
                                        next_word = ''
                                        l = apply_coder(s[start:], build_decoder(new_shift))
##                                        print "l: ", l
                                        if new_shift == 28:
                                            break;
                                        for x in l:
                                            next_word += x
##                                            print "x: ", x
##                                            print "word: ", next_word
                                            if x == ' ' or next_word == l:
##                                                print "going to check word"
                                                if is_word(wordlist, next_word):
##                                                    print "found word in all shifts."
                                                    word_check = True
                                                    break;
                                                else:
                                                    break;
                                        new_shift += 1
                                    check = False
                                    break;
                    if word_check == False:
##                        print "will not use this shift, continuing shift"
                        shifts = []
                        start = start_orig
                        continue;
##                    print "going to try recursion now"
##                    print "shifts before appending: ", shifts
                    print "returning shifts: ", shifts
                    return shifts + find_best_shifts_rec(wordlist, s, start)
                else:
                    word = ''
                    break;
        shift += 1

                    



##test harness
s = random_scrambled(wordlist, 5)

def decrypt_fable():
     """
    Using the methods you created in this problem set,
    decrypt the fable given by the function get_fable_string().
    Once you decrypt the message, be sure to include as a comment
    at the end of this problem set how the fable relates to your
    education at MIT.

    returns: string - fable in plain text
    """
     
    ### TODO.
     apply_shifts(get_fable_string(), find_best_shifts(wordlist, get_fable_string()))
     
#What is the moral of the story?
#
#
#
#
#

