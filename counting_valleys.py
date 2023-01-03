import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    up_down_sum = 0
    previous_sum = 0
    counter = 0
    for i in range(n):
        if s[i] == 'U':
            up_down_sum += 1
        else:
            up_down_sum -= 1

        if previous_sum == 0 and up_down_sum < 0:
            counter += 1

        previous_sum = up_down_sum

    return counter