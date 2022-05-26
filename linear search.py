#linear search checks each value in list until it is found

list = [1,2,3,4,5,6,7,8,9]

def linear(value):
    for i in list:
        if value == i:
            return True
    return False

print(linear(4))#returns True
print(linear(10))#returns False
