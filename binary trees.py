#for a binary tree you need to be able to..
#find an item and insert an item

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def find(self, val):
        if val < self.data:
            if self.left is None:
                return "value not found"
            return self.left.find(val)
        elif val > self.data:
            if self.right is None:
                return "value not found"
            return self.right.find(val)
        else:
            return "value found" 

root = Node(30)
root.insert(15)
root.insert(35)
root.insert(40)     
root.insert(10)
root.insert(20)    
print(root.find(2))
print(root.find(40))  