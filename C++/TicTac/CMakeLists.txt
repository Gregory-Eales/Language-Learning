cmake_minimum_required(VERSION 3.10)
project(OpenCog)

set(CMAKE_CXX_STANDARD 17)

add_executable(OpenCog main.cpp AtomSpace/Atoms.cpp AtomSpace/Atoms.h NeuralNetwork.cpp NeuralNetwork.h TicTacToe.cpp TicTacToe.h)