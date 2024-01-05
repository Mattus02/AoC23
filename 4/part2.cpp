#include <bits/stdc++.h>

using namespace std;

#define TOTAL_CARDS 202
#define WINNING_NUMBERS 10
#define OTHER_NUMBERS 25

int main()
{
    vector<int> card_count(TOTAL_CARDS, 1);
    ifstream file {"sample_input.txt"};
    string line;
    int sum = 0;
    int current_card = 0;
    while (getline(file, line))
    {
        istringstream iss{line};
        string token;
        iss >> token >> token;
        int winning_numbers[WINNING_NUMBERS];
        for (int i = 0; i < WINNING_NUMBERS; ++i)
        {
            iss >> winning_numbers[i];
        }
        iss >> token;
        int match_count = 0;
        for (int i = 0; i < OTHER_NUMBERS; ++i)
        {
            int current;
            iss >> current;
            if (find(begin(winning_numbers), end(winning_numbers), current) != end(winning_numbers))
            {
                match_count += 1;
            }
        }
        if (match_count != 0)
        {
            for (int i = 0; i < card_count[current_card]; ++i)
            {
                for (int j = current_card + 1; j < TOTAL_CARDS && j <= current_card + match_count; ++j)
                {
                    card_count[j] += 1;
                }
            }
        }
        current_card += 1;
    }
    cout << accumulate(card_count.begin(), card_count.end(), 0) << endl;
}