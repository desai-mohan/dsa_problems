def search(arr, target) :
    low=0 
    high=len(arr)-1  
    while low<=high:
        mid = low + (high-low)//2
        if arr[mid]==target:
            return mid 
        if arr[low]>arr[mid]:
            # right_sorted
            if arr[mid]<target and target <= arr[high]:
                low=mid+1 #discard left completely
            else:
                high=mid-1 
        else:
            #left_sorted
            if arr[low]<=target and target <arr[mid]:
                high=mid-1 #discard right completely
            else:
                low=mid+1 
    return -1 
        

array=[11,12,13,1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
target =13 
result=search(array,target) 
if result != -1:
    print(f"Element {target} found at index: {result}") 
else:    
    print(f"Element {target} not found in the array.")
