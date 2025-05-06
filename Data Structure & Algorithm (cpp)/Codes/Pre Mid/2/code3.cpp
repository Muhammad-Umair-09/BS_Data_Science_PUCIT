#include <iostream>

using namespace std;

//a, b & x are local variables, try to access them in other functions, there will be an error.
void f1(int a){
	cout << "F1: " << a << ' ';	
	a++;
	cout << a << '\n';
}
void f2(int b){
	cout << "F2: " << b << ' ';
	b+=5;
	cout << b << '\n';
}
int main(){  
	int x = 1111;		//local variable of main function
	cout << "Main: " << x << '\n';
	f1(x);
	cout << "Main: " << x << '\n';
	f2(x);
	cout << "Main: " << x << '\n';
	return 0;
}