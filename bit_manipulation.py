
def getBit(num, i):
    return int(num&(1<<i)!=0)

def setBit(num, i):
    return num|(1<<i)
def clearBit(num, i):
    mask = ~(1<<i)
    return num&mask
def clearBitsFromI2MSB(num, i):
    mask = (1<<i)-1 
    return num&mask
def clearBitsFromZero2I(num, i):
    mask = -1<<(i+1) # -1 == ~0 ==all 1'
    return num&mask
def updateBit(num, i,val): #val == 1,0
    mask = ~(1<<i)
    return (num&mask)|val<<i
def numOfOnes(num):
    count =0
    while num:# !=0
        """
        time as the number of bits
        count += num&1
        num >>=1 """
        # Brian Kernighan’s Algorithm: 
        # time as the number of ones
        num = (num&(num-1)) # clearing the lowest 1' bit
        count +=1
    return count


#5.1
# Insertion: You are given two 32-bit numbers, N and M, and two bit positions, i and
# j. Write a method to insert M into N such that M starts at bit j and ends at bit i. You
# can assume that the bits j through i have enough space to fit all of M. That is, if
# M = 10011, you can assume that there are at least 5 bits between j and i. You would not, for
# example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.
def insertion(m,n,i,j):
    """
    bitMask = (~0)<<j # 0' until bit j then 1'
    bitMask = bitMask | (2**i -1) #2**i = 1 bit on after i, (2**i)-1 = all 1 before i
    m = m & bitMask
    res = m|n
    """
    newN = clearBitsFromZero2I(n,j)|clearBitsFromI2MSB(n,i) #cleard from i to j
    res = newN | m<<j
    return res
# 5.2 Binary to String: Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double,
# print the binary representation. If the number cannot be represented accurately in binary with at
# most 32 characters, print "ERROR:

def bin2string(num):
    strBin = ""
    for i in range(32):
        if int(num) == num:
            break
        num *=2
        val = 0
        if num >1:
            val = 1
            num -=1
        strBin.append(val)

if int(num) != num:
    print("ERROR")
else:
    print(strBin)

# 5.3 Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to
# find the length of the longest sequence of 1 s you could create.
# EXAMPLE
# Input: 1775 (or: 11011101111)
# Output: 8
def flipBit(num):
    longest = 0
    posi = 0
    pre= 0 #first contur
    curr = 0
    
    strNum = str(bin(num))[2:]
    for i in range(strNum):
        if strNum[i] =='1':
            curr+=1
        else:
            if pre +1 >longest:
                posi = i
                longest = pre +1


# 5.4 Next Number: Given a positive integer, print the next smallest and the next largest number that
# have the same number of 1 bits in their binary representation 
def nextNum(num): 

# 5.6 Conversion: Write a function to determine the number of bits you would need to flip to convert
# integer A to integer B.
# EXAMPLE
# Input: 29 (or: 11101), 15 (or: 01111)
# Output: 2

def conversion(a,b):
    num = a^b
    return numOfOnes(num)

# 5.7 Pairwise Swap: Write a program to swap odd and even bits in
#  an integer with as few instructions as possible 
# (e.g ., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on)
def pairSwipe(num):
    evenMask = int('0xaaaaaaa', 16) #bin(int('0xaaaaaaa', 16)) '0b1010101010101010101010101010'
    oddMask = int('0x5555555', 16)
    odd = (num>>1)&oddMask
    even = (num<<1)&evenMask
    return odd|even

# 5.8 Draw Line: A monochrome screen is stored as a single array of bytes, allowing eight consecutive
# pixels to be stored in one byte. The screen has width w, where w is divisible by 8 (that is , no byte will
# be spl it across rows) . The height of the screen, ofcourse, can be derived from the length of the array
# and the width . Implement a function that draws a horizontal line from (xl, y) to (x2, y).
# The method signature should look something like :
# drawL i ne(byte[] screen, int width, int Xl , int x2 , int y)


def main():
    pass
if __name__ == "__main__":
    main()