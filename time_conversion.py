#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#bc i did it recently sort of, with that meetup group, am not 100% stumped, but not pulling it off

def timeConversion(s):
  # Write your code here
    string = ""
    timeDenotion = s[-2:]    
    hour = s[:2]
    
    if timeDenotion == "AM":
        print('1')
        if s[:2] != "12":
            print('2')
            s = s[:-2]
        else:
            print('3')
            s = "00" + s[2:-2] #has to start at index 2, bc 00 replaces the first two
    elif timeDenotion == "PM":
        print('4')
        if int(s[:2]) < 12:
            print('5')
            s = str(int(s[:2])+ 12) + s[2:-2] #add 12 to the hour
        else:
            print('6')
            s = s[:-2]
    return s
          #Attempt 2 didn't evaluate anything, it was for sure because i messed up the slicing:/  
#    if timeDenotion == "AM":
#        print("1")
#        if (s[:2] == '12'):
#            print('2')
#            string = "00" + s[2:-2]
#           return string
#        else:
#            print('3')
#            string = s[:-2]
#            return string
#    if timeDenotion == "PM":
#        print('4')
#        if(int(s[:2])==12):
#            string = s[:7]
#            return string
#        else:
#            print('5')
#            string = str(int(s[:2])+ 12)
#            return string
#         return string      
            
    
    
    
    
#     #if timeDenotion == "PM" and s[:1] != "12" :
#       string = str( 12 + int(s[0:2])) + s[2:8]
#        string = s[2:8]
        
#    elif timeDenotion == "PM": 
#        string = str(int(s[0:1]) + int(12)) + s[2:8]
    
#    elif s[-2:] == "AM" and s[:2] == "12":
#        string = "00" + s[2:8]
#    elif s[-2:] == "AM":
#        string = str(int(s[:7]))
#        string = s[2:7]  
#    return string
            
        
        
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
