#include <iostream>
using namespace std;
int main(){
   int row,sSpace=0,midSpaxce;
   cout<< "N: ";
   cin>>row;
   if (row==2)midSpaxce=3;
   else midSpaxce=(row-2)*4+3;
   for (;row>0;row--){
        for (int sp=0;sp<sSpace;sp++)cout<<" ";
        if (row-1!=0){
            cout<<"|_";
            for (int ss=0;ss<midSpaxce;ss++)cout<<" ";
            cout<<"_|"<<endl;
        }
        else cout<<"|_|"<< endl;
        midSpaxce-=4;
        sSpace+=2;
    }

   }


