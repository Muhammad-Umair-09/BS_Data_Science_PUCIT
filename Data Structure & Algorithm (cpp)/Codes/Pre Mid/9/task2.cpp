#include <iostream>
#include <vector>

using namespace std;

int vESum (vector<int>& v, int i){
	if (i == v.size())	return 0;
	int sum = vESum(v, i+1);
	if (v[i] % 2) return sum;
	return v[i] + sum;
}
int vESum (vector<int>& v){
	return vESum(v, 0);
}
int main(){
	vector<int> v = {2,3,1,4,6,9};
	cout << vESum(v) << '\n';
	return 0;
}