//
// Created by Greg Eales on 8/6/18.
//

#ifndef UNTITLED1_NEURALNET_H
#define UNTITLED1_NEURALNET_H
#include <vector>


class NeuralNet {
public:
    int Forward();
    int BackProp();
    int GetResults();
    long double Sigmoid(long double z);
    void saveVector(vector<double> vec);
};


#endif //UNTITLED1_NEURALNET_H
