from advent.year24.problem4.solution import word_count, xmas_count

def test_word_count_examples():
    examples = [
        (
            """..X...
.SAMX.
.A..A.
XMAS.S
.X....""",
            4
        ),
        (
            """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""",
            18
        ),
        (
            """....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX""",
            18
        )
    ]

    for input, expected in examples:
        assert word_count(input) == expected


def test_xmas_count_examples():
    examples = [
        (
            """M.S
.A.
M.S""",
            1
        ),
        (
            """.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........""",
            9
        )
    ]

    for input, expected in examples:
        assert xmas_count(input) == expected