def join(*lists, sep='-'):
    if not lists:
        return None

    result = []

    for i, current_list in enumerate(lists):
        result.extend(current_list)

        if i < len(lists) - 1:
            result.append(sep)

    return result



print(join([1, 2], [8], [9, 5, 6], sep='@'))
print(join([1, 2], [8], [9, 5, 6]))
print(join([1]))
print(join())
