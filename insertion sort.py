#for a insertion sort, you check the value (from index 1, not 0) against every value behind of it until it is orderd

arr = [2,8,4,0,2,6,1,22,44,33,11,6,3]

#ascending order
def insertion():
    for i in range(1,len(arr)):
        item_to_sort = arr[i] #item that is first to be sorted arr[1]
        current_index = i - 1 #current index of value behind value to be sorted 
        while (arr[current_index]>item_to_sort) and (current_index > -1): #if the value behind the item to be sorted is greater
            arr[current_index + 1] = arr[current_index] #set the index of the value to be sorted to the value of the one behind it
            current_index -= 1 #go to the next index behind it, so if we are sorting index 3, we will now be on index 1
        arr[current_index + 1] = item_to_sort #put item to be sorted in its new index
    
    print(arr)

insertion()
