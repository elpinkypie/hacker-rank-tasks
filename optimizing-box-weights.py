#!/bin/python3


# Complete the 'minimalHeaviestSetA' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
from typing import List

def minimalHeaviestSetA(arr: List[int]) -> List[int]:
    # Sort the array in descending order
    arr.sort(reverse=True)
    
    total_sum = sum(arr)
    sum_A = 0
    subset_A = []
    
    # Add elements to subset A until its sum > remaining sum
    for number in arr:
        sum_A += number
        subset_A.append(number)
        if sum_A > total_sum - sum_A:
            break
    
    # Return subset A in sorted order
    return sorted(subset_A)

if __name__ == "__main__":
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    result = minimalHeaviestSetA(arr)
    print("\n".join(map(str, result)))
