#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

int main()
{
    ifstream file {"sample_input.txt"};
    int sum = 0;
    string line;
    while (getline(file, line))
    {
        istringstream iss {line};
        string token;
        iss >> token >> token;
        token.pop_back();
        int id = stoi(token);
        bool possible = true;
        while (iss >> token)
        {
            int amount = stoi(token);
            string color;
            iss >> color;
            if ((color.front() == 'r' && amount > 12) ||
                (color.front() == 'g' && amount > 13) ||
                (color.front() == 'b' && amount > 14))
            {
                possible = false;
                break;
            }
        }
        if (possible) {
            sum += id;
        }
    }
    cout << sum << endl;
}