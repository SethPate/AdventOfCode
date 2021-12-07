#import <fstream>
#import <iostream>
#import <string>
using namespace std;

struct position {
    int depth = 0, horizontal = 0, aim = 0;
};

typedef struct position Pos;

string delimiter = " "; // for parsing

int update_a(Pos *p, string command, string number) {
    if (command.compare("forward") == 0) {
        p->horizontal += stoi(number);
    } else if (command.compare("down") == 0) {
        p->depth += stoi(number);
    } else if (command.compare("up") == 0) {
        p->depth -= stoi(number);
    }
    return 0;
}

int update_b(Pos *p, string command, string number) {
    if (command.compare("forward") == 0) {
        p->horizontal += stoi(number);
        p->depth += p->aim * stoi(number);
    } else if (command.compare("down") == 0) {
        p->aim += stoi(number);
    } else if (command.compare("up") == 0) {
        p->aim -= stoi(number);
    }
    return 0;
}

int partAB(ifstream& f, Pos *a, Pos *b) { 
    string line, command_token, number_token;
    int split;
    if (f.is_open()) {
        while (getline(f,line)) {
            split = line.find(delimiter);
            command_token = line.substr(0,split);
            number_token = line.substr(split,line.length());
            update_a(a, command_token, number_token);
            update_b(b, command_token, number_token);
        }
    } 
    return 0;
}


int main() {
    ifstream f ("input.txt");
    Pos a, b;
    partAB(f,&a,&b); // update with answer
    f.close();

    cout << "Part A: " << endl;
    cout << "Depth: " << to_string(a.depth) << endl;
    cout << "Horizontal: " << to_string(a.horizontal) << endl;
    cout << "Depth * Horizontal: " << 
            to_string(a.depth * a.horizontal) << endl;

    cout << "Part B: " << endl;
    cout << "Depth: " << to_string(b.depth) << endl;
    cout << "Horizontal: " << to_string(b.horizontal) << endl;
    cout << "Aim: " << to_string(b.aim) << endl;
    cout << "Depth * Horizontal: " << 
            to_string(b.depth * b.horizontal) << endl;

    return 0;
}
