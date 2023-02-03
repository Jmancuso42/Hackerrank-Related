##My solution
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your c  ode here
    positive,negative,neutral = 0.0,0.0,0.0
    
    #range(0,len(arr)-1)
    for num in arr:
        
        if num > 0:
            positive += 1
        if num < 0:
            negative += 1
        elif num == 0:
            neutral +=1
    positive = format((positive/len(arr)),'.6f')
    negative = format((negative/len(arr)),'.6f')
    neutral = format((neutral/len(arr)),'.6f')
    
    print(positive)
    print(negative)
    print(neutral)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)






##Someone else's solution that I like better because of the f-string
pos = 0 
neg = 0 
zeros = 0 
length = len(arr)
for i in range(length):
    if (arr[i] > 0):
        pos += 1
    elif (arr[i] < 0):
        neg += 1
    else:
        (arr[i] == 0)
        zeros += 1
print(f'{pos / length:.6f}')
print(f'{neg / length:.6f}')
print(f'{zeros / length:.6f}')
