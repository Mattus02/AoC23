#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#define MAP_SIZE 140

bool is_symbol[MAP_SIZE][MAP_SIZE];
int answer = 0;

bool is_digit(char c)
{
    return c >= '0' && c <= '9';
}

int power_of_ten(int digit, int power)
{
    int m = 1;
    while (power--)
        m *= 10;
    return digit * m;
}

bool is_near_symbol(int row, int column)
{
    for (int curr_row = row - 1; curr_row <= row + 1; ++curr_row)
        for (int curr_column = column - 1; curr_column <= column + 1; ++curr_column)
            if (curr_row >= 0 && curr_column >= 0 && is_symbol[curr_row][curr_column])
                return true;
    return false;
}

void initialize_grid()
{
    for (int i = 0; i < MAP_SIZE; ++i)
        for (int j = 0; j < MAP_SIZE; ++j)
            is_symbol[i][j] = false;
}

void fill_grid()
{
    ifstream file {"sample_input.txt"};
    string line;
    int row = 0;
    while (getline(file, line))
    {
        int column = 0;
        for (char c : line)
        {
            if (c != '.' && !is_digit(c))
                is_symbol[row][column] = true;
            column += 1;
        }
        row += 1;
    }
}

void count_numbers()
{
    ifstream file {"sample_input.txt"};
    string line;
    int row = 0;
    while (getline(file, line))
    {
        int column = MAP_SIZE;
        while (column >= 0)
        {
            if (is_digit(line[column]))
            {
                bool near_symbol = false;
                int sum = 0;
                int power = 0;
                while (column >= 0 && is_digit(line[column]))
                {
                    near_symbol = near_symbol || is_near_symbol(row, column);
                    sum += power_of_ten(line[column] - '0', power);
                    power += 1;
                    column -= 1;
                }
                if (near_symbol)
                    answer += sum;
            }
            else
            {
                column -= 1;
            }
        }
        row += 1;
    }

}

int main()
{
    initialize_grid();
    fill_grid();
    count_numbers();
    cout << answer << endl;
}