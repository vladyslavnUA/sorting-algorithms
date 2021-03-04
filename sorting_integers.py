def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # final is based on how many numbers in array
    final = [0] * len(numbers)

    # set the count for each element
    counting = [0] * 10

    # figure out how many times numbers are displayed
    for a in range(0, len(numbers)):
        counting[numbers[a]] += 1
    
    # count the times they're shown
    for b in range(1, 10):
        counting[b] += counting[b-1]

    # grab elements from array and append to final
    item = len(numbers) - 1
    while item >= 0:
        final[counting[numbers[item]] - 1] = numbers[item]
        counting[numbers[item]] -= 1
        item -= 1
    
    # mutating the final result array
    for c in range(0, len(numbers)):
        numbers[c] = final[c]
    
    return numbers


def bucket_sort(numbers, buckets=5):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    final=[]

    # get bucket amount from length of array, 5
    for i in range(len(numbers)):
        final.append([])
    
    # looping through the range of array to place index into bucket 
    size = len(numbers)
    for a in range(0, size):
        b = int(numbers[a] * size)
        final[b].append(numbers[a])

    # sort the buckets
    for c in range(0, size):
        final[c].sort()

    # loop over final array to place sorted into original array
    item = 0
    for a in range(0, size):
        for b in range(0, len(final[a])):
            numbers[item] = final[a][b]
            item += 1

    print("Sorted data is:")        
    print(numbers)

numbers=[0.55, 0.21, 0.78, 0.42, 0.99]
print("Counting Sort: \n", counting_sort([4, 2, 2, 8, 3, 3, 1]))
bucket_sort(numbers)
