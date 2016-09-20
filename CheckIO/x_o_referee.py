def checkio(game_result):
    # check for a row winner
    for row in game_result:
        if row.count('X') is 3:
            return 'X'
        if row.count('O') is 3:
            return 'O'

    # check for a column winner
    for col in zip(*game_result):   # transposes the matrix
        if col.count('X') is 3:
            return 'X'
        if col.count('O') is 3:
            return 'O'

    # check for a diagonal winner
    diag1 = [game_result[r][c] for r in range(3) for c in range(3) if r==c]
    diag2 = [game_result[~r][c] for r in range(3) for c in range(3) if r==c]
    if (diag1.count('X') is 3) or (diag2.count('X') is 3):
        return 'X'
    if (diag1.count('O') is 3) or (diag2.count('O') is 3):
        return 'O'

    # if we got this far and haven't returned yet, it must be a draw
    return 'D'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
