#include <iostream>
using namespace std;

class Student{
    string name;
    int age,marks;

    public:
        Student(){
        name="Name";
        age=5;
        marks=50;
    }

    void setAge(int x){
        if (x>=5 && x<=20)
            age=x;
    }

    void setMarks(int m){
        if (m>=0 && m<=100)
            marks=m;
    }

    void setName(string s){
        if (s.size()<3)
            name="Unknown";
        else 
            name=s;
    }

    string getName(){
        return name;
    }

    int getAge(){
        return age;
    }

    int getMarks(){
        return marks;
    }

    void printStudentDetails(){
        cout<<name<<' '<<age<<' '<<marks<<endl;
    }

    bool isPassed(){
        return (marks>=50);
    }

    char getGrade(){
        if (marks>=85)
            return 'A';
        if (marks>=70)
            return 'B';
        if (marks>=50)
            return 'C';
        return 'F';
    }
};


int main(){
    Student s1;
    s1.setName("Umair");
    s1.setAge(23);
    s1.setMarks(83);
    cout<< "passed "<< s1.isPassed()<<endl;
    cout<< "grade "<<s1.getGrade()<<endl;
    cout<< "get name "<< s1.getName()<<endl;
    cout<< "get age "<< s1.getAge()<<endl;
    cout<< "get marks "<< s1.getMarks()<<endl;
    cout<< "student details ";
    s1.printStudentDetails();



    return 0;
}