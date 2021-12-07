#include <string>
#include <fstream>
#include <vector>
#include <iostream>
using namespace std;

// gamma = most common bit in list
// epsilon = least common
int gamma_epsilon(vector<int> sums, int n_input) {
    string gamma, epsilon; // ""
    int gamma_val, epsilon_val;
    for (size_t i=0; i<sums.size(); ++i) { // ++i?
        if (sums[i] < n_input / 2) {
            gamma += '0';
            epsilon += '1';
        } else {
            gamma += '1';
            epsilon += '0';
        }
    }
    gamma_val = stoi(gamma,0,2); 
    epsilon_val = stoi(epsilon,0,2); 
    cout << gamma << endl;
    cout << to_string(gamma_val) << endl; // convert from binary
    cout << epsilon << endl;
    cout << to_string(epsilon_val) << endl; // convert from binary
    cout << to_string(epsilon_val * gamma_val) << endl;
    return 0;
}

/* Store an array to sum each column of the binary numbers.
 * If the resulting sum is less than half the length of the input list,
 * then the most common bit is 0; otherwise, it is 1. */
int partA(ifstream& f) {
    cout << "Part A: " << endl;
    // grab the first to set n_bits
    string line;
    getline(f,line); 
    int n_bits = line.size();
    // now return to beginning of stream
    f.clear();
    f.seekg(0);

    int line_count = 0;
    vector<int> sums(n_bits,0); // init to 0
    while (f >> line) { // experimenting with >>
        line_count++;
        for (int i=0;i<n_bits;i++) {
            int bit_val = line[i] - '0'; // char to int
            sums[i] += bit_val;
        }
    }
    gamma_epsilon(sums,line_count);
    return 0;
}

int main() {
    ifstream f ("input.txt");
    if (f.is_open()) {
        partA(f);
    }
    return 0;
}
