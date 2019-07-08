#ask for and assign user input to a variable
word = input('Enter a word you\'d like translated: ')
#define some constants for the rest of the program, vowels and the universal suffix
vowels = ['a','e','i','o','u', 'y', 'A', 'E', 'I', 'O', 'U']
pyg = 'ay'
#an empty list for saving the first vowel's index to when iterating through the word
fvIndex = []

#make sure the user input is alpha and greater than zero
if len(word) > 0 and word.isalpha():
    #iterate through the word with our vowels, saving the index of the first occurence to the empty list
    for vowel in vowels:
        fvOccurance = word.find(vowel)
        if fvOccurance > 0:
            fvIndex.append(fvOccurance)
    #sort the list and point directly to the integer, the first and lowest index in the fvIndex list
    fvIndex = sorted(fvIndex)
    vowelIndex = fvIndex[0]
    #slap it all together to make the translated word
    prefix = word[0:vowelIndex]
    vSuffix = word[vowelIndex:]
    new_word = vSuffix + prefix + pyg
    #print (new_word)

else:
    print ('whoops')

print ("fvIndex:  " + str(fvIndex))
print ("vSuffix:  " + vSuffix)
print ("prefix:   " + prefix)
print ("pyg:      " + pyg)
print ("new_word  " + new_word)
