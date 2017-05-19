
def create_heap():
    """Create a heap"""
    return []

#
# Cormen implementation of HEAP
#
def parent(i):
    return (i - 1) / 2

def left(i):
    return i * 2 + 1

def right(i):
    return i * 2 + 2

def swap(h, i, j):
    temp = h[i]
    h[i] = h[j]
    h[j] = temp

def max_heapfiy(h, i, hl = -1):
    if hl == -1:
        hl = len(h)
    l = left(i)
    r = right(i)
    largest = i
    if l < hl and h[l] > h[largest]:
        largest = l
    if r < hl and h[r] > h[largest]:
        largest = r
    if largest != i:
        swap(h, i, largest)
        max_heapfiy(h, largest, hl)

def max_heap_insert(h, value):
    i = len(h)
    h.append(value)
    while i > 0 and h[parent(i)] < h[i]:
        swap(h, parent(i), i)
        i = parent(i)

def heap_extract_max(h):
    if len(h) < 1:
        return 0
    max = h[0]
    h[0] = h.pop()
    max_heapfiy(h, 0)
    return max

def heap_maximum(h):
    return h[0]

def build_max_heap(h, hl=-1):
    if hl == -1:
        hl = len(h)
    for i in reversed(range(0, hl/2)):
        print i
        print h
        max_heapfiy(h, i, hl)

def heap_sort(h):
    build_max_heap(h)
    hl = len(h)
    for i in reversed(range(1, len(h))):
        swap(h, 0, i)
        hl = hl - 1
        max_heapfiy(h, 0, hl)



