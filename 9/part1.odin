package main

import "core:os"
import "core:strings"
import "core:strconv"
import "core:fmt"

rec :: proc(values: []int) -> (last_value: int)
{
    if all_values_are_zero(values) {
        return 0
    }
    length := len(values)
    new_values := make([]int, length - 1)
    for i in 0..<length-1 {
        new_values[i] = values[i+1] - values[i]
    }
    return values[length - 1] + rec(new_values)
}

all_values_are_zero :: proc(values: []int) -> bool
{
    for v in values {
        if v != 0 {
            return false
        }
    }
    return true
}

main :: proc()
{
    data, ok := os.read_entire_file("sample_input.txt")
    defer delete(data)

    history: [dynamic]int
    defer delete(history)
    values: [dynamic]int
    defer delete(values)

    it := string(data)
    for line in strings.split_lines_iterator(&it)
    {
        clear(&history)
        splitted := strings.split(line, " ")
        for s in splitted {
            parsed_int, ok := strconv.parse_int(s)
            append(&history, parsed_int)
        }
        append(&values, rec(history[:]))
    }

    sum := 0
    for v in values {
        sum += v
    }
    fmt.println(sum)
}