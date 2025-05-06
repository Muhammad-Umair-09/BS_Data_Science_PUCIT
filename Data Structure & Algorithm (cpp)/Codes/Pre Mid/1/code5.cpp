#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
	srand(time(0));					//to change random seed with latest time
    int i, j, temp, x[20];
    for (i = 0 ; i < 20 ; i++){
    	x[i] = rand();				//initialize with random value
    	cout << x[i] << ' ';
	}
	cout << '\n';
	//bubble sort
	for (i = 0 ; i < 20 ; i++)
    	for (j = 0 ; j < 19 ; j++)
    		if (x[j] > x[j+1]){
    			temp = x[j];
    			x[j] = x[j+1];
    			x[j+1] = temp;
			}
    for (i = 0 ; i < 20 ; i++)
    	cout << x[i] << ' ';
	cout << '\n';
    return 0;
}
