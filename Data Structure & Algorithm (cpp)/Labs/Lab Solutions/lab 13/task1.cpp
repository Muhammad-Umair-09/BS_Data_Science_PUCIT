#include <bits\stdc++.h>
using namespace std;
int main(){
    vector<int> digits = {4,5,6,7,5,6,5,5,6,5,4};
    
    map<int,int> lst;
    for(int i = 0 ; i < digits.size() ; i++) {
        lst[digits[i]]++;
    }
    bool f=0;
    for(int i = 0 ; i < digits.size() ; i++) {
        if(lst[digits[i]] == 1) {cout<<digits[i];f=1; break;}
    }
    if(!f)cout<<-1;
}