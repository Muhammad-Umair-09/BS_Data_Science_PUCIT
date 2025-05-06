#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
	srand(time(0));					//to change random seed with latest time
    int i, j, min, temp, x[20];
    for (i = 0 ; i < 20 ; i++){
    	x[i] = rand();				//initialize with random value
    	cout << x[i] << ' ';
	}
	cout << '\n';
	//insertion sort
	for (i = 1 ; i < 20 ; i++){
		temp = x[i];
    	for (j = i - 1 ; j >= 0 && x[j] > temp ; j--)
    		x[j + 1] = x[j];
    	x[j + 1] = temp;
	}
    for (i = 0 ; i < 20 ; i++)
    	cout << x[i] << ' ';
	cout << '\n';
    return 0;
}
