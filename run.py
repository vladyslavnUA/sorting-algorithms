# from timer import Timer


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    # t = Timer()
    # t.start()

    sorted_list = items[:]
    sorted_list.sort()
    if sorted_list == items:
        # t.stop()
        return "list is sorted"
    else:
        # t.stop()
        return "list unsorted"

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    for a in range(len(items)):
        for b in range(len(items) - 1):
            if items[b] > items[b+1]:
                items[b], items[b+1] = items[b+1], items[b]

    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items

items = [3, 15, 4, 20, 6, 18, 11, 9, 7]
print(is_sorted(items))
# print("sorting took: ", timeit.timeit(is_sorted(items)))
print(bubble_sort(items))
# print("sorting took: ", timeit.timeit(bubble_sort(items)))