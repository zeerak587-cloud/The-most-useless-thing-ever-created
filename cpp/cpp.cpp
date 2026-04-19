#include <iostream>
#include <algorithm>
using namespace std;

int main(int argc, char* argv[]) {
    string input = argv[1];
    reverse(input.begin(), input.end());
    cout << "[C++] reversed: " << input;
    return 0;
}