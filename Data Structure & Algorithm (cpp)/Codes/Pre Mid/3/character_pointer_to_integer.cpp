#include <iostream>

using namespace std;

int main(){  
	int x = (68 << 24) + (67 << 16) + (66 << 8) + 65;
	cout << "X: " << x << '\n';
	char *c = (char*) &x;
	cout << "First Byte:\t" << c[0] << ' ' << (int)c[0] << '\n';
	cout << "Second Byte:\t" << c[1] << ' ' << (int)c[1] << '\n';
	cout << "Third Byte:\t" << c[2] << ' ' << (int)c[2] << '\n';
	cout << "Fourth Byte:\t" << c[3] << ' ' << (int)c[3] << '\n';
	return 0;
}