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
    return [x for x in itertools.chain(
        *itertools.zip_longest(
            *lists)) if x is not None]


def vinter_preallocated(*lists):
    temp = [None] * (max(map(len, lists)) * len(lists))
    N = len(lists)

    for i, l in enumerate(lists):
        for j, item in enumerate(l):
            temp[i + j*N] = item
    temp = [x for x in temp if x is not None]
    return temp


def vinter_procedural(*lists):
    temp = []
    for i in range(max(map(len, lists))):
        for l in lists:
            if i < len(l):
                temp.append(l[i])
    return temp


def vinter_procedural2(*lists):
    # unnecessary conditional branches ar the kryptonite of branch predictors
    # by culling from the input set as you go, conditional branches are removed
    # hence the sudden drop in execution time

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
