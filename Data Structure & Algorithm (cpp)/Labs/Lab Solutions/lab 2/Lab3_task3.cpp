#include <iostream>
using namespace std;
int main(){
    cout<<"Enter three numbers: ";
    int n1,n2,n3;
    cin>> n1>> n2>> n3;
    if (n1<=n2 && n2<=n3)cout<< n1<<" "<< n2<<" "<< n3;
    if (n1<=n3 && n3<=n2)cout<< n1<<" "<< n3<<" "<< n2;
    if (n2<=n1 && n1<=n3)cout<< n2<<" "<< n1<<" "<< n3;
    if (n2<=n3 && n3<=n1)cout<< n2<<" "<< n3<<" "<< n1;
    if (n3<=n1 && n1<=n2)cout<< n3<<" "<< n1<<" "<< n2;
    if (n3<=n2 && n2<=n1)cout<< n3<<" "<< n2<<" "<< n1;
}