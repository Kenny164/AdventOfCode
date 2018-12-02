#include <iostream>
#include <fstream>
#include <set>
#include <vector>

void extractInput(std::vector<int>& extractedInts, const char* filePath) {
    std::ifstream fileIn (filePath);
    if (!fileIn.is_open()) {
        std::cout << "File cannot open";
        exit(-2);
    }
    int current = 0;
    while(fileIn >> current) {
        extractedInts.push_back(current);
    }
    fileIn.close();
}

int starOne(const std::vector<int>& extractedInts) {
    int rollingTotal = 0;
    for (std::vector<int>::size_type j=0; j<extractedInts.size(); j++) {
        rollingTotal += extractedInts[j];
    }
    return rollingTotal;
}

int starTwo(const std::vector<int>& extractedInts) {
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
    std::vector<int> extractedInts;
    extractInput(extractedInts, "inputs/day1.txt");
    std::cout << starOne(extractedInts) << std::endl;
    std::cout << starTwo(extractedInts) << std::endl;
    return 0;
}
