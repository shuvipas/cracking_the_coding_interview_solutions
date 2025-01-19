# 8.1 Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
# steps at a time. Implement a method to count how many possible ways the child can run up the
# stairs.

def tripleStepDp(n,arr):
    if n <4:
        if n == 2 or n==3:
            return 2
        else: #  n==0 or n==1:
            return 1
       
        return 2 if n>1 else 1 # 2 ways for 3/2 1 way for 1/0
    
    if arr[n] != 0:
        return arr[n]
    else:
        arr[n] = tripleStepDp(n-1,arr)+tripleStepDp(n-2,arr)+tripleStepDp(n-3,arr)
        return arr[n]
def tripleStep(n):
    """ if n <4:
        if n == 2 or n==3:
            return 2
        else: #  n==0 or n==1:
            return 1
    return tripleStep(n-1) + tripleStep(n-2) +tripleStep(n-3)  """   
        
    arr = [0]*(n+1)
    arr[1] = 1
    return tripleStepDp(n,arr)

# 8.2 Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
# The robot can only move in two directions, right and down, but certain cells are "off limits" such that
# the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
# the bottom right
def robotMaze(r,c):
    pass

# 8.3 Magic Index: A magic index in an array A [1. .. n -1] is defined to be an
#  index such that A[ i] = i. Given a sorted array of distinct integers,
#  write a method to find a magic index, if one exists, in array A.
# FOLLOW UP
# What if the values are not distinct?
def magicIndex(arr):
    """ for i in range(len(arr)):
        if i == arr[i]:
            return i """
    if arr == []:
        return None
    mid = int(len(arr)/2)
    if arr[mid] == mid:
        return mid
    if arr[mid] < mid: # index not at the left side 
        return magicIndex(arr[mid+1:])
    else:
        return magicIndex(arr[:mid])

# 8.4 Power Set: Write a method to return all subsets of a set.
def powerSet(arr):
    pass

# 8.5 Recursive Multiply: Write a recursive function to multiply two positive integers without using
# the * operator (or / operator) . You can use addition, subtraction, and bit shifting, but you should
# minimize the number of those operations.
def recursiveMultiply(a,b):
    small = a if a<b else b
    big = b if b>a else a
    if small ==1:
        return big
    else:
        return big + recursiveMultiply(big, small-1)
def test_recursiveMultiply():
    print(recursiveMultiply(3,4) ==3*4)
    print(recursiveMultiply(3,9) ==3*9)
    print(recursiveMultiply(1,86) ==86)

# 8.6 Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of
# different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order
# of size from top to bottom (Le ., each disk sits on top of an even larger one). You have the following
# constraints:
# (1) Only one disk can be moved at a time .
# (2) A disk is slid off the top of one tower onto another tower.
# (3) A disk cannot be placed on top of a smaller disk.
# Write a program to move the disks from the first tower to the last using Stacks
    



def main():
    test_recursiveMultiply()
if __name__ == "__main__":
    main()