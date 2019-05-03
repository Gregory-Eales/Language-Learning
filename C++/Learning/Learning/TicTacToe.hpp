//
//  TicTacToe.hpp
//  Learning
//
//  Created by Greg Eales on 11/1/18.
//  Copyright © 2018 Greg Eales. All rights reserved.
//

#ifndef TicTacToe_hpp
#define TicTacToe_hpp

#include <stdio.h>



#include <vector>
#include <iostream>
#include <fstream>

using namespace std;

bool check_winner(vector<int> board);

bool check_horizontal(vector<int> board);

bool check_vertical(vector<int> board);

void TicTacToe();




#endif /* TicTacToe_hpp */
