module part2;

import std.stdio;
import std.array;

struct node {
    int left;
    int right;
}

int
charsToValue(char[3] chars)
{
    int result = 0;
    result += (chars[2] - 'A');
    result += (chars[1] - 'A') * 26;
    result += (chars[0] - 'A') * 26 * 26;
    return result;
}

void
registerNode(ref node[26 * 26 * 26] nodes, char[3] curr, char[3] l, char[3] r)
{
    nodes[charsToValue(curr)].left = charsToValue(l);
    nodes[charsToValue(curr)].right = charsToValue(r);
}

bool
endsWith(char c, int i)
{
    return i % 26 == c - 'A';
}

void main()
{
    node[26 * 26 * 26] nodes;
    foreach (ref n; nodes) {
        n.left = -1;
        n.right = -1;
    }

    auto lines = File("sample_input.txt", "r").byLine();
    string commands = lines.front.dup;
    lines.popFront();
    lines.popFront();
    int[] ghosts;
    foreach (line; lines) {
        registerNode(nodes, line[0..3], line[7..10], line[12..15]);
        if (endsWith('A', charsToValue(line[0..3]))) {
            ghosts ~= charsToValue(line[0..3]);
        }
    }

    ulong[] loopTimes;
    foreach (g; ghosts)
    {
        int count = 0;
        int commandIndex = 0;
        while (!endsWith('Z', g)) {
            if (commands[commandIndex++] == 'L') {
                g = nodes[g].left;
            } else {
                g = nodes[g].right;
            }
            count += 1;
            commandIndex %= commands.length;
        }
        loopTimes ~= count;
    }

    writeln(loopTimes);
    import std.numeric : lcm;
    import std.algorithm.iteration;
    ulong result = fold!((a, b) => lcm(a, b))(loopTimes);
    writeln(result);
}