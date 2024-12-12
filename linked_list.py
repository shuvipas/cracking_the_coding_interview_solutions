import random


class Node:
        def __init__(self,data):
            self.data = data
            self.next = None
def newLinked(endVal, startVal=0):
    head = Node(0)
    curr = head
    if endVal>startVal:
        for i in range(startVal,endVal + 1):
            curr.next = Node(i)
            curr = curr.next
    else:
        for i in range(startVal,endVal - 1,-1):
                    curr.next = Node(i)
                    curr = curr.next

    return head.next

def randNewLinked(maxVal, nodeNum):
    head = Node(random.randint(0,maxVal))
    curr = head
    for i in range(1,nodeNum):
        curr.next = Node(random.randint(0,maxVal))
        curr = curr.next
    return head

def insertAtBegin(head, val):
    nhead = Node(val)
    nhead.next = head
    return nhead

def printLinked(head):
    while head:
        if head.next:
            print(head.data, " -> ",end="")
        else: 
            print(head.data)
        head = head.next



# 2.1 Remove Dups: Write code to remove duplicates from an unsorted li nked list.
# FOLLOW UP How would you solve this problem if a temporary buffer is not allowed?

def removeDuplicates(head):
    #with a set O(n) time and space
    """
    curr = head
    llset = {curr.data}
    while curr.next:
        val =curr.next.data 
        if val in llset:
            curr.next = curr.next.next
        else:
            llset.add(val)
            curr = curr.next
    return head
"""
    #with o(n^2) time O1 space
    curr = head
    while curr:
        runner = curr
        while runner.next:
            if runner.next.data == curr.data:
                runner.next = runner.next.next
            else:  
                runner = runner.next
        curr = curr.next
    return head

def test_removeDuplicates():
    head = newLinked(4)
    for i in range(6):
        head = insertAtBegin(head,i)
    printLinked(head)
    printLinked(removeDuplicates(head))

# 2.2 Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

def kthElement(head,k):
    llLen =0
    curr = head
    while curr:
        llLen +=1
        curr = curr.next
    curr =head
    target = llLen -k 
    print(target)
    print(llLen)
    for i in range(target):
        curr = curr.next
    return curr

# 2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.
# EXAMPLE
# Input: the node c from the linked list a - >b- >c - >d - >e- >f
# Result: nothing is returned, but the new linked list looks like a - >b- >d - >e- >f

def delMiddle(node):
    node.data = node.next.data
    node.next = node.next.next
    

def test_delMiddle():
    head = newLinked(7)
    curr = head
    printLinked(head)
    for i in range(3):
        curr=curr.next
    print(curr.data)
    delMiddle(curr)
    printLinked(head)

# 2.4 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x . lf x is contained within the list, the values of x only need
# to be after the elements less than x (see below) . The partition element x can appear anywhere in the
# "right partition "; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input: 3 -> 5 -> 8 -> 5 - > 10 -> 2 -> 1 [partition = 5)
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
def partition(head, k):
    smaller = Node(None)
    bigger = Node(None)
    currSmall = smaller
    currBig = bigger
    
    curr = head
    while curr:
        if curr.data < k:
            currSmall.next = curr
            currSmall = currSmall.next
        else:
            currBig.next = curr
            currBig = currBig.next
        curr = curr.next
    
    currBig.next = None
    currSmall.next = bigger.next
    return smaller.next
def test_partition():
    head = randNewLinked(10,15)
    printLinked(head)

    nhead = partition(head, 3)
    printLinked(nhead)
    nhead = partition(head, 7)
    printLinked(nhead)

# 2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2) . Thatis,617 + 295.
# Output: 2 - > 1 - > 9. That is, 912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).Thatis,617 + 295.
# Output: 9 - > 1 - > 2. That is, 912 .

def linked2numReverse(head):
    i = 0
    num =0
    curr= head
    while curr:
        num += curr.data*(10**i)
        i += 1
        curr = curr.next
    return num
def linked2numForward(head):
    num =0
    curr= head
    while curr:
        num = num*10 + curr.data
        curr = curr.next
    return num

def num2llReverse(num):
    head = Node(0)
    curr =head
    while num:
        curr.next = Node(num%10)
        num //=10
    return head.next



def sumLists(nodeA,nodeB):
    numA = linked2numReverse(nodeA)
    numB = linked2numReverse(nodeB)
    return numA+numB
def test_sumLists():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    assert(linked2numReverse(head)==321)
    assert(linked2numForward(head)==123)
    assert(sumLists(head,head)==2*321)


# 2.6 Palindrome: Implement a function to check if a linked list is a palindrome.

def palindrome(head):
    #with n space
    arr = []
    curr = head
    while curr:
        arr.append(curr.data)
        curr = curr.next
    i =0 
    j = len(arr) -1
    while j>i:
        if arr[i] != arr[j]:
            return False
        i+=1
        j-=1
    return True
def test_palindrome():
    print("start testing")
    lla = newLinked(3,0)
    llb = newLinked(0,3)
    last = lla
    while last.next:
        last = last.next    
    last.next = llb
    assert(palindrome(lla))
    
    last.next = Node(2)
    last.next.next= llb
    assert(palindrome(lla))

    llc = Node(77)
    llc.next = lla
    assert(palindrome(llc)==False)
    print("end testing")

#2.7 Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the inter-
# secting node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.

# 2.8 Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.
# EXAMPLE
# Input:A -> B -> C -> o -> E - > C [the same 'C' as earlier]
# Output:C



def main():
    # test_removeDuplicates()
    # test_delMiddle()
    # test_delMiddle()
    #test_partition()
    #test_sumLists()
    test_palindrome()
    pass

if __name__ == "__main__":
    main()

