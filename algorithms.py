# https://www.geeksforgeeks.org/sorting-algorithms/

import os
from sorters import Sorters

numberOfItems = 9
randomList = [i + 1 for i in range(numberOfItems)]
sortedList = sorted(randomList)
seeSort = True

sorter = Sorters(randomList, sortedList, seeSort)

def optimized():
    sorter.radix_sort()
    sorter.selection_sort()
    sorter.bogo_sort()
    sorter.insert_sort()
    sorter.pancake_sort()
    sorter.bubble_sort()

def notOptimized():
    pass

def notMade():
    sorter.shell_sort()
    sorter.heap_sort()
    sorter.merge_sort()
    sorter.quick_sort()

def continueThings():
    input("Press 'Enter' to Continue > ")
    os.system('cls')
    print("Computing . . . ")

countBubble = sorter.bubble_sort(0)
print("BUBBLE SORT --- Total Iterations: {}".format(countBubble))
if numberOfItems < 11:
    continueThings()
    countBogo = sorter.bogo_sort(0)
    print("BOGO SORT --- Total Iterations: {}".format(countBogo))
continueThings()
countInsert = sorter.insert_sort(0)
print("INSERT SORT --- Total Iterations: {}".format(countInsert))
# continueThings()
# countQuick = quick_sort(randomList, count, seeSort)
# print("QUICKSORT --- Total Iterations: {}".format(countQuick))
# continueThings()
# countMerge = merge_sort(randomList, count, seeSort)
# print("MERGE SORT --- Total Iterations: {}".format(countMerge))
continueThings()
countSelection = sorter.selection_sort(0)
print("SELECTION SORT --- Total Iterations: {}".format(countSelection))
# continueThings()
# countHeap = heap_sort(randomList, count, seeSort)
# print("HEAP SORT --- Total Iterations: {}".format(countHeap))
# continueThings()
# countShell = shell_sort(randomList, count, seeSort)
# print("SHELL SORT --- Total Iterations: {}".format(countShell))
continueThings()
countPancake = sorter.pancake_sort(0)
print("PANCAKE SORT --- Total Iterations: {}".format(countPancake))
continueThings()
countRadix = sorter.radix_sort(0)
print("RADIX SORT --- Total Iterations: {}".format(countRadix))