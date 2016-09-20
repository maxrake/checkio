def checkio(number):
    minute = fed_pigeons = pigeons = 0
    
    while True:
        minute += 1
        old_pigeons = pigeons
        pigeons += minute
        if number >= pigeons:
            fed_pigeons += minute
            number -= pigeons
        else:
            number -= old_pigeons
            if number > 0:
                fed_pigeons += number
            return fed_pigeons


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"