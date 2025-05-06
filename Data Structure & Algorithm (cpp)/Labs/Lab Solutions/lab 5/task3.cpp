#include <iostream>
#include <vector>
using namespace std;

class Library{
    string libraryName;
    vector<string> books;
    
    public:
        Library(string l){
            libraryName=l;
            
    }

    vector<string> getBooks(){
        return books;
    }

    void setBooks(vector<string> x){
        books=x;
    }

    string getLibraryName(){
        return libraryName;
    }
    void setLibraryName(string x){
        libraryName=x;
    }



    void addBook(string title){
        books.push_back(title);
    }

    void removeBook(const string& title){
        int i;
        for (i=0;i<books.size();i++){
            if (books[i]==title){
                string temp=books[i];
                books[i]=books[books.size()-1];
                books[books.size()-1]=temp;
                books.pop_back();
                break;
            }
        }
    }

    int totalBooksCounts(){
        return books.size();
    }

    void printLibraryDetails(){
        cout<<"Library Name: "<< libraryName<<'\n'<<"List of Books: "<<endl;
        for (string s:books){
            cout<<s<<endl;
        }
    }



};


int main(){
    Library lib("Iqbal");
    cout<< "get library name "<< lib.getLibraryName()<<endl;
    lib.setLibraryName("Hameed");
    cout<< "get library name "<< lib.getLibraryName()<<endl;
    vector<string> s =  lib.getBooks();
    lib.removeBook("Book 4");

    lib.addBook("Book 1");
    lib.addBook("Book 2");
    lib.addBook("Book 3");
    lib.addBook("Book 4");
    lib.addBook("Book 5");
    lib.addBook("Book 6");
    lib.addBook("Book 7");
    lib.addBook("Book 8");
    cout<< "Library details "<<endl;
    lib.printLibraryDetails();
    cout<<endl;
    lib.removeBook("Book 4");
    cout<<endl;
    cout<< "Library details "<<endl;
    lib.printLibraryDetails();
    cout<<endl;
    cout<<"total count of books: "<<lib.totalBooksCounts()<<endl;

   
    


    return 0;
}