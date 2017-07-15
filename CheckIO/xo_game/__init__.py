def checkio(game_result):
    c=['','','']
    for raw in game_result:
        if raw == "XXX":
            return "X"
        elif raw ==  "OOO":
            return "O"
        c[0]=c[0]+raw[0]
        c[1]=c[1]+raw[1]
        c[2]=c[2]+raw[2]
    for col in c:
        if col == "XXX":
            return "X"
        elif col == "OOO":
            return "O"
    diag1 = c[0][0] + c[1][1] + c[2][2]
    diag2 = c[2][0] + c[1][1] + c[0][2]
    if diag1 == "XXX" or diag2 == "XXX":
        return "X"
    elif diag1 == "OOO" or diag2 =="OOO":
        return "O"
    return "D"

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