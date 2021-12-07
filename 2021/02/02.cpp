#import <fstream>
#import <iostream>
#import <string>
using namespace std;

struct position {
    int depth = 0, horizontal = 0;
};

typedef struct position Pos;

string delimiter = " "; // for parsing

Pos update(Pos p, string command, string number) {
    if (command.compare("forward") == 0) {
        p.horizontal += stoi(number);
    } else if (command.compare("down") == 0) {
        p.depth += stoi(number);
    } else if (command.compare("up") == 0) {
        p.depth -= stoi(number);
    }
    return p;
}

Pos partA() { 
    Pos p; // return value
    ifstream f ("input.txt");
    string line, command_token, number_token;
    int split;
    if (f.is_open()) {
        while (getline(f,line)) {
            split = line.find(delimiter);
            command_token = line.substr(0,split);
            number_token = line.substr(split,line.length());
            p = update(p, command_token, number_token);
        }
    } 
    return p;
}


int main() {
    Pos part_a = partA();
    cout << "Part A: " << endl;
    cout << "Depth: " << to_string(part_a.depth) << endl;
    cout << "Horizontal: " << to_string(part_a.horizontal) << endl;
    cout << "Depth * Horizontal: " << 
            to_string(part_a.depth * part_a.horizontal) << endl;
    return 0;
}
