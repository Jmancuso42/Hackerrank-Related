##Algo:
#for Loop
#create evaluation variables
#loop through the parameter number
#if evaluation chain, make sure it is in correct order:

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    for num in range (1,n+1):
        divides_by_three = (num%3==0)
        divides_by_five = (num%5==0)
        
        if divides_by_three and divides_by_five:
            print("FizzBuzz")
        elif divides_by_three:
            print("Fizz")
        elif divides_by_five:
            print("Buzz")
        elif not divides_by_three or divides_by_five:
            print(num)
            
        
if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)




### A far more elegant solution using hashmaps. It would be far more maintainable and elegant than the naive solution if you used an ordered dict:

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # ans list
        ans = []

        # Dictionary to store all fizzbuzz mappings
        fizz_buzz_dict = {3 : "Fizz", 5 : "Buzz"}
        
        # List of divisors which we will iterate over.
        divisors = [3, 5]

        for num in range(1, n + 1):

            num_ans_str = []

            for key in divisors:
                # If the num is divisible by key,
                # then add the corresponding string mapping to current num_ans_str
                if num % key == 0:
                    num_ans_str.append(fizz_buzz_dict[key])

            if not num_ans_str:
                num_ans_str.append(str(num))

            # Append the current answer str to the ans list
            ans.append(''.join(num_ans_str))
