#total = 0
#idx = 0
#reached_exception = False
#def checkio(data):
#    global total
#    global idx
#    global reached_exception
#    try:
#        total += data[idx]
#        idx += 1
#        checkio(data)
#        if reached_exception:
#            return total
#    except IndexError:
#        reached_exception = True

def checkio(data):
    total = 0
    idx = 0
    reached_exception = False

    def _accumulate(data):
        nonlocal total
        nonlocal idx
        nonlocal reached_exception
        try:
            total += data[idx]
            idx += 1
            _accumulate(data)
            if reached_exception:
                return total
        except IndexError:
            reached_exception = True

    return _accumulate(data)


if __name__ == '__main__':
    assert checkio([1,2,3]) == 6, "test 1"
    assert checkio([2,2,2,2,2,2]) == 12, "test 2"
    assert checkio([42]) == 42, "test 3"
    print(' [+] All asserts passed')