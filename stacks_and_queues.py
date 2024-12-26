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

# 3.3 Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push () and SetOfStacks. pop () should behave identically to a single stack
# (that is , pop ( ) should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt (int index) which performs a pop operation on a specific sub-stack 
class SetOfStacks:
    def __init__(self, limit=3):
        self.limit = limit
        self._ptr=0
        self._stacks_len = [0]
        self._stacks= [MyLIFO()]
    def push(item):
        if self._stacks_len[self._ptr] < self.limit -1:
            _stacks[self._ptr].push(item)
            self._stacks_len[self._ptr] +=1
            
        pass
    def pop():
        pass


def main():
    #test_mylifo()
    #test_myfifo()
    pass
if __name__ == "__main__":
    main()