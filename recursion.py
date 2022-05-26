#recursive function is a function that calls itself within itself:
"""
def function():
    function()

function()

"""

#recurcive function to find factorial of n
from turtle import position


def factorial(n): #n is the base case
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)# returns n*n-1*n-2*n-3


#recursive binary search
list=[1,2,3,4,5,6,7,8]

def binary(value, upper , lower):
    
    #check the base case
    if upper >= lower:
        mid = lower + (upper-1) // 2

        #if value is at mid
        if list[mid] == value:
            return f"found at {mid}"
        
        #if value is smaller, call the function on the left half
        elif list[mid] > value:
            return binary(value,mid-1,lower)
        
        #if value is bigger, call function on the right half
        else:
            return binary(value,upper,mid+1)
    
    return "value not found"

print(binary(3,len(list)-1,0))

#recursive insertion sort
def insertion(arr, n): #arr is the list to sort and n is how many things in list
    #base case
    if n <= 1:
        return
    
    #sort first n-1 elements
    insertion(arr, n-1)
    item_to_sort = arr[n-1]
    current_index = n-2
    while (current_index >= 0) and (arr[current_index] > item_to_sort):
        arr[current_index+1] = arr[current_index]
        current_index -=1
    arr[current_index+1] = item_to_sort


#recursive bubble sort
def bubble(arr, n): #where n is len(arr)
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
        
        if n-1 > 1: #if there is more than one element, do again
            bubble(arr, n-1)
    
    
