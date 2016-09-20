FIRST_TEN  = ["one", "two", "three", "four", "five", "six", "seven",
              "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]

def checkio(number):

    num_as_text = ''

    hundreds = number//100
    tens     = (number - hundreds*100)//10
    units    = number - hundreds*100 - tens*10

    if hundreds:
        num_as_text += FIRST_TEN[hundreds-1] + " hundred "
    
    if tens > 1:
        num_as_text += OTHER_TENS[tens-2]
        if units:
            num_as_text += " " + FIRST_TEN[units-1]
    elif tens == 1:
        num_as_text += SECOND_TEN[units]
    elif units:
        num_as_text += FIRST_TEN[units-1]

    return num_as_text.rstrip()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert checkio(400) == 'four hundred', "even hundreds"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"