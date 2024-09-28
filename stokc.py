#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'stockPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY stocksProfit
#  2. LONG_INTEGER target
#

def stockPairs(stocksProfit, target):
    # Write your code here
    final=[]
    print(stocksProfit, target)
    
    def rec(start, total, val, level):
        level+=1
        if total == target:
            print(final)
            if start not in final and len(start)==2:
                final.append(start.copy())
            return
        if level ==3:
            return
        for index, i in enumerate(val):
            start.append(i)
            total += i
            if total > target:
                start.pop()
                total -=i
                break
            rec(start, total, val[index+1:], level)
            start.pop()
            total -=i
    
    rec([], 0, sorted(stocksProfit),0)
    print(final)
    return len(final)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stocksProfit_count = int(input().strip())

    stocksProfit = []

    for _ in range(stocksProfit_count):
        stocksProfit_item = int(input().strip())
        stocksProfit.append(stocksProfit_item)

    target = int(input().strip())

    result = stockPairs(stocksProfit, target)

    fptr.write(str(result) + '\n')

    fptr.close()
