"""
Import modules below
from {dir}/{folder} import {filename}
"""
from typing import List


def insertion_sort(arr: List) -> List:
    """
    Input: sequence of number store in array (list): [a1,a2,a3 ,.... an]
    Output: permutation of that array that following the ascending value property: [a1', a2', a3', ... , an']
            where a1'<= a2' <= a3' <= ...  <= an'

    Property:
    - Stable
    - Runtime: O(n^2) amortize
    - Space: O(1) 

    Description: 
    - For each sorted subarray of  arr[0,1,2,...,j - 1] that is sorted, we find the appropriate index for the current value arr[j] in the sorted array and update it to the sorted array.
    - Start with j = 1, meaning that arr[0,..,0] is sorted itself, than building up from there until we cover all of the rest unsorted subarray

    Doctest:
    >>> insertion_sort([2,5,4,1])
    [1, 2, 4, 5]

    >>> insertion_sort([1])
    [1]

    >>> insertion_sort([2,3,3,2,1,1,1])
    [1, 1, 1, 2, 2, 3, 3]

    >>> insertion_sort([2, -1, 3, -2, 1, 5])
    [-2, -1, 1, 2, 3, 5]
    """
    if len(arr) < 2:
        return arr
    j = 1
    while j < len(arr):
        i = j - 1
        cur_val = arr[j]
        while i >= 0 and arr[i] > cur_val:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = cur_val
        j += 1
    return list(arr)
