#include <iostream>
using namespace std;
int main(){
    int row,space;
    cout<< "Rows: ";
    cin>>row;
    space=row-1;
    for (int i=1;i<=row;i++){
        for (int x=0;x<space;x++)cout<< " ";
        space-=1;
        int num=i;
        while (num>0){
            cout<<num;
            num--;
        }
        num=2;
        while (num<=i){
            cout<<num;
            num++;
        }
        cout<< "\n";
    }
}
