#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

def twoStacks(maxSum, a, b):
    # Write your code here
    index_a, index_b, current_sum, maximum_count = 0, 0, 0, 0

    while index_a < len(a) and current_sum + a[index_a] <= maxSum:
        current_sum += a[index_a]
        index_a += 1

    if current_sum > maxSum:
        index_a -= 1
        maximum_count = max(maximum_count, index_a)
    else:
        maximum_count = max(maximum_count, index_a)
        index_a -= 1

    while index_b < len(b) and current_sum <= maxSum:
        current_sum += b[index_b]
        index_b += 1

        while current_sum > maxSum and index_a >= 0:
            current_sum -= a[index_a]
            index_a -= 1

        if current_sum <= maxSum:
            maximum_count = max(maximum_count, index_a + index_b + 1)

    return maximum_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
