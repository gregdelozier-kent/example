def parse(s):
    if s == "":
        return None
    if s[0] == "-":
        sign = -1
        s = s[1:]
    else:
        sign = 1
    v = 0
    fractional = False
    column_value = 1
    for c in s:
        if c == '.':
            if fractional:
                return None
            fractional = True
            continue
        if not c in "0123456789":
            return None
        if fractional:
            column_value = column_value / 10
            v = v + (ord(c) - ord('0')) * column_value
        else:
            v = v * 10 + ord(c) - ord('0')
    return v * sign
