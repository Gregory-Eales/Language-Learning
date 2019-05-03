#include "Basics.hpp"
#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

// the void in front of the function indicates that the funtion doesnt return anything
void print_program(){
    cout<<"Program Success"<<endl;
}

// this function doubles an integer value and returns it
int double_number(int x){
    return 2*x;
}

// this funtion tales two variables and adds them
// notice that the variable c was pre-declared to be a int value
int adder(int a, int b){
    int c;
    c = a + b;
    return c;
}

// initiates two variables of type const and constexpr
// const is essentially a promise to the interpreter not to change the value
// constexpr means that the value is to remain constant after the code is compiled
int const_creator(){
    const int x = 1;
    return x;
}









