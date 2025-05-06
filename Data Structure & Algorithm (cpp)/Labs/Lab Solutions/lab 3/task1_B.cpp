#include <iostream>
using namespace std;
int main(){
    int row,col;
    cout<< "Rows Cols: ";
    cin>> row>>col;
    for (int i=1;i<=row;i++){
        int x=1,num=1,sum=0;
        for (;x<col;x++){
            cout<< num<<"+";
            sum+=num;
            num+=i;
        }
        cout<< num<<"="<<num+sum<<endl;
    }
}
