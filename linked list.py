#syllabus says you need to be able to ....
#find an item,insert an item,delete an item
#to understand each function, easiest way is to go through with paper and draw whats happening

list = [1,6,3,9,77,32,4,None,None,None,None]
pointers = [-1,0,1,2,3,6,7,8,9,10,-1]
start_pointer = 6
null_pointer =  -1
heap_pointer = 7

def find(item):
    found = False
    item_pointer = start_pointer
    while item_pointer != null_pointer and not found:
        if list[item_pointer] == item:
            found = True
            return True
        else:
            item_pointer = pointers[item_pointer]
    return False

def insert(item):
    global start_pointer
    if heap_pointer == null_pointer:
        print("List is full")
    else:
        temp = start_pointer
        start_pointer = heap_pointer
        heap_pointer = pointers[heap_pointer]
        list[start_pointer] = item
        pointers[start_pointer] = temp

def delete(item):
    global start_pointer, heap_pointer
    if start_pointer == null_pointer:
        print("List is empty")
    else:
        index = start_pointer
        while list[index] != item and index != null_pointer:
            oldindex = index
            index = pointers[index]
        if index == null_pointer:
            print("item was not found in list")
        else:
            list[index] = None
            temp = pointers[index]
            pointers[index] = heap_pointer
            heap_pointer = index
            pointers[oldindex] = temp
