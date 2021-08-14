def insertion_sort(lst):
    # This will iterate N-1 times
    for i in range(1, len(lst)):

        # The key we will be comparing to is the i index
        key = lst[i]

        # We will hold the index before i inside variable j
        j = i - 1

        # If the key is less than what is inside j, and j > 0
        # ....we will keep pushing the values to the right from the growing sorted sublist
        # Keep moving j back
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        # Put the key value one spot infront of J in the correct order of the growing sorted sublist on the left
        lst[j+1] = key

arr = [19, 633, 275, 653, 685, 72, 375, 11, 532, 18, 675, 148, 252, 371, 130, 813, 424, 162, 997, 921, 115, 96, 615,
       403, 112]

print("Insertion Sort")
insertion_sort(arr)

print(arr)