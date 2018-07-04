def numbers_in_lists(string):
    bigger = 0
    result = []
    sublist = []
    for n in string:
        n = int(n)
        if n > bigger:
            if sublist:
                result.append(sublist)
                sublist = []
            result.append(n)
            bigger = n
        else:
            sublist.append(n)
    if sublist:
        result.append(sublist)
    return result