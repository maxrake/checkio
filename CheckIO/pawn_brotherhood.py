def safe_pawns(pawns):
    # make a set of (row,col) coordinates out of the rank/file strings
    pawn_idxs = {(int(p[1]) - 1, ord(p[0]) - 97) for p in pawns}
    
    # initialize the count
    count = 0

    # loop through the set of pawns, incrementing the count for every safe pawn
    for p in pawn_idxs:
        if ((p[0]-1, p[1]-1) in pawn_idxs) or ((p[0]-1, p[1]+1) in pawn_idxs):
            count += 1

    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("[+] All asserts passed!")