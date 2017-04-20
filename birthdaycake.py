# Input Format

#The first line contains a single integer, , denoting the number of candles on the cake. The second line contains  space-separated integers, where each integer  describes the height of candle .

#Constraints

#Output Format

#Print the number of candles Colleen blows out on a new line.

#Sample Input 0

# 4
# 3 2 1 3
#Sample Output 0

#2

---------------------------------------------------------------------
Solution

#!/bin/python

import sys


n = int(raw_input().strip())
height = map(int,raw_input().strip().split(' '))
print (height.count(max(height)))

----------------------------------------------------------
