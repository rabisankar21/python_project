def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key

data = [9,5,1, 4,3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)


# 1st: step = 1, j = 0, key = 5
#     1: arr[1] = 9, j = -1, [9, 9, 1, 4,3]
# arr[0] = 5
# final arr = [5,9, 1,4, 3]
#
# 2nd: step= 2, j = 1, key = 1
#     1: arr[2] = 9, j = 0, [5, 9, 9, 4,3]
#     2: arr[1] = 5, j = -1, [5, 5, 9, 4,3]
# arr[0] = 1
# final arr = [1, 5, 9, 4, 3]
#
# 3rd: step =3, j = 2, key = 4
#     1: arr[3] = 9, j = 1, [1, 5, 9, 9, 3]
#     2: arr[2] = 5, j = 0, [1, 5, 5, 9, 3]
# arr[0+1] = 4
# final arr = [ 1, 4,  5, 9, 3]
#
# 4th: step = 4, j = 3, key = 3
#     1: arr[4] = 9, j  = 2, [1, 4, 5, 9, 9]
#     2: arr[3] = 5, j = 1, [1, 4, 5, 5, 9]
#     3: arr[2] = 4, j = 0, [1, 4, 4,5 , 9]
# arr[0+1] = 3
# final array = [1, 3, 4, 5, 9]



# def insertionSort(array):
#
#     for step in range(1, len(array)):
#         key = array[step]
#         j = step - 1
#         while j >= 0 and key > array[j]:
#             array[j + 1] = array[j]
#             j = j - 1
#         array[j + 1] = key
#
# data = [9,5,1, 4,3]
# insertionSort(data)
# print('Sorted Array in Desc. Order:')
# print(data)


