# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CLion.app/Contents/bin/cmake/bin/cmake

# The command to remove a file.
RM = /Applications/CLion.app/Contents/bin/cmake/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/gregeales/CLionProjects/TicTacToe

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/gregeales/CLionProjects/TicTacToe/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/OpenCog.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/OpenCog.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/OpenCog.dir/flags.make

CMakeFiles/OpenCog.dir/main.cpp.o: CMakeFiles/OpenCog.dir/flags.make
CMakeFiles/OpenCog.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/gregeales/CLionProjects/TicTacToe/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/OpenCog.dir/main.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/OpenCog.dir/main.cpp.o -c /Users/gregeales/CLionProjects/TicTacToe/main.cpp

CMakeFiles/OpenCog.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/OpenCog.dir/main.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/gregeales/CLionProjects/TicTacToe/main.cpp > CMakeFiles/OpenCog.dir/main.cpp.i

CMakeFiles/OpenCog.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/OpenCog.dir/main.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/gregeales/CLionProjects/TicTacToe/main.cpp -o CMakeFiles/OpenCog.dir/main.cpp.s

CMakeFiles/OpenCog.dir/main.cpp.o.requires:

.PHONY : CMakeFiles/OpenCog.dir/main.cpp.o.requires

CMakeFiles/OpenCog.dir/main.cpp.o.provides: CMakeFiles/OpenCog.dir/main.cpp.o.requires
	$(MAKE) -f CMakeFiles/OpenCog.dir/build.make CMakeFiles/OpenCog.dir/main.cpp.o.provides.build
.PHONY : CMakeFiles/OpenCog.dir/main.cpp.o.provides

CMakeFiles/OpenCog.dir/main.cpp.o.provides.build: CMakeFiles/OpenCog.dir/main.cpp.o


CMakeFiles/OpenCog.dir/AtomSpace/Atoms.cpp.o: CMakeFiles/OpenCog.dir/flags.make
CMakeFiles/OpenCog.dir/AtomSpace/Atoms.cpp.o: ../AtomSpace/Atoms.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/gregeales/CLionProjects/TicTacToe/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/OpenCog.dir/AtomSpace/Atoms.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/OpenCog.dir/AtomSpace/Atoms.cpp.o -c /Users/gregeales/CLionProjects/TicTacToe/AtomSpace/Atoms.cpp

CMakeFiles/OpenCog.dir/AtomSpace/Atoms.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/OpenCog.dir/AtomSpace/Atoms.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/gregeales/CLionProjects/TicTacToe/AtomSpace/Atoms.cpp > CMakeFiles/OpenCog.dir/AtomSpace/Atoms.cpp.i

CMakeFiles/OpenCog.dir/AtomSpace/Atoms.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/OpenCog.dir/AtomSpace/Atoms.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/gregeales/CLionProjects/TicTacToe/AtomSpace/Atoms.cpp -o CMakeFiles/OpenCog.dir/AtomSpace/Atoms.cpp.s

CMakeFiles/OpenCog.dir/AtomSpace/Atoms.cpp.o.requires:

.PHONY : CMakeFiles/OpenCog.dir/AtomSpace/Atoms.cpp.o.requires

CMakeFiles/OpenCog.dir/AtomSpace/Atoms.cpp.o.provides: CMakeFiles/OpenCog.dir/AtomSpace/Atoms.cpp.o.requires
	$(MAKE) -f CMakeFiles/OpenCog.dir/build.make CMakeFiles/OpenCog.dir/AtomSpace/Atoms.cpp.o.provides.build
.PHONY : CMakeFiles/OpenCog.dir/AtomSpace/Atoms.cpp.o.provides

CMakeFiles/OpenCog.dir/AtomSpace/Atoms.cpp.o.provides.build: CMakeFiles/OpenCog.dir/AtomSpace/Atoms.cpp.o


CMakeFiles/OpenCog.dir/NeuralNetwork.cpp.o: CMakeFiles/OpenCog.dir/flags.make
CMakeFiles/OpenCog.dir/NeuralNetwork.cpp.o: ../NeuralNetwork.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/gregeales/CLionProjects/TicTacToe/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/OpenCog.dir/NeuralNetwork.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/OpenCog.dir/NeuralNetwork.cpp.o -c /Users/gregeales/CLionProjects/TicTacToe/NeuralNetwork.cpp

CMakeFiles/OpenCog.dir/NeuralNetwork.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/OpenCog.dir/NeuralNetwork.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/gregeales/CLionProjects/TicTacToe/NeuralNetwork.cpp > CMakeFiles/OpenCog.dir/NeuralNetwork.cpp.i

CMakeFiles/OpenCog.dir/NeuralNetwork.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/OpenCog.dir/NeuralNetwork.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/gregeales/CLionProjects/TicTacToe/NeuralNetwork.cpp -o CMakeFiles/OpenCog.dir/NeuralNetwork.cpp.s

CMakeFiles/OpenCog.dir/NeuralNetwork.cpp.o.requires:

