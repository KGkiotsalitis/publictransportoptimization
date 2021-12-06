import sympy as sp

#write bubble sort algorithm
def bubble_sort(items):
    '''
    :param items
    '''

    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]

print(bubble_sort(5))