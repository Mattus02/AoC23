#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream file {"sample_input.txt"};
    string line;
    int sum = 0;
    while (getline(file, line))
    {
        istringstream iss{line};
        string token;
        iss >> token >> token;
        int winning_numbers[10];
        for (int i = 0; i < 10; ++i)
        {
            iss >> winning_numbers[i];
        }
        iss >> token;
        int count = 0;
        for (int i = 0; i < 25; ++i)
        {
            int current;
            iss >> current;
            if (find(begin(winning_numbers), end(winning_numbers), current) != end(winning_numbers))
            {
                count += 1;
            }
        }
        if (count != 0)
        {
            int points = 1 << (count - 1);
            sum += points;
        }
    }
    cout << sum << endl;
}