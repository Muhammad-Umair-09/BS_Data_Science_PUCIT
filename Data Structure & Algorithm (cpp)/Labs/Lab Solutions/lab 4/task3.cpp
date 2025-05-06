#include <iostream>
#include "time.h"
#include "cstdlib"
using namespace std;

void printArray(int a[], int size){
int i;
for (i = 0 ; i < size ; i++)
	cout << a[i] << ' ';
cout << '\n';
}

int main(){
    int roll_no[30],marks[30],count=0;
    srand(time(0));
    for (int i=0;i<30;i++){
        roll_no[i]=i+1;
        marks[i]=rand()%101;
    }
    cout<<"Marks: ";
    printArray(marks,30);
    cout<<"ROll_NO ";
    printArray(roll_no,30);

    for (int i=0;i<5;i++){
        marks[rand()%30]=-1;
    }
    cout<<"Marks: ";
    printArray(marks,30);

    cout<<"Roll_no        Marks\n";
    for (int i=0;i<30;i++){
        if (marks[i]!=-1){
            cout<<roll_no[i] <<"              "<<marks[i]<<'\n';
            count++;
        }
        
    }
    cout<<"count "<<count<<"\n";
    int new_marks[count],new_roll_no[count],j=0;
    for (int i=0;i<30;i++){
        if (marks[i]!=-1){
            new_marks[j]=marks[i];
            new_roll_no[j]=roll_no[i];
            j++;
        }
    }
    cout<< "Roll_No: ";
    printArray(new_roll_no,count);
    cout<< "Marks: ";
    printArray(new_marks,count);

   return 0;
}