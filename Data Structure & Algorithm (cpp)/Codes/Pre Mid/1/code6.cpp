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
	//selection sort
	for (i = 0 ; i < 20 ; i++){
		min = i;
    	for (j = i + 1 ; j < 20 ; j++)
    		if (x[min] > x[j])
    			min = j;
		temp = x[i];
		x[i] = x[min];
		x[min] = temp;
	}
    for (i = 0 ; i < 20 ; i++)
    	cout << x[i] << ' ';
	cout << '\n';
    return 0;
}
