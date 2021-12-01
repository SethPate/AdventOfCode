#include <iostream>
#include <fstream>
#include <string>

int main () {

    std::ifstream f ("input.txt");
    std::string line;
    int increases = 0;
    int depth = 0;
    if (f.is_open()) {
        std::getline(f,line);
        int previous_depth = std::stoi(line); // first depth
        while (std::getline (f, line)) {
            depth = std::stoi(line);
            if (previous_depth < depth) {
                increases++;
            }
            previous_depth = depth;
        }
        f.close();
    }
    std::cout << std::to_string(increases) << std::endl;

    return 0;
}
