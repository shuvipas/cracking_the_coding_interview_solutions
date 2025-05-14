#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdint.h>
void print_binary(unsigned int val) {
    int bits = sizeof(val) * 8; // Calculate the number of bits in the type
    for (int i = bits - 1; i >= 0; i--) {
        putchar((val & (1u << i)) ? '1' : '0');
    }
    putchar('\n');
}
int insertion(int n, int m, int i,int j ){
    int right_mask = (1<<i)-1;
    int left_mask = -1<<(j+1);
    int mask = left_mask|right_mask;
    print_binary(mask);
    n &= mask;
    print_binary(n);
    n |= m<<i;
    return n;
}
void insertion_test(){
    print_binary(45);
    print_binary(insertion(45,3,2,4));
}
int main(){
    insertion_test();
}