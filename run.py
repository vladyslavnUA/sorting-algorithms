import time

def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    start = time.time()

    sorted_list = items[:]
    sorted_list.sort()    # python sorts the list for us
    if sorted_list == items:     # check if sorted is = to given array
        end = time.time()
        print(f"Runtime of is sorted: {end - start}")
        return "list is sorted"
    else:
        end = time.time()
        print(f"Runtime of is sorted: {end - start}")
        return "list unsorted"

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    start = time.time()

    for a in range(len(items)):
        for b in range(len(items) - 1):
            if items[b] > items[b+1]:
                items[b], items[b+1] = items[b+1], items[b]

    end = time.time()
    print(f"Runtime of bubble sort: {end - start}")
    return "Bubble Sort: ", items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item

    start = time.time()
    for i in range(len(items)):
        smallest = i

        for b in range(i+1, len(items)):
            if items[b] < items[smallest]:
                smallest = b
        
        swap = items[i]
        items[i] = items[smallest] 
        items[smallest] = swap

    end = time.time()
    print(f"Runtime of selection sort: {end - start}")
    return "Selection Sort: ", items

def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    
    start = time.time()
    for i in range(1, len(items)): # looping through each item
        val = items[i]    # getting the value of current index
        index = i         # getting the current index

        while index > 0 and items[index-1] > val:
            items[index] = items[index-1]     # going through the list to find the correct sequence
            index -= 1  
        items[index] = val    # found it
        end = time.time()
        print(f"Runtime of insertion sort: {end - start}")
        return "Insertion Sort: ", items



items = [3, 15, 4, 20, 6, 18, 11, 9, 7]
print(is_sorted(items))
print(bubble_sort(items))
print(selection_sort(items))
print(insertion_sort(items))