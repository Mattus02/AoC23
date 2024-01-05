package main

import "core:fmt"
import "core:os"
import "core:strings"
import "core:container/queue"


search_info :: struct {
    idx: int,
    dist: int
}

find_start :: proc(m: ^[dynamic]rune) -> int
{
    for i in 0..<len(m) {
        if m[i] == 'S' {
            return i
        }
    }
    return -1
}

idx_to_xy :: proc(idx: int, side_length: int) -> (int, int)
{
    x := idx % side_length
    y := idx / side_length
    return x, y
}

xy_to_idx :: proc(x: int, y: int, side_length: int) -> int
{
    return y * side_length + x
}

search :: proc(m: ^[dynamic]rune, longest_dist: ^int, side_length: int)
{
    q: queue.Queue(search_info)
    visited := make([]bool, len(m))
    
    start := find_start(m)
    visited[start] = true;

    // Hard-coded to work with input.txt
    queue.push_back(&q, search_info{start - side_length, 1})
    queue.push_back(&q, search_info{start + 1, 1})

    for queue.len(q) > 0
    {
        curr := queue.front(&q)
        queue.pop_front(&q)

        longest_dist^ = max(longest_dist^, curr.dist)

        idx := curr.idx
        next_dist := curr.dist + 1
        x, y := idx_to_xy(idx, side_length)

        switch m[idx] {
            case '|':
                if y > 0 && !visited[idx - side_length] {
                    queue.push_back(&q, search_info{idx - side_length, next_dist})
                }
                if y < side_length - 1 && !visited[idx + side_length] {
                    queue.push_back(&q, search_info{idx + side_length, next_dist})
                }
            case '-':
                if x > 0 && !visited[idx - 1] {
                    queue.push_back(&q, search_info{idx - 1, next_dist})
                } 
                if x < side_length - 1 && !visited[idx + 1] {
                    queue.push_back(&q, search_info{idx + 1, next_dist})
                }
            case 'L':
                if x < side_length - 1 && !visited[idx + 1] {
                    queue.push_back(&q, search_info{idx + 1, next_dist})
                }
                if y > 0 && !visited[idx - side_length] {
                    queue.push_back(&q, search_info{idx - side_length, next_dist})
                }
            case 'J':
                if x > 0 && !visited[idx - 1] {
                    queue.push_back(&q, search_info{idx - 1, next_dist})
                } 
                if y > 0 && !visited[idx - side_length] {
                    queue.push_back(&q, search_info{idx - side_length, next_dist})
                }
            case '7':
                if x > 0 && !visited[idx - 1] {
                    queue.push_back(&q, search_info{idx - 1, next_dist})
                } 
                if y < side_length - 1 && !visited[idx + side_length] {
                    queue.push_back(&q, search_info{idx + side_length, next_dist})
                }
            case 'F':
                if x < side_length - 1 && !visited[idx + 1] {
                    queue.push_back(&q, search_info{idx + 1, next_dist})
                }
                if y < side_length - 1 && !visited[idx + side_length] {
                    queue.push_back(&q, search_info{idx + side_length, next_dist})
                }
        }

        visited[idx] = true
    }
}

main :: proc()
{
    data, ok := os.read_entire_file("sample_input.txt")
    defer delete(data)

    m: [dynamic]rune
    it := string(data)
    side_length: int
    for line in strings.split_lines_iterator(&it) {
        side_length = len(line)
        for c in line {
            append(&m, c)
        }
    }
    
    longest_dist := 0
    search(&m, &longest_dist, side_length)
    fmt.println(longest_dist)
}