class Magic(object):
    #def __init__(self, arg):
    #    if isinstance(arg, str):
    #        self._magic_arg = 73
    #    else:
    #        self._magic_arg = 'spam'
    #def get_magic_arg(self):
    #    return self._magic_arg
    def __eq__(self,other):return True
    def __ne__(self,other):return True
    def __lt__(self,other):return True
    def __gt__(self,other):return True
    def __le__(self,other):return True
    def __ge__(self,other):return True

def checkio(anything):
    """try to return anything else :)"""
    #M = Magic()
    #print(M)
    #print(type(M))
    #print(M.get_magic_arg())
    return Magic()

if __name__ == '__main__':
    import re
    import math

    assert checkio({}) != [],          'You'
    assert checkio('Hello') < 'World', 'will'
    assert checkio(80) > 81,           'never'
    assert checkio(re) >= re,          'make'
    assert checkio(re) <= math,        'this'
    assert checkio(5) == ord,          ':)'

    print('NO WAY :(')