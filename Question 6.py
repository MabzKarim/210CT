##Pseudocode for Reversing Words:
"""This is the pseudocode to reverse any given string"""

## words_reversed(r)
## if LEN(var)(r) = 0
##      RETURN("")
## ELSE
##      RETURN words_reversed(r[1:]) + (r[0]) + (" ")
## sentence <-INPUT "enter something you want to see in reverse:"
## words <-split(sentence, " ")
## PRINT words_reversed(words)

def words_reversed(r):                                                          #1
    """this function reverses any given string"""
    if len(r) == 0:                                                             #1
        #if the sequence is empty then it will return nothing, it terminates the function
        return str("")                                                          #1
    else:                                                                       #1
        return words_reversed(r[1:]) + str(r[0]) + str(" ")                     #1
        # puts the first word after the last word
sentence = input ("enter something you want to see in reverse: ")               #1
words = sentence.split(" ")                                                     #1
# splits every array and puts it into its index
print(words_reversed(words))                                                    #1

##formula = 8
####therefore this function would have a big O() of 1
