#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    lst=[]
    lst=lst+[len(arr)]
    count=0
    
    for j in range(len(arr)):
        count=0
        mi=min(arr)
        print(mi)
        for i in range(0,len(arr)):
            if arr[i]==mi:
                count+=1
        print(count)
        
        for r in range(count):
            arr.remove(mi)
        if len(arr)==0:
            break
        lst=lst+[len(arr)]

        for h in range(len(arr)):
            arr[h]=arr[h]-mi

    return(lst)


            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
