from typing import (List)


def max_sum_subarray(arr: List) -> int:
    """
    LC: https://leetcode.com/problems/maximum-subarray/

    Given an integer array, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

    Since there are different approach in solving this problem, including Kadane's Algorithm (https://en.wikipedia.org/wiki/Maximum_subarray_problem). Implementing this in DP approach is more subtle.

    Description:
    1. Suppose we want to find the maximum subarray of arr[i,i+1,i+2..., j] have start and end index denoted as m, n where i <= m <= n <= j.
    2. If we divide original array into 2 partial arrays arr[i, mid] and arr[mid + 1, j], then there are 3 scenerios/places: 
      1) i <= m <= n <= mid <= j. In this case maximum_array[arr[i,i+1,i+2,...,j]] == maximum_array[arr[i,i+1,i+2,...,mid]]
      2) i <= mid <= m <= n <= j. In this case maximum_array[arr[i,i+1,i+2,...,j]] == maximum_array[arr[mid + 1,mid + 2,mid+3,...,j]]
      3) i <= m <= mid <= n <= j. We have to create a method call find_max_crossing_subarray for this case.

    Example:
    Input: [-2,1,-3,4,-1,2,1,-5,4],
    Output: 6

    Doctest template:
    >>> max_sum_subarray([1,2,-5,2,4,-4,1,4])
    7
    >>> max_sum_subarray([1,-1])
    1
    >>> max_sum_subarray([-1,-2,-3])
    -1
    >>> max_sum_subarray([1,2,3,4,5])
    15
    >>> max_sum_subarray([1,2,4,3,-12,11])
    11
    """

    def find_max_crossing_subarray(mid: int, low: int, high: int):
        nonlocal arr
        max_left = float('-inf')
        cur_sum = 0
        i = mid
        while i >= low:
            cur_sum += arr[i]
            max_left = max(max_left, cur_sum)
            i -= 1
        max_right = float('-inf')
        cur_sum = 0
        i = mid + 1
        while i <= high:
            cur_sum += arr[i]
            max_right = max(max_right, cur_sum)
            i += 1
        return max(max_left, max_right, max_left + max_right)

    def find_max_subarray(low: int, high: int):
        nonlocal arr
        if low == high:
            return arr[low]

        mid = low + int((high - low) / 2)
        return max(find_max_subarray(low, mid), find_max_subarray(mid + 1, high), find_max_crossing_subarray(mid, low, high))

    return find_max_subarray(0, len(arr) - 1)
