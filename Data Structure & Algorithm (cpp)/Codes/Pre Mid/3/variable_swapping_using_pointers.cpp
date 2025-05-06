#include <iostream>

using namespace std;

void swap(int* a, int* b){
	int temp = *a;
	*a = *b;
	*b = temp;
}
int main(){  
	int x = 23, y = 45, *a = &x;
	cout << "X: " << x << " Y: " << y << '\n';
	swap(&x, &y);
	cout << "X: " << x << " Y: " << y << '\n';
	return 0;
}