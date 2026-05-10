def flat(iterable):
    for item in iterable:
        if isinstance(item, list):
            yield from flatten(item)
        elif item is not None:
            yield item
    

def flatten(iterable):
    return list(flat(iterable))