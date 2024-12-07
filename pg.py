from copy import deepcopy

import pygame


CELL_SIZE = 30

SPACE_COLOR = (0, 0, 0)
BORDER_COLOR = (128, 128, 128)
FILLED_COLOR = (128, 0, 0)
COLORS = (SPACE_COLOR, BORDER_COLOR, FILLED_COLOR)

SPACE = 0
BORDER = 1
FILLED = 2


def fill(states, bitmap):
    offsets = ((1, 0), (0, 1), (-1, 0), (0, -1))
    if not states:
        return

    while states[-1][1] == len(offsets):
        states.pop()

    while bitmap[states[-1][0][1]][states[-1][0][0]] == BORDER:
        states.pop()

    bitmap[states[-1][0][1]][states[-1][0][0]] = FILLED  # fill pos with current x & y
    print(*states[-1][0])

    while True:
        try:
            while states[-1][1] == len(offsets):
                states.pop()
        except IndexError:
            return
        states.append([
            (
                states[-1][0][0] + offsets[states[-1][1]][0],  # x + offset_x
                states[-1][0][1] + offsets[states[-1][1]][1],  # y + offset_y
            ), 0  # offset count
        ])
        states[-2][1] += 1  # next offset on next call
        if 0 <= states[-1][0][0] < len(bitmap[0]) and 0 <= states[-1][0][1] < len(bitmap) and bitmap[states[-1][0][1]][states[-1][0][0]] == SPACE:
            break
        else:
            states.pop()

def main() -> None:
    pygame.init()
    bitmap = [
        ".....###.....",
        "...##...##...",
        "..#.......#..",
        ".#.........#.",
        ".#.........#.",
        "#...........#",
        "#...........#",
        "#...........#",
        ".#.........#.",
        ".#.........#.",
        "..#.......#..",
        "...##...##...",
        ".....###....."
    ]
    bitmap = [[int(ch == '#') for ch in line] for line in bitmap]
    bitmap_save = deepcopy(bitmap)

    width = len(bitmap[0])
    height = len(bitmap)

    screen = pygame.display.set_mode((width * CELL_SIZE, height * CELL_SIZE))
    pygame.display.set_caption("Task 8")

    clock = pygame.time.Clock()

    states = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = [x // CELL_SIZE for x in pygame.mouse.get_pos()]
                print(x, y)
                if bitmap[y][x] != BORDER:
                    bitmap = deepcopy(bitmap_save)
                    states = [[(x, y), 0]]
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    return

        fill(states, bitmap)

        for y, line in enumerate(bitmap):
            for x, bit in enumerate(line):
                pygame.draw.rect(
                    screen,
                    COLORS[bit],
                    (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                )

        pygame.display.flip()

        clock.tick(30)


if __name__ == "__main__":
    main()
