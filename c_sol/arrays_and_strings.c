#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdint.h>




int is_permutation(const char*str1,const char*str2 ){
    int n1 = strlen(str1);
    int n2 = strlen(str2);
    if(n1!= n2) return 0;
    int arr1[26] ={0};
    int arr2[26] ={0};
    for(int i=0; i<n1; i++){
        arr1[str1[i]-'a']++;
        arr2[str2[i]-'a']++;
    }
    for(int i =0; i<26;i++){
        if(arr1[i]!= arr2[i]) return 0;
    }
    return 1;
}
void is_permutation_test(){
    char* str1 = "asdf";
    char* str2 = "fdsa";
    char* str3 = "asef";
    char* str4 = "asff";
    assert(is_permutation(str1,str2));
    assert(!is_permutation(str1,str3));
    assert(!is_permutation(str1,str4));

}


int is_unique(const char* str1){
    //On time 
    //O1 space
    //asuuming only small chars if not
    // use uint64 and avoid all non alpha
    int n = strlen(str1);
    if(n>26) return 0;
    //int arr[26] ={0};
    uint32_t arr =0;
    for (int c=0; c<n; c++){
        int c_num =str1[c]-'a';
        if(arr>>c_num & 1) return 0;
        uint32_t mask = 1<<c_num; 
        arr = arr|mask;
    }
    return 1;
}
void is_unique_test(){
    char* str1 = "asdfghjk";
    assert(is_unique(str1));
    char* str2 = "asdfghajk";
    assert(!is_unique(str2));

}
int main(){
    printf("start testing\n");
    is_unique_test();
    is_permutation_test();
    printf("finished testing");
    return 0;
}