def linear_search(lst,key):

    for i in range(len(lst)):

        if lst[i] == key:

            return i

    return -1

arr = [19, 633, 275, 653, 685, 72, 375, 11, 532, 18, 675, 148, 252, 371, 130, 813, 424, 162, 997, 921, 115, 96, 615,
       403, 112]

print("Linear Search")
print(linear_search(arr,193883193))
