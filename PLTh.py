#define some constants for the rest of the program, vowels, silent 'h's, and the universal suffix (w or w/o starting letter as vowel)
vowels = ['a','e','i','o','u','y','A','E','I','O','U','Y']
minus_y = ['a','e','i','o','u','A','E','I','O','U']
#standard suffix
pyg = 'ay'
#suffix for words starting in vowels (minus_y)
vow_pyg = 'yay'
#list of silent 'h' words
from silent_h_list import silent_h

#functions used for assembling the translated words
#get the index of the word's first vowel (fv)
def fv(word):  
    #an empty list for saving the first vowel's index to
    fv_index = []
    #iterate through the word with vowels list, saving the index of each occurence to the empty list
    for vowel in vowels:
        fv_occurrence = word.find(vowel)
        if fv_occurrence > 0:
            fv_index.append(fv_occurrence)
    #sort the list and point directly to the integer, the first and lowest index in the fv_index list
    fv_index = sorted(fv_index)
    vowel_index = fv_index[0]
    return vowel_index

#basic operation for translating words starting with a consonant
def basic(word):
    #define the standard prefix and suffix, split at 1st occurrence of a vowel
    prefix = word[0:(fv(word))]
    v_suffix = word[(fv(word)):]
    new_word = (v_suffix + prefix + pyg)
    #add a special case to help pronunciation on leading "y"s (i.e. "bye" now = "eyebay" instead of "yebay")
    if new_word[0] == 'y':
        return ('e' + new_word)
    #add a special case to deal with words starting in "qu" (i.e. "quit" now = "itquay" instead of "uitqay")
    if word[0] == 'q' and word[1] == 'u':
        return (v_suffix[1:] + 'qu' + pyg)
    #if none of the above cases apply, simply return the "new_word"
    else:
        return(new_word)

#slap it all together to make the translated word
def assemble(word):
    #make sure the individual word is greater than zero and is either all alpha or only has an apostrophe for a contraction
    if len(word) > 0 and (word.isalpha() or cont_true(word)):
        #proceed as normal assuming word starts with a consonant
        #lowercase it all for consistency and readability
        word = word.lower()
        #treat silent first letter 'h' words as you would if the first letter was a vowel
        if word in silent_h:
            sh_word = word +vow_pyg
            return(sh_word)
        #fix vowel first words ending in 'y'from having an awkward 'yy' in  the middle
        elif word[0] in minus_y and word[-1] == 'y':
            return(word + pyg)
        #return the 'word' unaltered if it is not > 0, or either alpha or a contraction
        elif word[0] not in minus_y:
            return basic(word)
        #append standard suffix for words starting in a vowel (-y)
        elif word[0] in minus_y:
            vow_word = word + vow_pyg
            return(vow_word)
        else:
            return word
    else:
        return word

#define a case for dealing with contractions and their apostrophes
def cont_true(string):
    if "'" in string:
        return True
    else:
        return False

#ask for and assign user input to a variable
userInput = input('Enter a word or sentence you\'d like translated: ')
#split the user input up into words you can iterate through, leaving punctuation unchanged
import re
ui_split = re.findall(r"[\w']+|[.,!?;:]", userInput)
#empty string to save translated words to
new_string = ''
#assemble each word, adding it (and a space before, if alpha or contraction) to the new string
for word in ui_split:
    if word.isalpha() or cont_true(word):
        new_string += (' ') + (assemble(word))
    #no spaces added before non alpha or contractions
    else:
        new_string += (assemble(word))
#print the result, omitting the 1st character, which will just be the blank space before the alpha
print (new_string[1:])
