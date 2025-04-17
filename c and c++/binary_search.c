#include <stdio.h>
int main(void){
    int search = 101;
    int arry[] = {1,2,3,4,5,6,10,20,30,40,50,60,70,80,81,92,101};

    int start = 0;
    int end = 7;
    int test  = 0/2;
    printf("test %d\n", test);
    while(start <= end){
        int mid = (end + start)/2;
        printf("mid %d\n", mid);
    if (arry[mid] == search){
        printf("found %d at index %d of the arry\n", search, mid);
        break;
    }
    if(arry[mid] < search){
        start = mid + 1;
    }
    else{
        end = mid -1;
    }

    }

}