#include <iostream>

using namespace std;

void printArray(int a[], int size){
	int i;
	for (i = 0 ; i < size ; i++)
		cout << a[i] << ' ';
	cout << '\n';
}
int main(){  
	int x[3][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
	// printArray(x, 12);
	printArray(x[0], 12);
	printArray(x[1], 4);
	printArray(&x[1][2], 4);
	return 0;
}