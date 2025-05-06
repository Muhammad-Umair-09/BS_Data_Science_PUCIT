#include <iostream>
using namespace std;

class Course{
    string courseName;
    int courseCode,credits;

    public:
        Course(){
        courseName="COURSE";
        courseCode=0;
        credits=1;

    }

    void setCourseName(string x){
        courseName=x;
    }

    void setCourseCode(int m){
        if (m>0)
            courseCode=m;
    }

    void setCredits(int s){
        if (s>=1 && s<=3)
            credits=s;
    }

    string getCourseName(){
        return courseName;
    }

    int getCourseCode(){
        return courseCode;
    }

    int getCredits(){
        return credits;
    }

    void printCourseDetails(){
        cout<<"Course: "<< courseName<<" Code: "<<courseCode<<" Credits: "<<credits<<endl;
    }

    bool isGreater(Course& c){
        return credits>c.credits;
    }

};


int main(){
    Course c1,c2;
    c1.setCourseName("OOP");
    c1.setCourseCode(24);
    c1.setCredits(2);
    cout<< "Course details ";
    c1.printCourseDetails();
    cout<< "get course name "<< c1.getCourseName()<<endl;
    cout<< "get course code "<< c1.getCourseCode()<<endl;
    cout<< "get credits "<< c1.getCredits()<<endl;
    
    c2.setCourseName("Progranmming Fundamentals");
    c2.setCourseCode(23);
    c2.setCredits(3);
    cout<< "Course details ";
    c2.printCourseDetails();
    cout<< "get course name "<< c2.getCourseName()<<endl;
    cout<< "get course code "<< c2.getCourseCode()<<endl;
    cout<< "get credits "<< c2.getCredits()<<endl;
    cout<<"\n\n";
    cout<<"is credits of course 1 greater than course 2: "<< c1.isGreater(c2);
    


    return 0;
}