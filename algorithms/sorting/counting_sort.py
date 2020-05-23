from typing import List


def counting_sort(arr: List = []) -> List:
    """
    Input: sequence of number store in array (list): [a1,a2,a3 ,.... an]
    Output: permutation of that array that following the ascending value property: [a1', a2', a3', ... , an']
        where a1'<= a2' <= a3' <= ...  <= an'

    Property:
    1. The algorithm works well when range (maxVal - minVal) is lower than the length of array
    2. Stable
    3. Runtime: O(n)
    4. Space: O(range)

    Description:
    1. Keep track of the frequency of each value since it is much likely that one element appear more than once
    2. Iterate through the original array once, and tally the frequency of each element.
    3. Iterate through the array and in-place updating the corrected order of elements with its frequency

    Examples:
    >>> counting_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> counting_sort([])
    []
    >>> counting_sort([-2, -5, -45])
    [-45, -5, -2]
    >>> counting_sort([-1,-1,-1,1,0])
    [-1, -1, -1, 0, 1]
    """
    if not arr:
        return arr
    minVal, maxVal = min(arr), max(arr)

    # frequency table
    tally = [0] * (maxVal - minVal + 1)

    # traverse and keep increase the frequency of each number
    for num in arr:
        tally[num - minVal] += 1

    # sort the input arr in-place by updating each element based on the tally array.
    i = 0
    for index, frequency in enumerate(tally):
        number = index + minVal
        while frequency > 0:
            arr[i] = number
            i += 1
            frequency -= 1
    return arr
