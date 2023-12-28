from typing import List


def is_valid_sudoku(board: List[List[str]]) -> bool:
    row_set = set()
    column_set = []
    for i in range(9):
        column_set.append(set())
    print(column_set)
    block_set = [set(), set(), set()]
    for index_row in range(9):
        row_set.clear()
        if (index_row == 3 or index_row == 6):
            for elem in block_set:
                elem.clear()
        for index_column in range(9):
            if board[index_row][index_column] == ".":
                continue
            if board[index_row][index_column] in row_set:
                return False
            if board[index_row][index_column] in block_set[int(index_column / 3)]:
                return False
            if board[index_row][index_column] in column_set[index_column]:
                return False
            row_set.add(board[index_row][index_column])
            column_set[index_column].add(board[index_row][index_column])
            if (index_column >= 0 and index_column <= 2):
                block_set[0].add(board[index_row][index_column])
            if (index_column >= 3 and index_column <= 5):
                block_set[1].add(board[index_row][index_column])
            if (index_column >= 6 and index_column <= 8):
                block_set[2].add(board[index_row][index_column])
    return True


print(is_valid_sudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                       ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                       [".", "9", "8", ".", ".", ".", ".", "6", "."],
                       ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                       ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                       ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                       [".", "6", ".", ".", ".", ".", "2", "8", "."],
                       [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                       [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
                      ))
