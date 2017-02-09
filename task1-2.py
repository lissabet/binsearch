def findindex(array,element):
    if element in array:
        return array.index(element)
    else:
        return None


def binsearch(array,element):
    if element in array:
        begin = 0
        end = len(array)-1
        middle = int(end/2)
        while array[middle] != element and begin < end:
            if element > array[middle]:
                begin = middle + 1
            else:
                end = middle - 1
            middle = int((begin + end)/2)
        return middle
    else:
        return None
