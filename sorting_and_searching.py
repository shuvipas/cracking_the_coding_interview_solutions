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




def main():
    test_bubbleSort()
if __name__ == "__main__":
    main()