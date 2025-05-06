#include <iostream>

using namespace std;

int main(){  
	int x[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
	cout << x << ' ' << &x[0] << ' ' << &x[1] << ' ' << &x[2]  << ' ' << &x[3] << '\n';
	cout << "Addresses in decimal: \n";	// for the time being ignore uintptr, 9tit is unsighbinar
	cout << (uintptr_t)(x) << ' ' << (uintptr_t)&x[0] << ' ' << (uintptr_t)&x[1] << ' ' << (uintptr_t)&x[2]  << ' ' << (uintptr_t)&x[3] << '\n';
	return 0;
}