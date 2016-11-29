import random

arraynumbers=[4,3,2,1,7,6,5,8,10,9]      

def randShuffle(arraynumbers):    
    """This function is so that the current array is shuffled into a
    different array"""
    countArray = len(arraynumbers)       
    # The variable above counts all the numbers in the array

    for i in range(countArray - 1, 0, -1):   
    # This would iterate through the elements starting from the end of the array

        randSelection = random.randint(0,countArray -1)          
        # this variable generates a random number
        
        temporary = arraynumbers[i]     
        arraynumbers[i] = arraynumbers[randSelection]          
        arraynumbers[randSelection] = temporary     
        # swaps the numbers in the array

    return arraynumbers     
    
print(randShuffle(arraynumbers))   

