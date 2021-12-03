#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int count_increases (int depths[], int length) {
    int increases = 0;
    int previous_depth = 0;
    int current_depth = 0;
    int bookmark = 0;

    for (int i=0 ; i<3 ; i++) {
        previous_depth += depths[i];
    }
    bookmark++;

    while (bookmark < (length - 2)) {
        current_depth = 0;
        current_depth += depths[bookmark];
        current_depth += depths[bookmark+1];
        current_depth += depths[bookmark+2];
        if (previous_depth < current_depth) {
            increases++;
        }
        previous_depth = current_depth;
        bookmark++;
    }

    return increases;
}

int main() {
    ifstream f ("input.txt");
    string line;
    int depths[10000];
    int counter = 0;
    int depth = 0;
    while (getline(f,line)) {
        depth = stoi(line);
        depths[counter] = depth;
        counter++;
    }
    int increases = count_increases(depths,counter);
    cout << to_string(increases) << endl;
    return 0;
}

