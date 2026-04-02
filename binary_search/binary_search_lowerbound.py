def Lower_bound(array,target):
    low=0 
    high=len(array)-1 
    ans=-1 
    while low<=high:
        mid=(low+high)//2 
        # if our mid is greater than or equal to the target, we update the answer 
        # and move the high pointer to mid-1 
        # to continue searching in the left half of the array.
        # If our mid is less than the target, 
        # we move the low pointer to mid+1 to continue searching in the right half of the array. 
        # This way, we can find the lower bound of the target in a sorted array efficiently.
        if array[mid]>target:
            ans=mid 
            high=mid-1 
        else:
            low=mid+1 
    return ans 
array=[1,1,2,2,3,3,4,5,5,5,5,6,7,8,9]
target=5 
result=Lower_bound(array,target)
if result != -1:
    print(f"Lower bound of {target} is at index: {result}") 
else:    
    print(f"{target} not found in the array.")
