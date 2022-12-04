from typing import TextIO, Tuple

#  X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

SHAPE_SCORE = {
    'X': 1,
    'Y': 2,
    'Z': 3
}


def parse_input(file: TextIO) -> Tuple[Tuple[str]]:
    return tuple(tuple(rounds.split(' ')) for rounds in file.read().strip().split("\n"))


def score_shape(shape: str) -> int:
    return SHAPE_SCORE[shape]

# TODO: Solve using new strategy (part 2)
# def score_outcome(round: Tuple) -> int:
#     match round:
#         case (('A', 'Y') | ('B', 'Z') | ('C', 'X')):
#             return 6
#         case (('A', 'Z') | ('B', 'X') | ('C', 'Y')):
#             return 0
#         case _:
#             return 3


def score_round(round: Tuple) -> int:
    return score_outcome(round) + score_shape(round[1])


if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        print(f"Part 2: {sum(tuple(score_round(r) for r in parse_input(f)))}")
