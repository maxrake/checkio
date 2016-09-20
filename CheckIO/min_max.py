## First submission:
#def min_max(*args, is_min=True, **kwargs):
#    key = kwargs.get("key", None)
#    items = iter(args) if len(args) > 1 else iter(args[0])
#    return_item = next(items)
#    return_val = key(return_item) if key is not None else return_item
#    while True:
#        try:
#            item = next(items)
#        except StopIteration:
#            return return_item
#        val = key(item) if key is not None else item
#        if is_min:  # min function
#            if val < return_val:
#                return_item, return_val = item, val
#        else:       # max function
#            if val > return_val:
#                return_item, return_val = item, val
#
#def min(*args, **kwargs):
#    return min_max(*args, is_min=True, **kwargs)
#
#def max(*args, **kwargs):
#    return min_max(*args, is_min=False, **kwargs)


# Refactored
def min_max(*args, is_min=True, **kwargs):
    key = kwargs.get("key", lambda x: x)
    items = iter(args if len(args) > 1 else args[0])
    return_item = next(items)
    for item in items:
        if is_min:  # min function
            if key(item) < key(return_item):
                return_item = item
        else:       # max function
            if key(item) > key(return_item):
                return_item = item
    return return_item

def min(*args, **kwargs):
    return min_max(*args, is_min=True, **kwargs)

def max(*args, **kwargs):
    return min_max(*args, is_min=False, **kwargs)


## Best answer I saw
#def sort_args(args, key_func=None, reverse=False):
#    if len(args) == 1:
#        args = args[0]
#    return sorted(args, key=key_func, reverse=reverse)[0]
#??
#def min(*args, **kwargs):
#    key = kwargs.get("key", None)
#    return sort_args(args, key_func=key)
#??
#def max(*args, **kwargs):
#    key = kwargs.get("key", None)
#    return sort_args(args, key_func=key, reverse=True)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    assert min(abs(i) for i in range(-10, 10)) == 0, "Generator object"
    print(" [+] All asserts passed.")
