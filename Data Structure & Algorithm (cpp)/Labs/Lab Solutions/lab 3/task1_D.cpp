#include <iostream>
using namespace std;
int main(){
    char a=65;
    int row;
    cout<< "Rows: ";
    cin>>row;
    for (int i=1;i<=row;i++){
        for (int j=1;j<=4;j++){
            cout<<a<< " ";
            a++;
        }
        cout<<endl;
    }
    
}
