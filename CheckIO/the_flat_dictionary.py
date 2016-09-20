def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        if current:
            for k, v in current.items():
                if isinstance(v, dict):
                    stack.append((path + (k,), v))
                else:
                    result["/".join((path + (k,)))] = v
        else:
            result["/".join(path)] = ''
    return result

if __name__ == "__main__":
    assert flatten({'key':'value'}) == {'key':'value'}, "simple"
    assert flatten({'key':{'deeper':{'more':{'enough':'value'}}}}) == {'key/deeper/more/enough':'value'}, "nested"
    assert flatten({'empty':{}}) == {'empty':''}, "empty value"