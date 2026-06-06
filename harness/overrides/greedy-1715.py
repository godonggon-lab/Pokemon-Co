from __future__ import annotations

from typing import List

from harness.cases import GeneratedCase, edge, stress


def gen_inputs(_seed: int) -> List[GeneratedCase]:
    return [
        edge('1\n10\n', '0\r\n'),
        edge('2\n10\n20\n', '30\r\n'),
        edge('3\n10\n20\n40\n', '100\r\n'),
        edge('5\n1\n1\n1\n1\n1\n', '12\r\n'),
        edge('6\n100\n1\n50\n2\n3\n4\n', '239\r\n'),
        stress('30\n1\n18\n35\n52\n69\n86\n3\n20\n37\n54\n71\n88\n5\n22\n39\n56\n73\n90\n7\n24\n41\n58\n75\n92\n9\n26\n43\n60\n77\n94\n', '6568\r\n'),
    ]
