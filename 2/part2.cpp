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
        int r_min = 0, g_min = 0, b_min = 0; 
        while (iss >> token)
        {
            int amount = stoi(token);
            string color;
            iss >> color;
            if (color.front() == 'r') 
                r_min = max(r_min, amount);
            else if (color.front() == 'g')
                g_min = max(g_min, amount);
            else if (color.front() == 'b')
                b_min = max(b_min, amount);
        }
        sum += (r_min * g_min * b_min);
    }
    cout << sum << endl;
}