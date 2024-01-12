# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the
# second element is sum of negative numbers. 0 is neither positive nor negative
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15],
# you should return [10, -65].
def count_positives_sum_negatives(arr):
    if arr == []:
        return []

    countofpo = 0
    sumofneg = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            countofpo += 1
        else:
            sumofneg += arr[i]

    return [countofpo, sumofneg]
arrr = [3,4,56,-4 ,-4,-5]
answer = count_positives_sum_negatives(arrr)
print(answer)