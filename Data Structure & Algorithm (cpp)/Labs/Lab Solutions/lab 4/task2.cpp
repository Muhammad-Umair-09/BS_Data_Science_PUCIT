#include <iostream>
using namespace std;


void printArray(int a[], int size){
    int i;
    for (i = 0 ; i < size ; i++)
	    cout << a[i] << ' ';
    cout << '\n';
}

int main(){
    int i=0,j=0,ar1[10],ar2[10],temp;
    for (int i=0;i<10;i++){
        ar1[i]=rand()%100;
        ar2[i]=i+1;
    }
    cout<<"ar1: ";
    printArray(ar1,10);
    cout<<"ar2: ";
    printArray(ar2,10);

    //bubble sort
    for (i=0;i<10;i++){
        for (j=0;j+1<10-i;j++){
            if (ar1[j]>ar1[j+1]){
                temp=ar1[j];
                ar1[j]=ar1[j+1];
                ar1[j+1]=temp;

                temp=ar2[j];
                ar2[j]=ar2[j+1];
                ar2[j+1]=temp;
            }
        }
    }
    
    for (int i=0;i<10;i++){
        cout<<ar1[i]<<" at position "<<ar2[i]<<'\n';
    }
    
   return 0;
}