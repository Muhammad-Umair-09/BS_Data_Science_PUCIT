#include <iostream>
#include <vector>

using namespace std;

int vESumNegativeOne (vector<int>& v, int i){
	if (i == v.size())	return -1;
	int sum = vESumNegativeOne(v, i+1);
	if (v[i] % 2) return sum;
	if (sum == -1)	return v[i];
	return v[i] + sum;
}
//The function will return -1 if there is no even value
int vESumNegativeOne (vector<int>& v){
	return vESumNegativeOne(v, 0);
}
int main(){
	vector<int> v1 = {2,3,1,4,6,9};
	cout << vESumNegativeOne(v1) << '\n';
	vector<int> v2 = {3,1,9,5};
	cout << vESumNegativeOne(v2) << '\n';
	return 0;
}