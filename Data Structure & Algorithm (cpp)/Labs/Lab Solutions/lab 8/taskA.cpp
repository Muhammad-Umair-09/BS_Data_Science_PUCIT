#include <iostream>
using namespace std;
//print array
void showarr(int *ar,int size,int i=0){
        if (i<size){
            cout<< ar[i]<<' ';
            showarr(ar,size,i+1);
        }
}

int main(){
    int a[]={1,2,3,4,5,6,7,2,3,5,4,3,5,10};
    showarr(a,14);
   return 0;
}