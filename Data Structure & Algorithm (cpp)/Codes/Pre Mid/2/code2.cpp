#include <iostream>

using namespace std;

void f1(){
	int x = 11;			//local variable of f1 function
	cout << "F1: " << x << ' ';
	x++;
	cout << x << '\n';
}
void f2(){
	int x = 111;		//local variable of f2 function
	cout << "F2: " << x << ' ';
	x++;
	cout << x << '\n';
}
int main(){  
	int x = 1111;		//local variable of main function
	cout << "Main: " << x << '\n';
	f1();
	x++;
	cout << "Main: " << x << '\n';
	f2();
	x++;
	cout << "Main: " << x << '\n';
	return 0;
}