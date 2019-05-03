#include <iostream>
#include "NeuralNet.h"
#include <fstream>
#include <cmath>
#include <vector>
#include <iomanip>

long double Sigmoid(long double z){
    long double ans = 2.000/(1.000+exp(double(-z))) - 1.000 ;
    return ans;

using namespace std;

int main(){
    NeuralNet NN;
    ofstream file;
    file.open("Data.txt");
    for(int i=-100; i<100; i++) {
        file << setprecision(5) << NN.Sigmoid((i)/10.0000) <<endl;
    }
    file.close();







    return 0;





}