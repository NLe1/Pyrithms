"""
Counting sort is a method of sorting in O(n) time and space complexity.
Although the input array has range <= length array in order to be optimal, and the input min and max has to known before hand.

For example if we have arr = [1,9,4,2,1,6,8,9,3,1,2], minVal = 1, maxVal=9
Then range is 9 - 1 = 8 and the len(arr) = 11 > range, which is good to use counting sort.

Here the method will sort the array in-place but feel free to re-implement if you make your code functional.

Input:
- minVal: the minimum value in the arr
- maxVal: max ...
- arr: array itself

Output:
- array that is sorted

#TODO: test instructions
"""


def counting_sort(minVal, maxVal, arr):
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
