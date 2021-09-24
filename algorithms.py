# https://www.geeksforgeeks.org/sorting-algorithms/
# https://www.w3resource.com/ODSA/AV/Sorting/shellsortAV.html

import random
import time
from sorters import Sorters
from visualizer import Visualizer

numberOfItems = 51
randomList = [i + 1 for i in range(numberOfItems)]
sortedList = sorted(randomList)
seeSort = False

visualizer = Visualizer()
sorter = Sorters(randomList, sortedList, seeSort)

def optimized():
    sorter.bubble_sort()
    sorter.bogo_sort()
    sorter.pancake_sort()
    sorter.selection_sort()
    sorter.radix_sort()

def notOptimized():
    sorter.insert_sort() # THIS IS BROKE

def notMade():
    sorter.shell_sort()
    sorter.heap_sort()
    sorter.merge_sort()
    sorter.quick_sort()

def continueThings():
    time.sleep(5)
    sorter.randomize()

def finished():
    time.sleep(10)

def main():
    continueThings()
    countBubble = sorter.bubble_sort(0)
    print("BUBBLE SORT --- Total Iterations: {}".format(countBubble))
    if numberOfItems <= 8:
        continueThings()
        countBogo = sorter.bogo_sort(0)
        print("BOGO SORT --- Total Iterations: {}".format(countBogo))
    continueThings()
    countInsert = sorter.insert_sort(0)
    print("INSERT SORT --- Total Iterations: {}".format(countInsert))
    continueThings()
    countSelection = sorter.selection_sort(0)
    print("SELECTION SORT --- Total Iterations: {}".format(countSelection))
    continueThings()
    countPancake = sorter.pancake_sort(0)
    print("PANCAKE SORT --- Total Iterations: {}".format(countPancake))
    continueThings()
    countRadix = sorter.radix_sort(0)
    print("RADIX SORT --- Total Iterations: {}".format(countRadix))
    continueThings()
    countGnome = sorter.gnome_sort(0)
    print("GNOME SORT --- Total Iterations: {}".format(countGnome))
    # countHeap = heap_sort(randomList, count, seeSort)
    # print("HEAP SORT --- Total Iterations: {}".format(countHeap))
    continueThings()
    countShell = sorter.shell_sort(0)
    print("SHELL SORT --- Total Iterations: {}".format(countShell))
    continueThings()
    countOddEven = sorter.oddEvenSort(0)
    print("ODDEVEN SORT --- Total Iterations: {}".format(countOddEven))
    continueThings()
    countStooge = sorter.stoogesort(0, 0, len(randomList) - 1)
    print("STOOGE SORT --- Total Iterations: {}".format(countStooge))
    continueThings()
    countCocktail = sorter.cocktailSort(0)
    print("COCKTAIL SORT --- Total Iterations: {}".format(countCocktail))
    # continueThings()
    # countQuick = quick_sort(randomList, count, seeSort)
    # print("QUICK SORT --- Total Iterations: {}".format(countQuick))
    # continueThings()
    # countMerge = merge_sort(randomList, count, seeSort)
    # print("MERGE SORT --- Total Iterations: {}".format(countMerge))
    finished()

if __name__ == "__main__":
    main()