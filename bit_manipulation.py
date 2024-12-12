
#5.1
# Insertion: You are given two 32-bit numbers, Nand M, and two bit positions, i and
# j. Write a method to insert Minto N such that M starts at bit j and ends at bit i. You
# can assume that the bits j through i have enough space to fit all of M. That is, if
# M = 10011, you can assume that there are at least 5 bits between j and i. You would not, for
# example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.
def insertion(m,n,i,j):
    newn = n<<i
    bitMask = (~0)<<j # 0 until bit j
    bitMask = bitMask | (2**i -1) #2**i = 1 bit on after i, (2**i)-1 = all 1 before i
    m = m & bitMask
    res = m|n
    return res

#dgk
     

def main():
    pass
if __name__ == "__main__":
    main()