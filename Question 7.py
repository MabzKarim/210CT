##Pseudocode for Prime Number Checking:
"""This is the pseudocode to check whether a number is prime or not """

## user<-INPUT"What number would you like to check whether it is prime or not:"
## primeNum(n)
##    primeCheck(x,y)
##       IF Y<=1
##          RETURN N"is prime number"
##       ELSE IF X MOD Y=0
##          RETURN N"is a prime number"
##       ELSE
##          RETURN primeCheck(x, y-1)
##    RETURN primeCheck N, funtionROUND.sqrt(n)
## PRINT primeNum(user)

import math

user = int(input("What number would you like to check whether it is prime or not:"))

def primeNum(n):
   def primeTest(x,y):
      #checks if number is less than or equal to one, which would be a prime number
      if (y<=1):
         return (str(n)+" is prime number")
      elif (x % y==0):
         #if number is anything else then it would not be a prime number 
         return (str(n)+" not a prime number")
      else:
         return primeTest(x, y-1)
   return primeTest(n, round(math.sqrt(n)))
   # returns back the number rounded after sqrt

print(primeNum(user))
   
