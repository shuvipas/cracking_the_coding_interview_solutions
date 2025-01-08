
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
    for i in range(32):
        if int(num) != num:
            break
        num *=2

if int(num) != num:
    print("ERROR")
else:
    print(bin(num))

# 5.3 Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to
# find the length of the longest sequence of 1 s you could create.
# EXAMPLE
# Input: 1775 (or: 11011101111)
# Output: 8


def main():
    pass
if __name__ == "__main__":
    main()