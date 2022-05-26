#bubble sort checks two values next to each other and swaps them if it needs to
#at then edn of each iteration, the last indexes will be sorted 

#quick way of bubble
def bubble(arr):
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    print(arr)

bubble([5,1,7,2,8,3])

#textbook way of bubble (probably better for paper 4)
def textbook_bubble(arr):
    top = len(arr)
    swap = True
    while swap or top > 0:
        swap = False
        for i in range(top-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swap = True
        top -= 1
    print(arr)

textbook_bubble([5,1,7,2,8,3])
         