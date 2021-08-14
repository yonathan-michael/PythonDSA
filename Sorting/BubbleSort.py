def bubble_sort(lst):
    # We traverse through all list elements
    for i in range(len(lst)):

        # The last "i" elements are in place, starts with 0 being in place
        for j in range(0, len(lst) - i - 1):

            if lst[j] > lst[j + 1]:

                lst[j], lst[j+1] = lst[j+1], lst[j]



arr = [19, 633, 275, 653, 685, 72, 375, 11, 532, 18, 675, 148, 252, 371, 130, 813, 424, 162, 997, 921, 115, 96, 615,
       403, 112]

print("Bubble Sort")
bubble_sort(arr)

print(arr)