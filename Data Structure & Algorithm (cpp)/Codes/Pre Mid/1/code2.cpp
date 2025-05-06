#include <iostream>

using namespace std;

int main() {
    int n;
    do{
    	cout << "Enter Number in Range (10-99): ";
		cin >> n; 
	}while (n < 10 || n > 99);
	cout << "N: " << n << '\n';
    return 0;
}
