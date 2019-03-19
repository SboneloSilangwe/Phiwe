def bubble_sort(items):
    for i in range(len(items)-1,0,-1):
        for j in range(i):
            if items[j]> items[j+1]:
                items[j],items[j+1]=items[j+1],items[j]

    '''Return array of items, sorted in ascending order'''
    return items

def merge_sort(items):
    if len(items) < 2:
        return items

    result,mid = [],int(len(items)/2)

    n = merge_sort(items[:mid])
    z = merge_sort(items[mid:])

    while (len(n) > 0) and (len(z) > 0):
            if n[0] > z[0]:result.append(z.pop(0))
            else:result.append(n.pop(0))

    result.extend(n+z)

    '''Return array of items, sorted in ascending order'''
    return result

def quick_sort(items):
    if len(items) == 0:
        return items
    pivot = items[0]
    pivots = [x for x in items if x == pivot]
    smaller = quick_sort([x for x in items if x < pivot])
    larger = quick_sort([x for x in items if x > pivot])

    '''Return array of items, sorted in ascending order'''
    return smaller + pivots + larger
