import re


## Original solution
#def translate(phrase):
#    """Translate an ornithological phrase to english."""
#    strip_single_vowels = re.sub(r'([^aeiouy\s])[aeiouy]', r'\1', phrase)
#    return re.sub(r'([aeiouy]){3}', r'\1', strip_single_vowels)


# Re-factored
def translate(txt):
    """Translate an ornithological phrase to english."""
    return re.sub(r'([aeiouy])..', r'\1', re.sub(r'([^ aeiouy]).', r'\1', txt))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print(' [+] All asserts passed.')