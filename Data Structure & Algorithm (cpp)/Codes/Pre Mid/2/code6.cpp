#include <iostream>

using namespace std;

//Carefully observe the range of elements handled by the function
void printArray(int a[], int size){
	int i;
	for (i = 0 ; i < size ; i++)
		cout << a[i] << ' ';
	cout << '\n';
}
int main(){  
	int x[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
	printArray(x, 9);
	printArray(x, 5);
	printArray(&x[3], 4); 
	printArray(&x[2], 6);
	return 0;
}