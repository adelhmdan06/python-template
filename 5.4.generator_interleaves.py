def interleave(*iterables):
    for group in zip(*iterables):
        for item in group:
            yield item
result = list(interleave('abc', [1, 2, 3], ('!', '@', '#')))
print(result)
