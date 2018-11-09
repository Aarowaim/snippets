import itertools


# ========== Finite amount of parameters ==========
def inter1(l1, l2):
    temp = []
    for i in range(len(max(l1, l2))):
        if i < len(l1):
             temp.append(l1[i])
        if i < len(l2):
             temp.append(l2[i])
    return temp


def inter2(l1, l2):
    small, large = min(l1, l2), max(l1, l2)
    front = list(itertools.chain(*zip(l1, l2)))
    back = large[len(small):]
    return front + back


# ========== Variadic amount of parameters ==========
def vinter_tools(*lists):
    '''iterators are powerful and concise, and more often than not are the most performant solution'''
    return [x for x in itertools.chain(
        *itertools.zip_longest(
            *lists)) if x is not None]
    

def vinter_preallocated(*lists):
    '''preallocates a list of the desired size and populates using one input list at a time, then a final step cleans up the default values
    _Default prevents collisions with lists containing None or other useful primitive datatypes, but does carry some overhead
    this is a fairly cache-friendly way to iterate, so while not as fast as builtins, still is performant'''
    _Default = type('_Default', (), {})
    temp = [_Default] * (max(map(len, lists)) * len(lists))
    N = len(lists)

    for i, l in enumerate(lists):
        for j, item in enumerate(l):
            temp[i + j*N] = item
    temp = [x for x in temp if x is not _Default]
    return temp


def vinter_procedural(*lists):
    '''this is the natural generalization of inter1 to variadics
    it has the notable issue of traversing each list even after i >= len'''
    temp = []
    for i in range(max(map(len, lists))):
        for l in lists:
            if i < len(l):
                temp.append(l[i])
    return temp


def vinter_procedural2(*lists):
    '''by culling from the iteration set as you go, execution time improves significantly'''

    temp = []
    valid = list(lists)

    for i in range(max(map(len, lists))):
        for l in valid:
            if i < len(l):
                temp.append(l[i])
            else:
                valid.remove(l)
    return temp


a = range(25)
b = range(100)
c = range(50)

if __name__ == '__main__':
    import timeit
    for fn in filter(lambda x: hasattr(x, '__name__') and 'vinter' in x.__name__, list(locals().values())):
        print(fn.__name__, ':')
        print('\t', timeit.timeit(
            f'{fn.__name__}({a}, {b}, {c})',
            setup=f'from __main__ import {fn.__name__}'))
