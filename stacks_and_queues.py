class MyLIFO:
    """
    pop ( ) : Remove the top item from the stack.
    push (item): Add an item to the top of the stack.
    peek ( ) : Return the top of the stack.
    isEmpty ( ) : Return true if and only if the stack is empty.
    """
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.items[len(self.items)-1]
    
class MyFIFO:
    """
    add(item): Add an item to the end of the list.
    remove ( ): Remove the first item in the list.
    peek ( ) : Return the top of the queue.
    isEmpty ( ) : Return true if and only if the stack is empty.
    """
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def add(self,item):
        self.items.append(item)
    
    def remove(self):
        self.items.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.items[0]
    
def test_mylifo():
    stack = MyLIFO()
    for i in range(5):
        stack.push(i)
    print(stack.peek())
    while not stack.isEmpty():
        print(stack.pop())
    print(stack.peek())

def test_myfifo():
    queue = MyFIFO()
    for i in range(5):
        queue.add(i)
    while not queue.isEmpty():
        print("peek: ",queue.peek())
        queue.remove()        

# 3.1 Three in One: Describe how you could use a single array to implement three stacks.



def main():
    #test_mylifo()
    #test_myfifo()
    pass
if __name__ == "__main__":
    main()