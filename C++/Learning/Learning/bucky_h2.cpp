//
//  bucky_h2.cpp
//  Learning
//
//  Created by Greg Eales on 11/2/18.
//  Copyright © 2018 Greg Eales. All rights reserved.
//

#include "bucky_h2.hpp"
#include <iostream>
#include <string>

using namespace std;

// This is a basic function that return nothing, indicated by void and has no perameters.
void funtion_boyo(){
    cout<<"This is a basic function!!!"<<endl;
}

// This is how you define a constuctor of a class in a cpp file
ClassBoyo::ClassBoyo(string name){
    cout<<"Your class has been construced"<<endl;
    cout<<"Your name is: "<<name<<endl;
}

// This is how you make a method of a class inside of a cpp file
int ClassBoyo::add_classy(int a, int b){
    cout<<a+b<<endl;
    return a+b;
}

void ClassBoyo::if_else_boyo(int age){
    
    if(age > 100){
        cout<<"Holy shit man, your really fucking old"<<endl;
    }
    
    if (age < 50) {
        cout<<"Hey man your still pretty young, you still got time"<<endl;
    } else {
        cout<<"Ehh your pretty old, but nothing crazy"<<endl;
    }
    
}

void ClassBoyo::while_boyo(int iterations){
    int x = 0;
    while(x < iterations){
        cout<<"This is a while statement"<<endl;
        x = x+1;
    }
    
    
}




