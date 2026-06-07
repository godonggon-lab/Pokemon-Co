from __future__ import annotations

from collections import deque
from typing import List

from harness.cases import GeneratedCase, edge, stress

DIRS = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('5 5\n#####\n#..B#\n#.#.#\n#RO.#\n#####\n', '1\r\nR\r\n'),
        edge('5 5\n#####\n#B..#\n#.#.#\n#RO.#\n#####\n', '1\r\nR\r\n'),
        stress('7 7\n#######\n#...RB#\n#.#####\n#.....#\n#####.#\n#O....#\n#######\n', '5\r\nLDRDL\r\n'),
    ]


def check_output(stdin: str, expected: str, actual: str) -> bool:
    best = expected.strip().splitlines()[0].strip()
    lines = actual.strip().splitlines()
    if not lines:
        return False
    if best == "-1":
        return lines[0].strip() == "-1"
    try:
        moves = int(lines[0].strip())
    except ValueError:
        return False
    if moves != int(best) or len(lines) < 2:
        return False
    path = lines[1].strip()
    if len(path) != moves or any(ch not in DIRS for ch in path):
        return False
    board, red, blue, _hole = _parse_board(stdin)
    for ch in path:
        red, blue, red_hole, blue_hole = _tilt(board, red, blue, DIRS[ch])
        if blue_hole:
            return False
        if red_hole:
            return True
    return False


def _parse_board(stdin: str):
    lines = stdin.splitlines()
    n, _m = map(int, lines[0].split())
    board = [list(line) for line in lines[1:1 + n]]
    red = blue = hole = (-1, -1)
    for r in range(n):
        for c in range(len(board[r])):
            if board[r][c] == "R":
                red = (r, c)
                board[r][c] = "."
            elif board[r][c] == "B":
                blue = (r, c)
                board[r][c] = "."
            elif board[r][c] == "O":
                hole = (r, c)
    return board, red, blue, hole


def _roll(board, pos, direction):
    r, c = pos
    dr, dc = direction
    count = 0
    while board[r + dr][c + dc] != "#":
        r += dr
        c += dc
        count += 1
        if board[r][c] == "O":
            return (r, c), count, True
    return (r, c), count, False


def _tilt(board, red, blue, direction):
    next_red, red_count, red_hole = _roll(board, red, direction)
    next_blue, blue_count, blue_hole = _roll(board, blue, direction)
    if not red_hole and not blue_hole and next_red == next_blue:
        dr, dc = direction
        if red_count > blue_count:
            next_red = (next_red[0] - dr, next_red[1] - dc)
        else:
            next_blue = (next_blue[0] - dr, next_blue[1] - dc)
    return next_red, next_blue, red_hole, blue_hole
