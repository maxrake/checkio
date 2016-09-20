## My first attempt:
#def checkio(str_number, radix):
#    
#    rads = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#    length = len(str_number)
#    base10 = 0
#
#    try:
#        for pos in range(length):
#            base10 += (rads[:radix].index(str_number[pos])) * (radix**(length-pos-1))
#        return base10
#    except:     # .index() throws exception when out of range (can't be converted)
#        return -1

## My second attempt:
#def checkio(num, rdx):
#    rads = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#    try:
#        return sum([rads[:rdx].index(num[i])*rdx**(len(num)-i-1) for i in range(len(num))])
#    except:     # .index() throws exception when out of range (can't be converted)
#        return -1

## My third attempt:
def checkio(number, radix):
    """Convert a stringified number of given radix into an integer."""
    try:
        return int(number, base=radix)
    except ValueError:
        return -1

## My favorite solution from another player:
#checkio=lambda n,r:-(r<=int(max(n),36))or int(n,r)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"
    assert checkio("909", 9) == -1, "Extra Test1"