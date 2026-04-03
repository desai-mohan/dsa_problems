def selection_sort(arr):  
    n=len(arr)
    for i in range(n):
        min_index=i #assume first element is minimum
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:#check if there is a smaller element than current min, if update min_index
                min_index=j 
        arr[i],arr[min_index]=arr[min_index],arr[i]#swap element with index i with min_index element
    return arr 

array=[64, 25, 12, 22, 11] 
print(selection_sort(array))