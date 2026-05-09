from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge("1 3\nBronze 10\n1\n5\n10\n", "Bronze\nBronze\nBronze\n"),
        edge("2 4\nBronze 10\nSilver 20\n1\n10\n11\n20\n", "Bronze\nBronze\nSilver\nSilver\n"),
        edge("3 4\nA 100\nB 100\nC 200\n99\n100\n101\n200\n", "A\nA\nC\nC\n"),
        edge("3 3\nLow 5\nMid 10\nHigh 15\n5\n6\n15\n", "Low\nMid\nHigh\n"),
        edge("4 5\nIron 10\nBronze 20\nSilver 30\nGold 40\n1\n21\n30\n31\n40\n", "Iron\nSilver\nSilver\nGold\nGold\n"),
        stress("5 6\nA 10\nB 30\nC 50\nD 70\nE 90\n10\n11\n49\n50\n89\n90\n", "A\nB\nC\nC\nE\nE\n"),
    ]
