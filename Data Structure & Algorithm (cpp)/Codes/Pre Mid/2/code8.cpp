#include <iostream>

using namespace std;

void swap(int a[], int i, int j){
	int temp = a[i];
	a[i] = a[j];
	a[j] = temp;
}
void sort(int a[], int size){
	int i, j;
	for (i = 0 ; i < size ; i++)
		for (j = 0 ; j + 1 < size ; j++)
			if (a[j] > a[j + 1])
				swap(a, j, j+1);
}
void printArray(int a[], int size){
	int i;
	for (i = 0 ; i < size ; i++)
		cout << a[i] << ' ';
	cout << '\n';
}
int main(){  
	int x[] = {41, 23, 31, 14, 52, 16, 27, 18, 39};
	sort(x, 9);
	printArray(x, 9);
	return 0;
}