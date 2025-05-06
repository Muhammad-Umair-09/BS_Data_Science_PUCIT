#include <iostream>
using namespace std;

int main(){
    //
    int marks;
    cout<< "Enter Marks: ";
    cin>> marks;
    if (marks>84)cout<< "Grade: A"; 
    else if (marks>79)cout<< "Grade: A-"; 
    else if (marks>74)cout<< "Grade: B+"; 
    else if (marks>69)cout<< "Grade: B"; 
    else if (marks>64)cout<< "Grade: B-"; 
    else if (marks>60)cout<< "Grade: C+"; 
    else if (marks>57)cout<< "Grade: C"; 
    else if (marks>54)cout<< "Grade: C-"; 
    else if (marks>49)cout<< "Grade: D"; 
    else cout<< "Grade: D ";
    
    cout<<endl;
    if (marks>84)cout<< "Grade: A"; 
    if (marks>79 && marks<85)cout<< "Grade: A-"; 
    if (marks>74 && marks<80)cout<< "Grade: B+"; 
    if (marks>69 && marks<75)cout<< "Grade: B"; 
    if (marks>64 && marks<70)cout<< "Grade: B-"; 
    if (marks>60 && marks<65)cout<< "Grade: C+"; 
    if (marks>57 && marks<61)cout<< "Grade: C"; 
    if (marks>54 && marks<58)cout<< "Grade: C-"; 
    if (marks>49 && marks<55)cout<< "Grade: D"; 
    if (marks<50)cout<< "Grade: D ";

    return 0;
}
