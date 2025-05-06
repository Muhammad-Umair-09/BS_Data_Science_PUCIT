#include <iostream>

using namespace std;

int main(){  
	int x1[5] = { 23, 45, 16, 49, 33};
	int x2[5] = { 12, 34, 19, 94, 43};
	int x3[5] = { 32, 51, 62, 91, 63};
	int i, *a, sum1 = 0, sum2 = 0, sum3 = 0;
	for (i = 0 ; i < 5 ; i++){
		sum1 += x1[i];
		sum2 += x2[i];
		sum3 += x3[i];
	}
	a = x2;
	if (sum1 > sum2 && sum2 > sum3)			a = x1;
	else if (sum3 > sum2 && sum3 > sum1)	a= x3;
	for (i = 0 ; i < 5 ; i++, a++)
		cout << a[0] << ' ';
	cout << '\n';
	return 0;
}