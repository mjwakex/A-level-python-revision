from operator import itemgetter
import queue


queue = [None for i in range(10)]
front_pointer = 0
rear_pointer = -1
queue_full = 10
queue_length = 0
item = None

#if rear_pointer is pointing to the last element in the array but queue is not full...
#item is stored in first element of array
def enQueue(x):
    global queue_length, rear_pointer
    if queue_length < queue_full:
        if rear_pointer < len(queue) - 1:
            rear_pointer += 1
        else:
            rear_pointer = 0
        queue_length += 1
        queue[rear_pointer] = x
        return True #item added
    else:
        return False #queue is full

#if front_pointer points to last element in the array and the queue is not empty...
#the pointer is updated to point at the first item in array rather than the next item
def deQueue():
    global queue_length, front_pointer, item
    if queue_length == 0:
        return False #queue is empty
    else:
        item = queue[front_pointer]
        if front_pointer == len(queue)-1:
            front_pointer = 0
        else:
            front_pointer += 1
    queue_length -= 1