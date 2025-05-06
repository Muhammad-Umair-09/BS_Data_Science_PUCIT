#include <iostream>
using namespace std;
int main(){
   int row,midSpaxce;
   cout<< "N: ";
   cin>>row;
   midSpaxce=row*2-3;
   for (int i=0;i<row;i++){
        for (int ss=0;ss<i;ss++)cout<<" ";
        cout<<"*";
        for (int ss=0;ss<midSpaxce;ss++)cout<<" ";
        if (row!=i+1)
        cout<<"*"<< endl;
        midSpaxce-=2;
    }

   }


