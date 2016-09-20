## dictionary of roman numeral possibilities...the building blocks
#ROMANS = {1000 : 'M', 
#          900  : 'CM',
#          500  : 'D',
#          400  : 'CD',
#          100  : 'C', 
#          90   : 'XC',
#          50   : 'L', 
#          40   : 'XL',
#          10   : 'X', 
#          9    : 'IX',
#          5    : 'V', 
#          4    : 'IV',
#          1    : 'I'}

#def checkio(data):
#    # start with an empty list of numerals
#    answer = []

#    # loop through the input, appending the next numeral to the answer list
#    while (data > 0):
#        # go from the high numbers down
#        for key in sorted(ROMANS, reverse=True):
#            # until you find the biggest key less than or equal to the input
#            if data >= key:
#                # add that key value (a numeral) to the list
#                answer.append(ROMANS[key])
#                # and subtract it from the input
#                data -= key
#                # before moving on to find the next numeral
#                break

#    # return the list, joined as a single string
#    return ''.join(answer)


def checkio(data):
    ROMANS = ((1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),
                (50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I'))
    answer = []
    while (data > 0):
        for number,numeral in ROMANS:
            if data >= number:
                answer.append(numeral)
                data -= number
                break
    return ''.join(answer)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print("All tests passed")