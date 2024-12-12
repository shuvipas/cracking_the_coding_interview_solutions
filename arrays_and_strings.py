#1.1 implement an algorithm to determine if a string has all unique characters. 
#What if you cannot use additional data structures?
def isUnique(st):
    """st_set = set()
    setLen =0
    for s in st:
        if s not in st_set:
            setLen +=1
            st_set.add(s)
    return len(st) == setLen
    """
    for i in range(len(st)):
        for j in range(i+1, len(st)):
            if st[i]== st[j]:
                return False
    return True


def test_isUnique():
    print(isUnique("aassdfg")==False)
    print(isUnique("qwertyui")==True)
    print(isUnique("")== True)
    print(isUnique("asdfghjkl;d")==False)

#1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

def checkPermutation(st1,st2):
    #i assume that case sasitive and inculdes white spaces

    if len(st1) != len(st2): return 0
    #sort in place and then loop and see if they are the same 
    # but you cant sort in place a string in python 
   
    #with set extra O(n) of space
    stDict= dict()
    for s in st1:
        if s in stDict: stDict[s] +=1
        else: stDict[s] =1

    for s in st2:
        if not bool(stDict) or s not in stDict: return False
        elif stDict[s] ==1: del stDict[s]
        else: stDict[s] -=1
    return not bool(stDict)



def test_checkPermutation():
    print(checkPermutation("asdddf","fdsdad")==True)
    print(checkPermutation("","")==True)
    print(checkPermutation("asddf","asdf")==False)
    print(checkPermutation("","asdfg")==False)
    print(checkPermutation("asdf","werty")==False)
    
    

# 1.3 URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: if implementing in Java, please use a character array so that you can
# perform this operation in place.)
#EXAMPLE
#Input:"Mr John Smith    "
#Output:"Mr%20John%20Smith"
def URLify(st):
    start = False
    nst = ""
    for s in st.strip():
        if s ==" ":
            if start:
                nst += "%20"
                start = False
        else: 
            nst+= s
            start = True
    return nst

def test_URLify():
    print("start test_URLify ")
    assert(URLify("Mr John Smith    ")=="Mr%20John%20Smith")
    assert(URLify("   Mr    John    Smith    ")=="Mr%20John%20Smith")
    assert(URLify("MrJohnSmith")=="MrJohnSmith")
    assert(URLify("   ")=="")
    print("end testing")

             
# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin-
# drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rea rrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input:Tact Coa
# Output:True (permutations: "taco cat". "atco cta". etc.)            

def charVal(c):
    caseDiff = ord('a') - ord('A')
    val = ord(c)
    if 'a'<=c<='z': # val >= ord('a') & val <= ord('z'):
        val -= ord('a')
    elif 'A'<=c<='Z': #val >= ord('A') & val <= ord('Z'):
        val -= ord('A')
    else: 
        val = -1
    return val
def toggleBit(bitVec, index):
    if index<0:
        return bitVec
    mask = 1<<index
    return bitVec ^ mask
def maxOneBitOn(bitVec):
    return (bitVec & (bitVec -1)) == 0 # true if only one or 0 bits are on


def checkPalindromePermutation(st):
    # using a hash table
    """
    arr = set()
    arrLen=0
    for s in st:
        if s == " ":
            continue
        if s.lower() in arr:
            arr.remove(s.lower())
            arrLen -=1
        else:
            arr.add(s.lower())
            arrLen +=1
    return arrLen<=1
"""
    # with a bit vector
    bitVec = 0
    for c in st:
        val = charVal(c)
        bitVec = toggleBit(bitVec, val)
   # print(bin(bitVec))
    return maxOneBitOn(bitVec)



def test_checkPalindromePermutation():
    print("start test_checkPalindromePermutation ")
    assert(checkPalindromePermutation("Tact Coa")==True)
    assert(checkPalindromePermutation("Tact Copa")==False)
    assert(checkPalindromePermutation("Tact Co@a")==True)
    assert(checkPalindromePermutation("sdfghj@#$%^78 ")==False)
    print("end testing")

# 1.5 One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, pal-> true
# pales. pale -> true
# pale .bale-> true
# pale.bake-> false

def oneAway(st1,st2):
    edits = 0 
    if -1< (len(st1) - len(st2))>1:
        return False
    i=0
    j=0
    while i <len(st1)-1 and j <len(st2)-1:
        if st1[i] != st2[j]:
            if st1[i+1] == st2[j+1]:
                edits +=1
                i+=1
                j+=1
            elif st1[i] == st2[j+1]:
                edits +=1
                i+=1
                j+=2
            elif st1[i+1] == st2[j]:
                edits +=1
                i+=2
                j+=1    
        else:
            i+=1
            j+=1
        if edits>1: return 0

    if edits == 0: return True
    if i==j and len(st1) ==len(st2):
        return  st1[i] == st2[j]
    else:
        return False
    

def test_oneAway():
    print("start test_oneAway ")
    assert(oneAway("pale", "pal")== True)
    assert(oneAway('pales', 'pale')== True)
    assert(oneAway('pale' ,'bale')== True)
    assert(oneAway('pale','bake')== False)
    
    print("end testing")

# 1.6 String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def stringCompress(st):
    
    nchr = st[0]
    arr = [nchr]
    counter = 0
    for c in st:
        if c == nchr:
            counter +=1
        else:
            arr.append(counter)
            
            arr.append(c)
            nchr = c
            counter = 1
    
    arr.append(counter)    
    
    return st  if len(arr)>= len(st) else "".join(arr) 


def test_stringCompress():
    print("start test_stringCompress ")
    assert(stringCompress("aabcccccaaa")=="a2b1c5a3")
    assert(stringCompress("asdfghj")=="asdfghj")
    
    print("end testing")
    
# 1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
#bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
def rotateMatrix(mat):
    #with O(n^2) space
    rotated = [[0 for c in range(len(mat))]for r in range(len(mat))]
    for r in range(len(mat)):
        for c in range(len(mat)):
            rotated[r][c] = mat[len(mat)-1 - c][r] 
    return rotated

def test_rotateMatrix():
    mat = matrixBulider(4)
    matrixPrinter(mat)
    matrixPrinter(rotateMatrix(mat))


def matrixBulider(n):
    mat = [[0 for c in range(n)]for r in range(n)]
    for r in range(n):
        for c in range(n):
            mat[r][c] = r,c
    return mat
    
def matrixPrinter(mat):
    for r in range(len(mat)):
        print(mat[r])
    print()


# 1.8 ero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to O.

# 1.9 String Rotation: Assume you have a method isSubst ring which checks if one word is a substring
# of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
# call to isSubstring (e .g. , "waterbottle " is a rotation of " erbottlewat").


    





def main():
    #test_isUnique()
    #test_checkPermutation()
    #test_URLify()
    #test_checkPalindromePermutation()
    #test_oneAway() 
    test_rotateMatrix()
    pass   

if __name__ == "__main__":
    main()