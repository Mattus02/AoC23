package main

import "core:fmt"
import "core:os"
import "core:strings"
import "core:strconv"
import "core:slice"
import "core:sort"

rune_map := map[rune]rune {
    'A' = 'e',
    'K' = 'd',
    'Q' = 'c',
    'T' = 'b',
    'J' = '1',
}

HandType :: enum {
    FiveKind,
    FourKind,
    FullHouse,
    ThreeKind,
    TwoPair,
    OnePair,
    HighCard,
}

Hand :: struct {
    runes: [dynamic]rune,
    type: HandType,
    value: int,
}

rune_count :: proc(r: rune, runes: ^[dynamic]rune) -> int
{
    count := 0
    for c in runes {
        if c == r || c == '1' {
            count += 1
        }
    }
    return count
}

cmp :: proc(h1: Hand, h2: Hand) -> bool
{

    if h1.type == h2.type {
        i := 0        
        for h1.runes[i] == h2.runes[i] {
            i += 1
        }
        return h1.runes[i] < h2.runes[i]
    }
    return h1.type > h2.type
}

clear_jokers :: proc(runes: ^[dynamic]rune)
{
    for c in runes {
        if c == '1' {
            c = '0'
        }
    }
}

find_type :: proc(runes: ^[dynamic]rune) -> HandType
{
    for c in runes {
        if rune_count(c, runes) == 5 {
            return HandType.FiveKind
        }
    }

    for c in runes {
        if rune_count(c, runes) == 4 {
            return HandType.FourKind
        }
    }
    
    has_three_kind := false
    used_rune: rune = ---
    for c in runes {
        if rune_count(c, runes) == 3 {
            has_three_kind = true
            used_rune = c
            clear_jokers(runes)
            break
        }
    }

    if has_three_kind {
        for c in runes {
            if c == '0' || c == used_rune {
                continue
            }
            if rune_count(c, runes) == 2 {
                return HandType.FullHouse
            }
        }
        return HandType.ThreeKind
    }

    pair_count := 0
    for c in runes {
        if rune_count(c, runes) == 2 {
            pair_count += 1
            clear_jokers(runes)
        }
    }
    
    if pair_count >= 3 {
        return HandType.TwoPair
    } else if pair_count >= 1 {
        return HandType.OnePair
    }
    
    return HandType.HighCard
}

main :: proc()
{
    data, ok := os.read_entire_file("sample_input.txt")
    defer delete(data)

    hands: [dynamic]Hand
    defer delete(hands)

    it := string(data)
    for line in strings.split_lines_iterator(&it)
    {
        splitted := strings.split(line, " ")
        h: Hand = ---
        h.runes = make([dynamic]rune, 0)
        for c, i in splitted[0] {
            if c in rune_map {
                append(&h.runes, rune_map[c])
            } else {
                append(&h.runes, c)
            }
        }
        h.type = find_type(&h.runes)
        h.value, ok = strconv.parse_int(splitted[1])
        append(&hands, h)
    }

    slice.sort_by(hands[:], cmp)

    for hand in hands {
        fmt.println("runes:", hand.runes, "| type:", hand.type, "| value:", hand.value)
    }
    
    answer := 0
    for h, i in hands {
        answer += h.value * (i+1)
    }
    fmt.println(answer)
}