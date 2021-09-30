# https://www.geeksforgeeks.org/sorting-algorithms/
# https://www.w3resource.com/ODSA/AV/Sorting/shellsortAV.html

import time
from sorters import Sorters
from visualizer import Visualizer

# Number of items = items in the list

numberOfItems = 35
randomList = [i + 1 for i in range(numberOfItems)]
sortedList = sorted(randomList)
# SeeSort is just for the terminal. Don't put True unless you want a seizure
seeSort = False

visualizer = Visualizer()
sorter = Sorters(randomList, sortedList, seeSort)

def continueThings():

    # Causes a time buffer and then randomizes the local list
    # for the algorithm to sort
    time.sleep(2)
    sorter.randomize()

def finished():
    # Runs whenever the program is complete
    time.sleep(10)

def main():

    # Runs continue Things and then triggers the sorting algorithm

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
    sorter.stoogesort(0, len(randomList) - 1, 0)
    continueThings()
    sorter.cocktailSort(0)
    continueThings()
    sorter.bogo_sort(0)
    finished()

if __name__ == "__main__":
    main()