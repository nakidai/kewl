from copy import deepcopy


def print_bitmap(bitmap):
    for line in bitmap:
        print(''.join([['  ', '()', "##"][bit] for bit in line]))


def fill(x, y, bitmap):
    if bitmap[y][x]:
        return x, y

    bitmap[y][x] = 2

    # print_bitmap(bitmap)
    # print()
    # print(x, y)

    last_x, last_y = x, y

    for offset_x, offset_y in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        if not (0 <= x + offset_x < len(bitmap[0]) and 0 <= y + offset_y < len(bitmap)) or bitmap[y + offset_y][x + offset_x] != 0:
            continue
        last_x, last_y = fill(x + offset_x, y + offset_y, bitmap)

    return last_x, last_y


def main() -> None:
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

    for x in range(len(bitmap[0])):
        for y in range(len(bitmap)):
            if fill(x, y, bitmap) == (5, 11):
                print(x, y)
            bitmap = deepcopy(bitmap_save)
    # print(fill(5, 10, bitmap))


if __name__ == "__main__":
    main()
