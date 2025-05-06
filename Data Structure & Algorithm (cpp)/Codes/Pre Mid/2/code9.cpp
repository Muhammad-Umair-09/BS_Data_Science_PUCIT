#include <iostream>

using namespace std;

int main(){  
	int x[3][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
	cout << (uintptr_t)(x) << ' ' << (uintptr_t)x[0] << ' '  << (uintptr_t)&x[0][0] << ' ' << (uintptr_t)x[1] << ' ' << (uintptr_t)x[2] << '\n';
	int y[2][6] = {{1, 2, 3, 4, 5, 6}, {7, 8, 9, 10, 11, 12}};
	cout << (uintptr_t)y[0] << ' '  << (uintptr_t)y[1] << '\n';
	int z[4][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {10, 11, 12}};
	cout << (uintptr_t)z[0] << ' '  << (uintptr_t)z[1] << ' '  << (uintptr_t)z[2] << ' '  << (uintptr_t)z[3] << '\n';
	return 0;
}