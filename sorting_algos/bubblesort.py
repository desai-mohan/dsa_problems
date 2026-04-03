def bubblesort(array):
    for i in range(0,len(array)-1):
        #outer loop to traverse through all elements, 
        # after each pass the largest element will be at the end of the array,
        #  so we can ignore it in the next pass
        for j  in range(0,len(array)-1-i): #inner loop to compare adjacent elements and swap if they are in wrong order
            if array[j]>array[j+1]: #compare adjacent elements and swap if they are in wrong order
                array[j],array[j+1]=array[j+1],array[j]
    return array
print(bubblesort([64, 34, 25, 12, 22, 11, 90]))