.PHONY : CMakeFiles/OpenCog.dir/NeuralNetwork.cpp.o.requires

CMakeFiles/OpenCog.dir/NeuralNetwork.cpp.o.provides: CMakeFiles/OpenCog.dir/NeuralNetwork.cpp.o.requires
	$(MAKE) -f CMakeFiles/OpenCog.dir/build.make CMakeFiles/OpenCog.dir/NeuralNetwork.cpp.o.provides.build
.PHONY : CMakeFiles/OpenCog.dir/NeuralNetwork.cpp.o.provides

CMakeFiles/OpenCog.dir/NeuralNetwork.cpp.o.provides.build: CMakeFiles/OpenCog.dir/NeuralNetwork.cpp.o


CMakeFiles/OpenCog.dir/TicTacToe.cpp.o: CMakeFiles/OpenCog.dir/flags.make
CMakeFiles/OpenCog.dir/TicTacToe.cpp.o: ../TicTacToe.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/gregeales/CLionProjects/TicTacToe/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object CMakeFiles/OpenCog.dir/TicTacToe.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/OpenCog.dir/TicTacToe.cpp.o -c /Users/gregeales/CLionProjects/TicTacToe/TicTacToe.cpp

CMakeFiles/OpenCog.dir/TicTacToe.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/OpenCog.dir/TicTacToe.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/gregeales/CLionProjects/TicTacToe/TicTacToe.cpp > CMakeFiles/OpenCog.dir/TicTacToe.cpp.i

CMakeFiles/OpenCog.dir/TicTacToe.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/OpenCog.dir/TicTacToe.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/gregeales/CLionProjects/TicTacToe/TicTacToe.cpp -o CMakeFiles/OpenCog.dir/TicTacToe.cpp.s

CMakeFiles/OpenCog.dir/TicTacToe.cpp.o.requires:

.PHONY : CMakeFiles/OpenCog.dir/TicTacToe.cpp.o.requires

CMakeFiles/OpenCog.dir/TicTacToe.cpp.o.provides: CMakeFiles/OpenCog.dir/TicTacToe.cpp.o.requires
	$(MAKE) -f CMakeFiles/OpenCog.dir/build.make CMakeFiles/OpenCog.dir/TicTacToe.cpp.o.provides.build
.PHONY : CMakeFiles/OpenCog.dir/TicTacToe.cpp.o.provides

CMakeFiles/OpenCog.dir/TicTacToe.cpp.o.provides.build: CMakeFiles/OpenCog.dir/TicTacToe.cpp.o


# Object files for target OpenCog
OpenCog_OBJECTS = \
"CMakeFiles/OpenCog.dir/main.cpp.o" \
"CMakeFiles/OpenCog.dir/AtomSpace/Atoms.cpp.o" \
"CMakeFiles/OpenCog.dir/NeuralNetwork.cpp.o" \
"CMakeFiles/OpenCog.dir/TicTacToe.cpp.o"

# External object files for target OpenCog
OpenCog_EXTERNAL_OBJECTS =

OpenCog: CMakeFiles/OpenCog.dir/main.cpp.o
OpenCog: CMakeFiles/OpenCog.dir/AtomSpace/Atoms.cpp.o
OpenCog: CMakeFiles/OpenCog.dir/NeuralNetwork.cpp.o
OpenCog: CMakeFiles/OpenCog.dir/TicTacToe.cpp.o
OpenCog: CMakeFiles/OpenCog.dir/build.make
OpenCog: CMakeFiles/OpenCog.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/gregeales/CLionProjects/TicTacToe/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Linking CXX executable OpenCog"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/OpenCog.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/OpenCog.dir/build: OpenCog

.PHONY : CMakeFiles/OpenCog.dir/build

CMakeFiles/OpenCog.dir/requires: CMakeFiles/OpenCog.dir/main.cpp.o.requires
CMakeFiles/OpenCog.dir/requires: CMakeFiles/OpenCog.dir/AtomSpace/Atoms.cpp.o.requires
CMakeFiles/OpenCog.dir/requires: CMakeFiles/OpenCog.dir/NeuralNetwork.cpp.o.requires
CMakeFiles/OpenCog.dir/requires: CMakeFiles/OpenCog.dir/TicTacToe.cpp.o.requires

.PHONY : CMakeFiles/OpenCog.dir/requires

CMakeFiles/OpenCog.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/OpenCog.dir/cmake_clean.cmake
.PHONY : CMakeFiles/OpenCog.dir/clean

CMakeFiles/OpenCog.dir/depend:
	cd /Users/gregeales/CLionProjects/TicTacToe/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/gregeales/CLionProjects/TicTacToe /Users/gregeales/CLionProjects/TicTacToe /Users/gregeales/CLionProjects/TicTacToe/cmake-build-debug /Users/gregeales/CLionProjects/TicTacToe/cmake-build-debug /Users/gregeales/CLionProjects/TicTacToe/cmake-build-debug/CMakeFiles/OpenCog.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/OpenCog.dir/depend

