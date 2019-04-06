unsorted_list = [5, 2, 3, 6, 1, 3]

#insertion sort ->

for j in range(1, len(unsorted_list)):
    key = unsorted_list[j]
    #insert unsorted_list[j] into the sorted sequence unsorted_list[1...j-1]
    i = j - 1
    while i >= 0 and unsorted_list[i] > key:
        unsorted_list[i + 1] = unsorted_list[i]
        i = i - 1
    unsorted_list[i + 1] = key

print(unsorted_list)