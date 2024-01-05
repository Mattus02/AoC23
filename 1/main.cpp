#include <bits/stdc++.h>

using namespace std;

vector<string> words = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

string replace_words(string& line)
{
    string result{};
    for (size_t i = 0; i < line.length(); ++i) 
    {
        bool found_word = false;
        for (int j = 0; j < 9; ++j)
        {
            if (line.find(words[j], i) == i)
            {
                result += to_string(j+1);
                found_word = true;
                break;
            }
        }
        if (!found_word)
        {
            result += line[i];
        }
    }
    return result;
}

int main()
{
    ifstream file {"sample_input.txt"};
    unsigned long long sum = 0;
    string line;

    while (getline(file, line))
    {
        string replaced = replace_words(line);
        auto it1 = find_if(replaced.begin(), replaced.end(), [](char c) -> bool { return c >= '0' && c <= '9'; });
        auto it2 = find_if(replaced.rbegin(), replaced.rend(), [](char c) -> bool { return c >= '0' && c <= '9'; });
        sum += (*it1 - '0') * 10 + (*it2 - '0');
    }

    cout << sum << endl;
}