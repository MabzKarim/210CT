import random

arraynumbers=[4,3,2,1,7,6,5,8,10,9]                                          #1

def randShuffle(arraynumbers):                                               #1
    """This function is so that the current array is shuffled into a
    different array"""
    countArray = len(arraynumbers)                                           #1
    # The variable above counts all the numbers in the array

    for i in range(countArray - 1, 0, -1):                                   #n
    # This would iterate through the elements starting from the end of the array

        randSelection = random.randint(0,countArray -1)                      #n
        # this variable generates a random number
        
        temporary = arraynumbers[i]                                          #n
        arraynumbers[i] = arraynumbers[randSelection]                        #n
        arraynumbers[randSelection] = temporary                              #n
        # swaps the numbers in the array

    return arraynumbers                                                      #1
    
print(randShuffle(arraynumbers))                                             #1

##formula = 5n+5
##therefore this function would have a big O() of n

def calculating_trailing_zeros(factorial_n):                                        #1
    """this function returns the trailling 0s of any factorial number"""
    power_root = 0                                                                  #1
    number_trailing_zeros = 0                                                       #1
    s = factorial_n / (5 ** power_root)                                             #1
    while ((factorial_n / (5 ** power_root)) >=1):                                  #n
        power_root = power_root + 1                                                 #n
        number_trailing_zeros = number_trailing_zeros + int((factorial_n / (5 ** power_root)))
                                                                                    #n
    return number_trailing_zeros                                                    #1

print(calculating_trailing_zeros(5555))                                             #1

##formula = 3n+6
####therefore this function would have a big O() of n

