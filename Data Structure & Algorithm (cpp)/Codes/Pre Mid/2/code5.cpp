#include <iostream>

using namespace std;

//Carefully observe the range of elements handled by the function
int getSum(int a[], int size){
	int i, sum = 0;
	for (i = 0 ; i < size ; i++)
		sum += a[i];
	return sum;
}
int main(){  
	int x[] = {3, 5, 2, 1, 7, 8, 4, 6, 9};
	cout << "Sum (0 - 8): " << getSum(x, 9) << '\n';
	cout << "Sum (0 - 6): " << getSum(x, 7) << '\n';
	cout << "Sum (2 - 5): " << getSum(&x[2], 4) << '\n';
	
	return 0;
}