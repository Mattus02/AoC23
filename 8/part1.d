module part1;

import std.stdio;

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
    foreach (line; lines) {
        registerNode(nodes, line[0..3], line[7..10], line[12..15]);
    }

    int curr = 0;
    int commandIndex = 0;
    int count = 0;
    while (curr != 17575)
    {
        char move = commands[commandIndex++];
        if (move == 'L') {
            curr = nodes[curr].left;
        } else {
            curr = nodes[curr].right;
        }
        commandIndex %= commands.length;
        count += 1;
    }

    writeln(count);
}