##Pseudocode for Deleting Vowels:
"""This is the pseudocode for deleting vowels, from any given string"""
    
##vowels<- LIST "a", "A", "e", "E", "i", "I", "o", "O", "u", "U"
##word_no_vowels<-""

## delete_vowels(w)
##   IF w = ""

##      FUNCTIONpass
##   ELSE IF W[0] IN VOWELS
##      delete_vowels(w[1:])
##   ELSE
##      word_no_vowels<-word_no_vowels+w[0]
##      delete_vowels(w[1:])
##delete_vowels("hello")
##PRINT word_no_vowels


vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
word_without_vowels = ""

def delete_vowels(w):
    global word_without_vowels
    if w == "":
        pass
        #if the word is empty
    elif w[0] in vowels:
        delete_vowels(w[1:])
        #checks the first element of the word, if it contains any elements in vowels                   
    else:
        word_without_vowels += str(w[0])
        delete_vowels(w[1:])
        #rest of the word continues and is put in a string and is then called back
delete_vowels("hello")
print(word_without_vowels)



