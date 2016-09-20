import re

def make_us_style(mo):
    """Convert Euro style re match object, mo, to a US style string."""
    if mo.group(2): # matches for Euro currency >= $1,000.00
        return mo.group(1).translate(str.maketrans(".,", ",."))
    else:           # matches for Euro currency < $1,000.00
        return mo.group(1).replace(',', '.')

def checkio(text):
    """Convert Euro style currency in dollars to US/UK style."""
    euro = re.compile(r"""
        ((              # first Euro style, >= $1,000.00:
        (\$\d{1,3})     # starts with a dollar sign and 1-3 digits
        ((\.\d{3})+)    # one or more groups of 3 digits preceded by a '.'
        (,\d{1,2})?     # optional fractional part of the currency
        )|(             # second Euro style, < $1,000.00:
        \$\d{1,3}       # starts with a dollar sign and 1-3 digits
        (,\d{1,2})?     # followed by an optional fractional part of currency
        $               # and terminates with it being the end of the string
        )|(             # third Euro style, like the second but mid-string:
        \$\d{1,3}       # starts with a dollar sign and 1-3 digits
        (,\d{1,2})?     # followed by an optional fractional part of currency
        [^,\d]))        # and terminates with non-comma or non-digit character
        """, re.VERBOSE)

    return euro.sub(make_us_style, text)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("$1.234.567,89") == "$1,234,567.89" , "1st Example"
    assert checkio("$0,89") == "$0.89" , "2nd Example"
    assert checkio("Euro Style = $12.345,67, US Style = $12,345.67") == \
                   "Euro Style = $12,345.67, US Style = $12,345.67" , "European and US"
    assert checkio("Us Style = $12,345.67, Euro Style = $12.345,67") == \
                   "Us Style = $12,345.67, Euro Style = $12,345.67" , "US and European"
    assert checkio("$1.234, $5.678 and $9") == \
                   "$1,234, $5,678 and $9", "Dollars without cents"
    print('\n[+] All asserts passed!')
