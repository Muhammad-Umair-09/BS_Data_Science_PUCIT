#include<iostream>
using namespace std;
#include<vector>
#include<string>
#include<algorithm>
int main(){
    vector<pair<char,int>> freq(26,pair<char,int>('0',0));
    string s="DACDADCBC";
    for (char c:s){
        freq[c-'A'].first=c;
        freq[c-'A'].second++;
    }
    sort(freq.begin(), freq.end(),[](const pair<int,int>& a,const pair<int,int>& b){if(a.second==b.second)return a.first<b.first; return a.second < b.second;});

    for (auto p:freq){
        for(int i=0;i<p.second;i++) cout<<p.first;
    }
    return 0;
}