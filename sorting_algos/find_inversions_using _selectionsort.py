# You have a list of numbers that are not in order. You want to find the sum of the differences between the indices of pairs of numbers that are in the wrong order. A pair of numbers is considered to be in the wrong order if the smaller number comes after the larger number in the list.

# Example:
# Input: ‘N’ = 5 
# ‘A’ = [3, 2, 11, 5, 1]

# Output: 6
def count_inversions(arr):
    inversions=0 
    n=len(arr) 
    for i in range(n):
        min_index=i 
        for j in range(i+1,n):
            if arr[j]<arr[min_index]: 
                min_index=j
        inversions=inversions+(min_index-i)
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return inversions
arr=[3, 2, 11, 5, 1]
print(count_inversions(arr))