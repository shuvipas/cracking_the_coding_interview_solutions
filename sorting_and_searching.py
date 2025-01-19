import random
def bubbleSort(arr):
    if len(arr)<2:
        return arr
    
    for i in range(len(arr)):
        swapped= False
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
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
            arr[i],arr[index] = arr[index],arr[i]
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
    print(randArr)
    mergeSort(randArr)




def main():
    pass
    #test_mergeSort()
    #test_selectionSort()
    #test_bubbleSort()
if __name__ == "__main__":
    main()