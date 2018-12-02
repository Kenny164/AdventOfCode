#include <iostream>
#include <fstream>
#include <string>

int starOne() {
    std::ifstream fileIn ("inputs/day1.txt");
    if (fileIn.is_open()) {
        long rollingTotal = 0;
        int current = 0;
        while(fileIn >> current) {
            rollingTotal += current;
        }
        return rollingTotal;
    }
    else {
        std::cout << "File cannot open";
        exit(-2);
    }
}

int main(int argc, char const *argv[]) {
    std::cout << starOne();
    return 0;
}
