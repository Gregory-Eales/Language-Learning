//
//  bucky_h1.cpp
//  Learning
//
//  Created by Greg Eales on 11/2/18.
//  Copyright © 2018 Greg Eales. All rights reserved.
//

#include "bucky_h1.hpp"
#include <iostream>

using namespace std;

// This functions shows the two different ways you can end a line in c++
void ways_to_print(){
    // you can end a line by putting a backslash n if you want
    cout<<"This is the first way\n";
    // alternativly you can add an endl which will also end the line
    cout<<"This is the second way"<<endl;
    // also you can do everything at once by including \n at after each word
    cout<<"this \n is \n printed \n on \n many \n lines \n";
    cout<<"This is the last line"<<endl;
}

// this function will ask a user for input
// and then print it back out to them
void parot_boy(){
    int a;
    cout<<"Tell me a number:"<<endl;
    // cin is what asks the user for input
    cin>>a;
    cout<<a<<endl;
    
}

// this function creates an if statement
void if_boyo(int a){
    if(a > 10){
        cout<<"Your number is a big boy"<<endl;
    }
}
