#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    # min,max,lowest,highest = 0
    # print(sum(arr)-arr[len(arr)-1],sum(arr)-arr[0]) original idea
    
    arr.sort()
    print(sum(arr[:len(arr)-1]),sum((arr[1:None])))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
    
    
