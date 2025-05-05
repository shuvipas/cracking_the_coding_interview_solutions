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
    def pop(self):
        return self.items.pop(0)
    
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
    def isEmpty(self):
        pass
    def push(self,item):
        if self._stacks_len[self._ptr] == self.limit:
            self._stacks.append(MyLIFO())
            self._stacks_len.append(0)
            self._ptr +=1

        self._stacks[self._ptr].push(item)
        self._stacks_len[self._ptr] +=1

    def pop(self):
        while self._ptr >=0 and self._stacks_len[self._ptr] == 0:
            if self._ptr ==0:
                return None
            self._stacks_len.pop()
            self._stacks.pop()
            self._ptr -=1
            
        self._stacks_len[self._ptr] -=1
        
        return self._stacks[self._ptr].pop()
    def popAt(self,index):
        if index<0 or index >= len(self._stacks) or self._stacks_len[index] == 0:
            return None
        self._stacks_len[index] -=1
        
        return self._stacks[index].pop()
            
def test_set_of_stacks():
    stacks = SetOfStacks(limit=3)
    for i in range(10):  
        stacks.push(i)
    
    print("Popped:", stacks.pop())  # Should return 9
    print("Popped at index 1:", stacks.popAt(1))  # Should return 5 (from second stack)
    print("Popped at index 0:", stacks.popAt(0))  # Should return 2
    while stacks._ptr >= 0:  # Pop until empty
        popped = stacks.pop()
        if popped ==None:
            break
        print("Popped:", popped )
# 3.4 Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.

class MyQueue:
    def __init__(self):
        self._pop_stack = MyLIFO()     
        self._add_stack = MyLIFO()

    def _transfer_items2pop(self):
        while not self._add_stack.isEmpty():
            self._pop_stack.push(self._pop_stack.pop()) 

    def add(self,item):
        self._add_stack.push(item)
    def remove(self):
        if self.isEmpty():
            return None
        if self._pop_stack.isEmpty():
            #transfer all elements from second stack
            self._transfer_items2pop()
        self._pop_stack.push()        
    def peek(self):
        if self.isEmpty():
            return None
        if self._pop_stack.isEmpty():
            self._transfer_items2pop()
        self._pop_stack.peek()

        pass
    def isEmpty(self):
        if self._pop_stack.isEmpty() and self._add_stack.isEmpty():
            return True
        return False
# 3.5 Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array) . The stack supports the following operations: push , pop, peek , and isEmpty .
def stack_sort(st):

    helper = MyFIFO()
    
    #loop on all st elements
    while not st.isEmpty():
        temp = st.pop()
        while not helper.isEmpty() or temp < helper.peek():
            st.push(helper.pop())
        helper.push(temp)
    while not helper.isEmpty():
        st.push(helper.pop())
    return st 
 
# 3.6 Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first
# out " basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or the y can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type). They cannot select which specific animal they would like. Create the data structures to
# maint ai n this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat. You may use the built- in LinkedList data structure.
class Animal:
    def __init__(self,name,kind):
        self.name =name
        self.kind = kind #dog =1, cat =0

class AnimalQueue:
    def __init__(self):
        self._allQueue = MyFIFO() #true  for dogs false for cats
        self._catQueue = MyFIFO()
        self._dogQueue = MyFIFO()
    def enqueue(self,animal):
        self._allQueue.add(animal)
        
    def dequeueAny(self):
        return self._allQueue.pop()
        
    def dequeueKind(self,kind):
        templifo = MyLIFO()
        curr = self.dequeueAny()
        while curr.kind != kind:
            if curr == None:
                break
            tempLifo.push(curr)
        temp = templifo.pop()
        while temp:
            self.enqueue(temp)
        return curr

    def dequeueDog(self):
        return dequeueKind(self,1)
        
    def dequeueCat(self):
        return dequeueKind(self,0)
        



def main():
    test_set_of_stacks()
    #test_mylifo()
    #test_myfifo()
    pass
if __name__ == "__main__":
    main()