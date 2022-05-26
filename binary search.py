#binary search gets the middle index and compares and then depending if the value u are looking for is > or < you look at the right or left half and so on

list=[1,2,3,4,5,6,7,8,9]

def binary(value):
    upper_bound = len(list) - 1
    lower_bound = 0
    while lower_bound <= upper_bound:
        mid = lower_bound + (upper_bound-1) // 2

        #check if value is at mid
        if list[mid] == value:
            return f"Found at index {mid}"

        #if value is bigger than mid, look at right half
        elif list[mid] < value:
            lower_bound = mid + 1
        
        #if value is smaller than mid, look at left half
        elif list[mid] > value:
            upper_bound = mid - 1
    
    return "Element not found"

print(binary(2))

#recursive version in recursion.py