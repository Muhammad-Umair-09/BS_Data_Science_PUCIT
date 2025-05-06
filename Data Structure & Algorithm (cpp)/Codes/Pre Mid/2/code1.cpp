#include <iostream>

using namespace std;

int g = 5;
const int gc = 1000;

void f1(){
	cout << "F1: " << g << ' ' << gc << ' ';
	//gc++;			//uncomment this line to check error to modify a constant variable
	g++;
	cout << g << '\n';
}
void f2(){
	cout << "F2: " << g << ' ' << gc << ' ';
	g+=5;
	cout << g << '\n';
}
int main(){  
	cout << "Main: " << g << ' ' << gc << ' ';
	f1();
	cout << "Main: " << g << ' ' << gc << ' ';
	f2();
	cout << "Main: " << g << ' ' << gc << ' ';
	return 0;
}