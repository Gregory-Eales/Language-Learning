//
// Created by Greg Eales on 8/6/18.
//
#include "NeuralNet.h"
#include <iostream>
#include <cmath>
#include <vector>


using namespace std;

int NeuralNet::Forward(){
    cout<<"Forward Success"<<endl;
}

int NeuralNet::BackProp(){
    cout<<"Back Propagation Success"<<endl;
}

int NeuralNet::GetResults(){
    cout<<"Get Results Success"<<endl;
}

void NeuralNet::saveVector(vector<double> vec){
    for(int i=0; i<=vec.size(); i++){

    }
}

long double NeuralNet::Sigmoid(long double z){
    long double ans = 2.000/(1.000+exp(double(-z))) - 1.000 ;
    return ans;
}
