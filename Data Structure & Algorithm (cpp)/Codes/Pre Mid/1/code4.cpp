#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
	srand(time(0));					//to change random seed with latest time
    int i, j, x[10];
    for (i = 0 ; i < 10 ; i++){
    	x[i] = rand();				//initialize with random value
    	cout << x[i] << ' ';
	}
	cout << '\n';
	//print pattern
	for (i = 0 ; i < 10 ; i++){
    	for (j = 0 ; j <= i ; j++)
			cout << x[j] << ' ';
		cout << '\n';
	}
    return 0;
}
