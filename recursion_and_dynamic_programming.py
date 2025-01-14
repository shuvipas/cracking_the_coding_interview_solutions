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
    