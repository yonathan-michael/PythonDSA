def SelectionSort(lst):
    # Outer iteration is n-1 times
    for i in range(0, len(lst) - 1):
        # If we don't find a minimum element in the sublist ,
        # the default is the i index, swap will be with itself if need be
        min_index = i
        # Inner iterator goes from the index in front of i , all the way to the end
        for j in range(i + 1, len(lst)):
            # By the end of this loop, we will capture the new min index
            if lst[j] <= lst[min_index]:
                min_index = j
        # At the end of the inner loop, we swap the new minimum index with i , attaching it to the end of
        # the growing sublist
        lst[i], lst[min_index] = lst[min_index], lst[i]


arr = [19, 633, 275, 653, 685, 72, 375, 11, 532, 18, 675, 148, 252, 371, 130, 813, 424, 162, 997, 921, 115, 96, 615,
       403, 112]

print("Selection Sort")

SelectionSort(arr)

print(arr)
