def searchUnsortedArray(readerArray, target):
    low = 0
    high = 1
    

    # get the high pointer value
    while target > readerArray.get(high):
        low = high
        high = high*2


    # find the index of the target
    while low <= high:
        mid = low + (high-low)//2
        if readerArray.get(mid) == target:
            return mid
        elif readerArray.get(mid) > target: # right half discarded
            high = mid - 1
        else:
            low = mid + 1

    return -1

