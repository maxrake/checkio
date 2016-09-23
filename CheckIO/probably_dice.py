## first attempt: brute force - too slow
#import itertools
#import collections
#
#def probability(dice_number, sides, target):
#    """Compute the probability of rolling a target sum with dice."""
#    rolls = itertools.product(range(1, sides + 1), repeat=dice_number)
#    roll_dict = collections.defaultdict(int)
#    for roll in rolls:
#        key = sum(roll)
#        roll_dict[key] += 1
#    return round(roll_dict.get(target, 0) / sum(roll_dict.values()), 4)


from itertools import combinations_with_replacement as cwr
from math import factorial
from collections import Counter


def probability(num_dice, sides, target):
    """Compute the probability of rolling a target sum with dice."""
    enums = (x for x in cwr(range(1, sides + 1), num_dice) if sum(x) == target)
    ways_to_get_target = 0
    
    for enum in enums:
        perms = factorial(num_dice)
        ctr = Counter(enum)
        for count in ctr:
            perms = perms / factorial(ctr[count])
        ways_to_get_target += perms
    
    return round(ways_to_get_target / (sides ** num_dice), 4)


if __name__ == '__main__':
    #These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision
        
    assert(almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert(almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert(almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert(almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert(almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert(almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert(almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
    print(' [+] All asserts passed.')
