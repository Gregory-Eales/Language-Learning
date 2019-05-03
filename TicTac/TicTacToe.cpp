//
// Created by Greg Eales on 8/20/18.
//

#include "TicTacToe.h"
#include <iostream>
#include <vector>
#include <string>

using namespace std;

// show the state of the board
void TicTacToe::PrintGame(vector<string> spaces){
    cout<<spaces[0]<<" | "<<spaces[1]<<" | "<<spaces[2]<<endl;
    cout<<"- - - - -"<<endl;
    cout<<spaces[3]<<" | "<<spaces[4]<<" | "<<spaces[5]<<endl;
    cout<<"- - - - -"<<endl;
    cout<<spaces[6]<<" | "<<spaces[7]<<" | "<<spaces[8]<<endl;
}

// initiates the board
vector<string> TicTacToe::InitBoard(){
    vector<string> spaces = {" ", " ", " ", " ", " ", " ", " ", " ", " "};
    return spaces;
}

// checks for a winner
bool TicTacToe::CheckWinner(vector<string> Board){
    bool winner = false;
    for(int i=1; i < 9; i+=3) {
        if ((Board[i] == Board[i + 1]) && (Board[i + 1] == Board[i + 2]) && (Board[i] != " ")) {
            cout << Board[i] << " wins the match!" << endl;
            winner = true;
        }

        if ((Board[i] == Board[i + 3]) && (Board[i + 3] == Board[i + 6]) && (Board[i] != " ")) {
            cout << Board[i] << " wins the match!" << endl;
            winner = true;
        }
    }

    if((Board[0] == Board[4]) && (Board[4] == Board[8]) && (Board[0] != " ")){
        cout << Board[0] << " wins the match!" << endl;
        winner = true;
    }

    if((Board[2] == Board[4]) && (Board[4] == Board[6]) && (Board[2] != " ")){
        cout << Board[2] << " wins the match!" <<endl;
        winner = true;
    }


    return winner;
}

// checks for a draw
bool TicTacToe::CheckDraw(vector<string> Board){
    bool draw = true;
    for(int i=0; i<9; i++){
        if(Board[i] == " "){
            draw = false;
        }
    }
    if(draw == true){
        cout<<"Its a draw!";
    }
    return draw;
}


// asks the player for their move
int TicTacToe::GetMove(vector<string> Board){
    int move;
    bool undecided = true;
    while (undecided){
        cout<<"Where would you like to move? (Square 1-9) "<<endl;
        cin>>move;

        if (Board[move-1] == " "){
            undecided = false;
        }

        else{
            cout<<"That is not a valid move, try again"<<endl;
        }
    }

    return move;
}

// makes a given move
vector<string> MakeMove(string player, int square, vector<string> Board){
    Board[square] = player;
    return Board;
}


// runs the main game loop
void TicTacToe::Play(){
    string Player1, Player2;
    Player1 = "X";
    Player2 = "O";
    bool playing, winner, draw;
    playing = true;
    winner = false;
    draw = false;
    int move;
    vector<string> Board = InitBoard();
    while(playing){
        // X's turn
        PrintGame(Board);
        move = GetMove(Board);
        Board = MakeMove(Player1, move-1, Board);
        winner = CheckWinner(Board);
        draw = CheckDraw(Board);
        if(winner or draw){
            playing = false;
            break;
        }

        // O's turn
        PrintGame(Board);
        move = GetMove(Board);
        Board = MakeMove(Player2, move-1, Board);
        winner = CheckWinner(Board);
        draw = CheckDraw(Board);
        if(winner or draw){
            playing = false;
            break;
        }



    }
}

