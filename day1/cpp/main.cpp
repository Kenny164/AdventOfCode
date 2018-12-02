#include <iostream>
#include <fstream>
#include <set>
#include <vector>

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

int starTwo() {
    std::ifstream fileIn ("inputs/day1.txt");
    std::vector<int> extractedInts;
    if (fileIn.is_open()) {
        int current = 0;
        while(fileIn >> current) {
            extractedInts.push_back(current);
        }
        fileIn.close();
    }
    else {
        std::cout << "File cannot open";
        exit(-2);
    }
    std::set<int> historicTotal;
    int rollingTotal = 0;
    for (int i=0; i<10000; i++) {
        for (std::vector<int>::size_type j=0; j<extractedInts.size(); j++) {
            rollingTotal += extractedInts[j];
            auto search = historicTotal.find(rollingTotal);
            if (search != historicTotal.end()) {
                return rollingTotal;
            }
            historicTotal.insert(rollingTotal);
        }
    }
    return -1;
}

int main(int argc, char const *argv[]) {
    std::cout << starOne() << std::endl;
    std::cout << starTwo() << std::endl;
    return 0;
}
