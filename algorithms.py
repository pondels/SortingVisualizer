# https://www.geeksforgeeks.org/sorting-algorithms/
# https://www.w3resource.com/ODSA/AV/Sorting/shellsortAV.html

import time
from sorters import Sorters
from visualizer import Visualizer

numberOfItems = 35
randomList = [i + 1 for i in range(numberOfItems)]
sortedList = sorted(randomList)
seeSort = False

visualizer = Visualizer()
sorter = Sorters(randomList, sortedList, seeSort)

def continueThings():
    time.sleep(2)
    sorter.randomize()

def finished():
    time.sleep(10)

def main():
    continueThings()
    sorter.bubble_sort(0)
    continueThings()
    sorter.insert_sort(0)
    continueThings()
    sorter.selection_sort(0)
    continueThings()
    sorter.pancake_sort(0)
    continueThings()
    sorter.radix_sort(0)
    continueThings()
    sorter.gnome_sort(0)
    continueThings()
    sorter.shell_sort(0)
    continueThings()
    sorter.oddEvenSort(0)
    continueThings()
    sorter.stoogesort(0, 0, len(randomList) - 1)
    continueThings()
    sorter.cocktailSort(0)
    continueThings()
    sorter.bogo_sort(0)
    finished()

if __name__ == "__main__":
    main()