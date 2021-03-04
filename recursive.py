def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list

    # merged lists
    final = []

    # get length of lists to sort through items
    one = len(items1)
    two = len(items2)

    # set the start points
    start, start2 = 0, 0

    # sort through lists starting at the beginning, the smallest item
    while start < one and start2 < two:
        # now we check if the smallest item of list one is greater than smallest in list two
        if items1[start] < items2[start2]:
            # add it to list 
            final.append(items1[start])    
            # continue to next node
            start += 1
        # if the smallest in list one is not greater than smallest in ;list two, add list two item
        else:
            final.append(items2[start2])
            start2 += 1  # continue

    # merge the lists 
    final += items1[start:]
    final += items2[start2:]

    print(f" Original Lists: \n  {items1} \n  {items2} \n Merged Lists: {final}")
    return final


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order

    # base case
    if len(items) <= 1:
        print(' Why so empty 😢? Your List: \n ', items)
        return items
    # if array if greater than 1 item, split in half
    centre = len(items) // 2    # floor division
    right = merge_sort(items[centre:])  # grab right items
    left = merge_sort(items[:centre])  # grab left items

    return merge(left, right)
    print(merge(left, right))

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p

    index = low - 1
    pivot = items[high]

    for i in range(low, high):
        if items[i] <= pivot:
            index += 1
            items[index], items[i] = items[i], items[index]
    items[index + 1], items[high] = items[high], items[index + 1]
    return index + 1


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
    if low < high:
        partion = partition(items, low, high)
        quick_sort(items, low, partion-1)
        quick_sort(items, partion+1, high)
        return items

    if len(items) == 0:
        return f'already sorted: {items}'


print('#####  MERGE  #####')
merge([1, 5, 6, 9, 11], [3, 4, 7, 8, 10])

print('')
print('#####  MERGE SORT  #####')
merge_sort([45, 90, 1, 34, 22, 5, 68])

print('')
print('#####  QUICK SORT  #####')
numbers = [36, 78, 4, 25, 12, 8, 68]
quick_sort(numbers, 0, len(numbers)-1)
f = []

for num in range(len(numbers)):
    f.append(numbers[num])
print(f)
