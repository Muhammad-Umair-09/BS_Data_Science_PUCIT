#include <iostream>
using namespace std;

void printArray(int a[], int size){
int i;
for (i = 0 ; i < size ; i++)
	cout << a[i] << ' ';
cout << '\n';
}

int main(){
    int ar1[10],ar2[10],ar3[20],i=0,j=0,k=0;
    ar1[0]=3;
    ar2[0]=9;
    for (int i=1;i<10;i++){
        ar1[i]=(rand()%5+ar1[i-1]);
        ar2[i]=(rand()%5+ar2[i-1]);
    }
    
    cout<<"ar1: ";
    printArray(ar1,10);
    cout<<"ar2: ";
    printArray(ar2,10);

    while (i<10 && j<10){
        if (ar1[i]<ar2[j]){
            ar3[k]=ar1[i];
            i++;
        }
        else{ 
        ar3[k]=ar2[j];
        j++;
        }
        k++;
    }
    if (i<10){
        while (i<10){
            ar3[k]=ar1[i];
            i++;
            k++;

        }
    }
    else{
        while (j<10){
            ar3[k]=ar2[j];
            k++;
            j++;
        }
        }
        cout<<"ar3: ";
    printArray(ar3,20);
    

    
   return 0;
}