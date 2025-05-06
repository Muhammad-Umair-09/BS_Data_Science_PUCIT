#include <iostream>
using namespace std;
int main(){
    int i=1,row;
    cout<< "Rows: ";
    cin >> row; 
    for (;i<=row*5;i++){
        cout<< i<< " ";
        if (i%5==0)cout<<"\n";
    };
}
