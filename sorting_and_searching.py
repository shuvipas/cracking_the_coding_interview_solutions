import random
def swap(arr,a,b):
    arr[a],arr[b] = arr[b],arr[a]

def bubbleSort(arr):
    if len(arr)<2:
        return arr
    
    for i in range(len(arr)):
        swapped= False
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                swap(arr,j,j+1)
                swapped= True
            print(arr)
        if swapped== False:
            return arr
    return arr
def test_bubbleSort():
    randArr = [random.randint(-10, 10) for _ in range(10)]
    bubbleSort(randArr)

def selectionSort(arr):
    for i in range(len(arr)):
        min =arr[i]
        index =i
        for j in range(i+1,len(arr)):
            if min> arr[j]:
                index =j
                min = arr[j]
        if i != index:
            swap(arr,i,index)

        print(arr)

def test_selectionSort():
    randArr = [random.randint(-10, 10) for _ in range(10)]
    selectionSort(randArr)

def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        larr = arr[:mid]
        rarr = arr[mid:]
    
        mergeSort(larr)
        mergeSort(rarr)
        
        l = 0
        r =0
        sortedIdx =0
        while l <len(larr) and r<len(rarr):
            if larr[l] <rarr[r]:
                arr[sortedIdx] = larr[l]
                l +=1
            else:
                arr[sortedIdx] = rarr[r]
                r +=1
            sortedIdx +=1 

        while l <len(larr):
            arr[sortedIdx] = larr[l]
            l +=1
            sortedIdx +=1 
        while r <len(rarr):
            arr[sortedIdx] = rarr[r]
            r +=1
            sortedIdx +=1 
        print(f"Merged: {arr}")



def test_mergeSort():
    randArr = [random.randint(-10, 10) for _ in range(10)]
    print( randArr)
    mergeSort(randArr)



def partition(arr,l,r):
    pivot = arr[(l+r)//2]
    while l<=r:
        while arr[l]<pivot: l+=1 #find element on the left that shold be on the right
        while arr[r] > pivot: r -= 1
        if l<=r:
            swap(arr,l,r)
            l+=1
            r -= 1
    return l

def quickSort(arr,l,r):
   # print(arr[l:r])
    idx = partition(arr,l,r)
    if l< idx -1: #sort left part
        quickSort(arr,l,idx-1)
    if idx < r: #sort right part
        quickSort(arr,idx,r)  

def test_quickSort():
    randArr = [random.randint(-10, 10) for _ in range(10)]
    print( randArr)
    quickSort(randArr,0,len(randArr)-1)
    print(randArr)

def binarySerch(arr,num):
    left = 0
    right =len(arr) -1
    while left <= right:
        mid = (left +right)//2
        midVal = arr[midVal]
        if midVal>num:
            right = mid -1
        elif midVal<num:
            left = mid +1
        else:
            return mid
    return None
# 10.1 Sorted Merge: You are given two sorted arrays, A and B, 
# where A has a large enough buffer at the
# end to hold B. Write a method to merge B into A in sorted order.

#for the pyhon code we will that A's buffer is full of None
def sortedMerge(a,b):
    lastA =len(a)-1
    while a[lastA] == None:
        lastA -=1
    lastB =len(b)-1
    lastComb = lastA + lastB(b)
    
    while lastB >=0:
        if b[lastB] > a[lastA]:
            a[lastComb] = b[lastB]
            lastB -=1 
        else:
            a[lastComb] = a[lastA]
            lastA -=1
        lastComb -=1
    return a
# 10.2 Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to
# each other.
def anagramGroup(arr):
    anagrams ={}
    for s in arr:
        key = "".join(sorted(s))
        if key in anagrams:
            anagrams[key].append(s)
        else: 
            anagrams[key] =[s]
    i = 0
    for val in anagrams.values():
        arr[i] = val
        i+=1
    return arr

# 10.3 Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown
# number of times, write code to find an element in the array. You may assume that the array was
# originally sorted in increasing order.
# EXAMPLE
# InputfindSin {15, 16, 19, 20, 25, 1, 3,4,5,7,10, 14}
# Output 8 (the index of 5 in the array)

def rotatedSearch(arr,k,left, right):

    mid = (right +left) //2
    if arr[mid] ==k:
        return mid
    if left >right:
        return -1
    if arr[left] <= arr[mid]:
        if k >= arr[left] and k<arr[mid]:
            return rotatedSearch(arr,k,left,mid - 1)
        else:
            return rotatedSearch(arr,k,mid+1,right)
    elif arr[mid] < arr[right]:
        if k > arr[mid] and k<=arr[right]:
            return rotatedSearch(arr,k,mid + 1,right)
        else:
            return rotatedSearch(arr,k,left , mid-1)
    else:
        res = rotatedSearch(arr,k,left,mid - 1)
        if res != -1:
            return res
        else:
             return rotatedSearch(arr,k,mid + 1,right)

def test_rotatedSearch():
    print("###test_rotatedSearch###")
    arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    assert(rotatedSearch(arr,3,0,len(arr)-1)== 6)
    assert(rotatedSearch(arr,5,0,len(arr)-1)== 8)
    assert(rotatedSearch(arr,19,0,len(arr)-1)== 2) 
    assert(rotatedSearch(arr,1,0,len(arr)-1)== 5) 
    arr =[0, 1, 2, 3, 4]
    assert(rotatedSearch(arr,4,0,len(arr)-1)==4)
    arr = [2,2,2,3,4,5,2,2]
    assert(rotatedSearch(arr,4,0,len(arr)-1)==4)
             
def main():
    test_rotatedSearch()
    #test_quickSort()
    #test_mergeSort()
    #test_selectionSort()
    #test_bubbleSort()
    pass
if __name__ == "__main__":
    main()