#define some constants for the rest of the program, vowels and the universal suffix (w or w/o starting letter as vowel)
vowels = ['a','e','i','o','u','y','A','E','I','O','U','Y']
minusY = ['a','e','i','o','u','A','E','I','O','U']
#standard suffix
pyg = 'ay'
#suffix for words starting in vowels (minusY), add alternates "ay" and "way" later
vowPyg = 'yay'

#define the functions used throughout translation, pull out more as needed for horizontal compression/simplification
#get the index of the first vowel (fv) in a word
def fv(word):  
    #an empty list for saving the first vowel's index to when iterating through the word
    fvIndex = []
    #iterate through the word with our vowels, saving the index of each occurence to the empty list
    for vowel in vowels:
        fvOccurrence = word.find(vowel)
        if fvOccurrence > 0:
            fvIndex.append(fvOccurrence)
    #sort the list and point directly to the integer, the first and lowest index in the fvIndex list
    fvIndex = sorted(fvIndex)
    vowelIndex = fvIndex[0]
    return vowelIndex

#basic operation for translating word starting with a consonant
def basic(word):
    #define the standard prefix and suffix, split at 1st occurrence of a vowel
    prefix = word[0:(fv(word))]
    vSuffix = word[(fv(word)):]
    new_word = vSuffix + prefix + pyg
    #add a special case to help pronunciation on leading "y"s (i.e. "bye" now = "eyebay" instead of "yebay")
    if vSuffix == 'ye':
        return('eye' + prefix + pyg)
    #if none of the above cases apply, siimpy return the "new_word"
    else:
        return(new_word)

#slap it all together to make the translated word
def assemble(word):
    #make sure the individual word is greater than zero and is either alpha or a contraction
    if len(word) > 0 and (word.isalpha() or cont_true(word)):
        #proceed as normal assuming world starts with a consonant
        if word[0] not in minusY:
            return basic(word)
        #append standard suffix for words starting in a vowel (-y)
        elif word[0] in minusY:
            vow_word = word + vowPyg
            return(vow_word)
        #return the word unaltered if it is not alpha or is not > 0
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
UIsplit = re.findall(r"[\w']+|[.,!?;:]", userInput)
#empty string to save translated words to
new_string = ''
#assemble each word, adding it (and a space before, if alpha or contraction) to the new string
for word in UIsplit:
    if word.isalpha() or cont_true(word):
        new_string += (' ') + (assemble(word))
    #no spaces added before non alpha or contraction
    else:
        new_string += (assemble(word))
#print the result, ommitting the 1st character, which will just be blank space before the alpha
print (new_string[1:])


debug = False
if debug:
    print ("fvIndex:  " + (fvIndex))
    print ("vSuffix:  " + vSuffix)
    print ("prefix:   " + prefix)
    print ("pyg:      " + pyg)
    print ("new_word  " + new_word)