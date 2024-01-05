#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>

using namespace std;

#define MAP_SIZE 140

int gear_product[MAP_SIZE][MAP_SIZE];
int number_id[MAP_SIZE][MAP_SIZE];
int answer = 0;
vector<int> all_numbers;

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

void find_numbers(int row, int column)
{
    set<int> neighbours;
    for (int curr_row = row - 1; curr_row <= row + 1; ++curr_row) {
        for (int curr_column = column - 1; curr_column <= column + 1; ++curr_column) {
            if (curr_row >= 0 && curr_column >= 0 && number_id[curr_row][curr_column] != -1) {
                neighbours.insert(number_id[curr_row][curr_column]);
            }
        }
    }
    if (neighbours.size() == 2)
        gear_product[row][column] = all_numbers[*neighbours.begin()] * all_numbers[*neighbours.rbegin()];
}

void initialize_grids()
{
    for (int i = 0; i < MAP_SIZE; ++i) {
        for (int j = 0; j < MAP_SIZE; ++j) {
            gear_product[i][j] = 0;
            number_id[i][j] = -1;
        }
    }
}

void register_numbers()
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
                int id = all_numbers.size();
                int sum = 0;
                int power = 0;
                while (column >= 0 && is_digit(line[column]))
                {
                    number_id[row][column] = id;
                    sum += power_of_ten(line[column] - '0', power);
                    power += 1;
                    column -= 1;
                }
                all_numbers.push_back(sum);
            }
            else
            {
                column -= 1;
            }
        }
        row += 1;
    }
}

void find_gears()
{
    ifstream file {"sample_input.txt"};
    string line;
    int row = 0;
    while (getline(file, line))
    {
        int column = 0;
        for (char c : line)
        {
            if (c == '*')
                find_numbers(row, column);
            column += 1;
        }
        row += 1;
    }
}

void sum_the_products()
{
    for (int i = 0; i < MAP_SIZE; ++i) {
        for (int j = 0; j < MAP_SIZE; ++j) {
            answer += gear_product[i][j];
        }
    }
}

int main()
{
    initialize_grids();
    register_numbers();
    find_gears();
    sum_the_products();
    cout << answer << endl;
}