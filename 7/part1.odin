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
    'J' = 'b',
    'T' = 'a',
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
    value: int,
    type: HandType,
}

rune_count :: proc(r: rune, runes: ^[dynamic]rune) -> int
{
    count := 0
    for c in runes {
        if c == r {
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
        h.type = HandType.HighCard
        for c, i in splitted[0] {
            if i >= 5 {
                break
            }
            if c in rune_map {
                append(&h.runes, rune_map[c])
            } else {
                append(&h.runes, c)
            }
        }
        has_three_kind := false
        pair_count := 0
        for c in h.runes {
            count := rune_count(c, &h.runes)
            switch count {
                case 5:
                    h.type = HandType.FiveKind
                case 4:
                    h.type = HandType.FourKind
                case 3:
                    has_three_kind = true
                case 2:
                    pair_count += 1
            }
        }
        if has_three_kind && pair_count == 2 {
            h.type = HandType.FullHouse
        } else if has_three_kind {
            h.type = HandType.ThreeKind
        } else if pair_count == 4 {
            h.type = HandType.TwoPair
        } else if pair_count == 2 {
            h.type = HandType.OnePair
        }
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