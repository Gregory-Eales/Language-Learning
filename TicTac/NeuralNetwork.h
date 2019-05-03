//
// Created by Greg Eales on 8/19/18.
//

#ifndef OPENCOG_NEURALNETWORK_H
#define OPENCOG_NEURALNETWORK_H

#include <iostream>
#include <vector>

using namespace std;

void test();

class NeuralNetwork {
public:

    void sigmoid();

    vector<float> Dot(vector<float> x, vector<float> theta);

    void train();

    void predict();



};


#endif //OPENCOG_NEURALNETWORK_H
