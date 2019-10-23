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
#get the index of the word's first vowel (first_vowel)
def first_vowel(word):  
    #an empty list for saving the first vowel's index to
    first_vowel_index = []
    #iterate through the word with vowels list, saving the index of each occurence to the empty list
    for vowel in vowels:
        first_vowel_occurrence = word.find(vowel)
        if first_vowel_occurrence > 0:
            first_vowel_index.append(first_vowel_occurrence)
    #sort the list and point directly to the integer, the first and lowest index in the first_vowel_index list
    first_vowel_index = sorted(first_vowel_index)
    vowel_index = first_vowel_index[0]
    return vowel_index

#basic operation for translating words starting with a consonant
def basic_translation(word):
    #define the standard prefix and suffix, split at 1st occurrence of a vowel
    prefix = word[0:(first_vowel(word))]
    suffix = word[(first_vowel(word)):]
    new_word = (suffix + prefix + pyg)
    #add a special case to help pronunciation on leading "y"s (i.e. "bye" now = "eyebay" instead of "yebay")
    if new_word[0] == 'y':
        return ('e' + new_word)
    #add a special case to deal with words starting in "qu" (i.e. "quit" now = "itquay" instead of "uitqay")
    if word[0] == 'q' and word[1] == 'u':
        return (suffix[1:] + 'qu' + pyg)
    #if none of the above cases apply, simply return the "new_word"
    else:
        return(new_word)

#slap it all together to make the translated word
def assemble(word):
    #make sure the individual word is greater than zero and is either all alpha or only has an apostrophe for a contraction
    if len(word) > 0 and (word.isalpha() or is_contraction(word)):
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
            return basic_translation(word)
        #append standard suffix for words starting in a vowel (-y)
        elif word[0] in minus_y:
            vow_word = word + vow_pyg
            return(vow_word)
        else:
            return word
    else:
        return word

#define a case for dealing with contractions and their apostrophes
def is_contraction(string):
    if "'" in string:
        return True
    else:
        return False

#ask for and assign user input to a variable
user_input = input('Enter a word or sentence you\'d like translated: ')
#split the user input up into words you can iterate through, leaving punctuation unchanged
import re
ui_split = re.findall(r"[\w']+|[.,!?;:]", user_input)
#empty string to save translated words to
new_string = ''
#assemble each word, adding it (and a space before, if alpha or contraction) to the new string
for word in ui_split:
    if word.isalpha() or is_contraction(word):
        new_string += (' ') + (assemble(word))
    #no spaces added before non alpha or contractions
    else:
        new_string += (assemble(word))
#print the result, omitting the 1st character, which will just be the blank space before the alpha
print (new_string[1:])
