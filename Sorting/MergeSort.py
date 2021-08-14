def merge_sort(lst):

    # If lst is 1 or less, don't do anything
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left) # sort left list
        merge_sort(right) # sort right rist

        # Initialize Variables
        i = 0
        j = 0
        k = 0

        # Copy data to temp lists left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        # Checking if any element was right
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1


arr = [19, 633, 275, 653, 685, 72, 375, 11, 532, 18, 675, 148, 252, 371, 130, 813, 424, 162, 997, 921, 115, 96, 615,
       403, 112]

print("Merge Sort")
merge_sort(arr)

print(arr)