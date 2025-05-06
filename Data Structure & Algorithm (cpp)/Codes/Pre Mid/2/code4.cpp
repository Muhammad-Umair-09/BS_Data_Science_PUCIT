#include <iostream>

using namespace std;

void swap(int& a, int& b){
	int temp = a;
	a = b;
	b = temp;
}
int main(){  
	int x = 53, y = 67;		//local variable of main function
	cout << "X: " << x << "\tY: " << y << '\n';
	swap(x, y);
	cout << "X: " << x << "\tY: " << y << '\n';
	//swap(23, 62);		//uncomment this statement to check the error
	return 0;
}