//
// Created by Greg Eales on 8/20/18.
//

#ifndef TICTACTOE_TICTACTOE_H
#define TICTACTOE_TICTACTOE_H

#include <vector>
#include <string>

using namespace std;

class TicTacToe {
public:
    // shows the state of the game
    void PrintGame(vector<string> spaces);
    // creates an empty board
    vector<string> InitBoard();
    // runs the main game loop
    void Play();
    // checks for a winner
    bool CheckWinner(vector<string> Board);
    // asks the player for their move
    int GetMove(vector<string> Board);
    // checks for a draw
    bool CheckDraw(vector<string> board);


};


#endif //TICTACTOE_H
