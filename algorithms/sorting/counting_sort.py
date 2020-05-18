from typing import List


def counting_sort(arr: List = []) -> List:
    """
        Implementation of counting_sort in Python: https://en.wikipedia.org/wiki/Counting_sort
        :param collection: some mutable ordered collection with heterogeneous
        comparable items inside
        :return: the same collection ordered by ascending
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
