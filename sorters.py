import random
from visualizer import Visualizer
import time

class Sorters():

    def __init__(self, list, sorted, seeSort):

        '''
        INITIALIZED BASIC INFORMATION FOR THE SORTING
        ALGORITHMS TO FUNCTION PROPERLY
        '''
        self.seeSort = seeSort
        self.list = list
        self.sorted = sorted
        self.visualizer = Visualizer()
        self.speedUp = True
        self.speedUpCount = 0

    def randomize(self):
        '''
        Called whenever a new sorter is called so that 
        the list is for sure the most random
        it can be.
        '''
        random.shuffle(self.list)

    def flip(self, list, smallest_num, ignoreNums, count, seeSort):
        # Triggered every time the list needs to be flipped
        
        
        # Finds the next smallest item and splits the list into 2 parts
        indexOfI = list.index(smallest_num)
        back_list = list[indexOfI:]

        # Reverses that part of the list and sticks it back with the front list, appending to the new_list
        back_list.reverse()
        count += 1
        front_list = list[:indexOfI]
        new_list = front_list + back_list

        # Reinitializes values for the list and reverses the new list
        first_values, new_list = new_list[:len(list) - ignoreNums], new_list[len(list) - ignoreNums:]
        if seeSort:
            print(first_values + new_list)
        new_list.reverse()
        count += 1

        # New list updated with repositioned value
        new_list = first_values + new_list
        self.visualizer.run_self(new_list, smallest_num, smallest_num, False, "Pancake Sort", count)
        return new_list, count

    def pancake_sort(self, count):
        backup_list = [i for i in self.list]
        sorted_list = [i for i in self.list]
        sorted_list.sort()

        # Continues running until the list is sorted
        while self.list != sorted_list:
            # Finds the smallest value
            smallest_num = min(backup_list)
            self.list, count = self.flip(self.list, smallest_num, len(backup_list), count, self.seeSort)
            if self.seeSort:
                print(self.list)

            # Pops the smallest number so the program knows what number to look for next
            # (dirty trick I know...)
            backup_list.pop(backup_list.index(smallest_num))
        return count

    def radix_sort(self, count):

        max_length = len(str(max(self.list)))
        items = 0

        # Runs from 1 to the length of the list + 1
        # Then runs from 0 - 9 checking each individual integer for sorting
        # Then runs through the entire list

        for n in range(1, max_length + 1):
            for num in range(10):
                for i in range(len(self.list)):
                    # Finds the values of the current item
                    intValue = len(str(self.list[i])) - n
                    indexOfI = self.list.index(self.list[i])
                    currentValue = self.list[indexOfI]

                    # Checks to see if the value has more numbers in front of it
                    if intValue > -1:
                        checkValue = int(str(self.list[i])[intValue])
                    else:
                        # This is usually if it's checking a number like 20 and 9 and 9 only has 1 digit whereas 20 has 2,
                        # so 9 would return 0 because it's checking 20, 09 and 9 is a 0
                        checkValue = 0

                    if checkValue == num:
                        # Found the next smallest number so it pops it and inserts it into the new position
                        self.list.pop(indexOfI)
                        self.list.insert(items, currentValue)
                        items += 1
                    count += 1
                    self.speedUpCount += 1

                    # Visuals
                    if self.speedUpCount >= 20:
                        self.visualizer.run_self(self.list, indexOfI, -1, self.speedUp, "RadixSort", count)
                    else:
                        self.visualizer.run_self(self.list, indexOfI, -1, False, "Radix Sort", count)
                    if self.seeSort:
                        print(self.list)
                if self.sorted == self.list:
                    break
            items = 0
        self.speedUpCount = 0
        return count

    def insert_sort(self, count):

        # INSERT SORT CODE CREDIT TO MOHIT KUMRA
        # https://www.geeksforgeeks.org/insertion-sort/

        # 10 TIMES MORE OPTIMIZED THAN MY CODE SO... KUDDOS

        for i in range(1, len(self.list)):
 
            num = self.list[i]
    
            j = i-1
            while j >= 0 and num < self.list[j] :
                self.list[j + 1] = self.list[j]
                j -= 1
                count += 1
                self.visualizer.run_self(self.list, j, i, False, "Insert Sort", count)
            self.list[j + 1] = num
        self.visualizer.run_self(self.list, j, i, False, "Insert Sort", count)

        return count

    def checkForCorrectBogo(self, list):

        '''
        Total Amount checks for the amount of numbers that
        were in the correct spot
        '''

        totalAmount = 0


        for i in range(len(list)):
            # Goes through the list and checks for a correct item
            # Compared to the sorted list
            if self.sorted[i] == list[i]:
                totalAmount += 1
        return totalAmount

    def bogo_sort(self, count):

        # totalBogo is a list of lists that appends a number
        # of items to check how many times it had x amount
        # of numbers correct when it randomized
        new_list = [i + 1 for i in range(7)]
        random.shuffle(new_list)
        totalBogo = [[] for _ in range(len(self.list) + 1)]

        # Runs while the list isn't sorted
        self.sorted = [i + 1 for i in range(7)]
        while new_list != self.sorted:
            count += 1
            # Shuffles the list
            random.shuffle(new_list)
            # Runs the new list into the checkForCorrectBogo
            # And then appends an item to the totalBogo
            # to the index value where the number
            # of items that were correct
            amount = self.checkForCorrectBogo(new_list)
            totalBogo[amount].append("")
            # Visualizes the list being 'sorted'
            self.visualizer.run_self(new_list, -1, None, True, "Bogo Sort", count)

        if self.seeSort:
            totalLoops = -1
            for i in totalBogo:
                totalLoops += 1
                print(f"\033[95mThere were a total of \033[92m{len(i)}\033[95m iterations that had \033[92m{totalLoops} \033[95mnumber(s) \033[92mcorrect.\033[0m")
        return count

    def bubble_sort(self, count):

        swapValue = False

        # Runs while it's not sorted
        while self.list != self.sorted:
            # Runs for the number of items in the list to check everything
            for i in range(len(self.list)):
                
                # Fail safe
                if i + 1 == len(self.list):
                    break
                else:
                    # Checks the values it's comparing
                    first_value, second_value = self.list[i], self.list[i + 1]

                    if first_value > second_value:
                        # Swaps the values if the left item is greater than the right
                        self.list[i+1], self.list[i] = self.list[i], self.list[i + 1]
                        swapValue = True
                    else:
                        swapValue = False
                    self.speedUpCount += 1
                    if self.speedUpCount >= 20:
                        self.visualizer.run_self(self.list, self.list.index(first_value), self.list.index(second_value), self.speedUp, "Bubble Sort", count)
                    else:
                        self.visualizer.run_self(self.list, self.list.index(first_value), self.list.index(second_value), False, "Bubble Sort", count)
                    count += 1
                    if self.seeSort:
                        if swapValue:
                            print(self.list, f"\033[91mVALUES SWAPPED\033[0m: \033[91m[{self.list[i+1], self.list[i]}]\033[0m \033[95mITERATION\033[0m: \033[92m{count}\033[0m")
                        else:
                            print(self.list, f"\033[92mVALUES CHECKED\033[0m: \033[92m[{self.list[i+1], self.list[i]}]\033[0m \033[95mITERATION\033[0m: \033[92m{count}\033[0m")         
        self.speedUpCount = 0
        return count

    def shell_sort(self, count):

        # CREDIT TO SHUBHAM PRASHAR
        # https://www.geeksforgeeks.org/shellsort/

        gap = len(self.list) // 2 # initialize the gap
 
        while gap > 0:
            i = 0
            j = gap
            
            # check the array in from left to right
            # till the last possible index of j
            while j < len(self.list):
        
                if self.list[i] >self.list[j]:
                    self.list[i],self.list[j] = self.list[j],self.list[i]
                    count += 1

                i += 1
                j += 1
            
                # now, we look back from ith index to the left
                # we swap the values which are not in the right order.
                k = i
                while k - gap > -1:
    
                    if self.list[k - gap] > self.list[k]:
                        self.list[k-gap],self.list[k] = self.list[k],self.list[k-gap]
                        count += 1
                    k -= 1
                self.speedUpCount += 1
                if self.speedUpCount >= 20:
                    self.visualizer.run_self(self.list, j, i, self.speedUp, "Shell Sort", count)    
                else:
                    self.visualizer.run_self(self.list, j, i, False, "Shell Sort", count)
            gap //= 2
        self.speedUpCount = 0
        return count

    def gnome_sort(self, count):

        # CREDIT TO HARSHIT AGRAWAL
        # https://www.geeksforgeeks.org/gnome-sort-a-stupid-one/

        index = 0
        n = len(self.list)
        while index < n:
            if index == 0:
                index = index + 1
            if self.list[index] >= self.list[index - 1]:
                index = index + 1
            else:
                self.list[index], self.list[index-1] = self.list[index-1], self.list[index]
                index = index - 1
            count += 1
            self.speedUpCount += 1
            if self.speedUpCount >= 20:
                self.visualizer.run_self(self.list, index, index+1, self.speedUp, "Gnome Sort", count)
            else:
                self.visualizer.run_self(self.list, index, index+1, False, "Gnome Sort", count)
        self.speedUpCount = 0
        return count

    def selection_sort(self, count):

        current_number = ''
        index = 0
        while self.list != self.sorted:
            for i in range(0, len(self.list)-index):
                if current_number == '':
                    current_number = self.list[i]
                if self.list[i] < current_number:
                    current_number = self.list[i]
                self.speedUpCount += 1
                if self.speedUpCount >= 50:
                    self.visualizer.run_self(self.list, self.list.index(current_number), i, self.speedUp, "Selection Sort", count)
                else:
                    self.visualizer.run_self(self.list, self.list.index(current_number), i, False, "Selection Sort", count)
                count += 1
            indexOfI = self.list.index(current_number)
            self.list.pop(indexOfI)
            self.list.append(current_number)
            self.speedUpCount += 1
            if self.speedUpCount >= 20:
                self.visualizer.run_self(self.list, self.list.index(current_number), -1, self.speedUp, "Selection Sort", count)
            else:
                self.visualizer.run_self(self.list, self.list.index(current_number), -1, False, "Selection Sort", count)
            current_number = ''
            index += 1
            if self.seeSort:
                print(f"FOUND {current_number} IN INDEX {indexOfI} OF {self.list}")
        if self.seeSort:
            print(f"SORTED LIST: {self.list}")
        self.speedUpCount = 0
        return count

    def oddEvenSort(self, count):

        # CREDIT FOR SORTER -- MOHIT GUPTA_OMG <(0_o)>
        # https://www.geeksforgeeks.org/odd-even-sort-brick-sort/

        # Initially array is unsorted
        n = len(self.list)
        isSorted = 0
        while isSorted == 0:
            isSorted = 1
            temp = 0
            for i in range(1, n-1, 2):
                if self.list[i] > self.list[i+1]:
                    self.list[i], self.list[i+1] = self.list[i+1], self.list[i]
                    isSorted = 0
                    count += 1
                    self.speedUpCount += 1
                    if self.speedUpCount >= 20:
                        self.visualizer.run_self(self.list, i, i+1, self.speedUp, "OddEven Sort", count)
                    else:
                        self.visualizer.run_self(self.list, i, i+1, False, "OddEven Sort", count)
                    
            for i in range(0, n-1, 2):
                if self.list[i] > self.list[i+1]:
                    self.list[i], self.list[i+1] = self.list[i+1], self.list[i]
                    isSorted = 0
                    count += 1
                    self.speedUpCount += 1
                    if self.speedUpCount >= 20:
                        self.visualizer.run_self(self.list, i, i+1, self.speedUp, "OddEven Sort", count)
                    else:
                        self.visualizer.run_self(self.list, i, i+1, False, "OddEven Sort", count)
        self.speedUpCount = 0
        return count

    def stoogesort(self, count, l, h):
        # CREDIT TO -- Mohit Gupta_OMG <(0_o)>
        # https://www.geeksforgeeks.org/stooge-sort/

        if l >= h:
            return count
    
        # If first element is smaller
        # than last, swap them
        if self.list[l]>self.list[h]:
            count += 1
            t = self.list[l]
            self.list[l] = self.list[h]
            self.list[h] = t
            self.speedUpCount += 1
            if self.speedUpCount >= 20:
                self.visualizer.run_self(self.list, l, h, self.speedUp, "Stooge Sort", count)
            else:
                self.visualizer.run_self(self.list, l, h, False, "Stooge Sort", count)
        # If there are more than 2 elements in
        # the array
        if h-l + 1 > 2:
            t = (int)((h-l + 1)/3)
    
            # Recursively sort first 2 / 3 elements
            self.stoogesort(count, l, (h-t))
    
            # Recursively sort last 2 / 3 elements
            self.stoogesort(count, l + t, (h))
    
            # Recursively sort first 2 / 3 elements
            # again to confirm
            self.stoogesort(count, l, (h-t))
        self.speedUpCount = 0
        return count
    
    def cocktailSort(self, count):
        # CREDIT TO -- Unknown (Possibly the creators of the site)
        # https://www.geeksforgeeks.org/cocktail-sort/

        n = len(self.list)
        swapped = True
        start = 0
        end = n-1
        while (swapped == True):
    
            # reset the swapped flag on entering the loop,
            # because it might be true from a previous
            # iteration.
            swapped = False
    
            # loop from left to right same as the bubble
            # sort
            for i in range(start, end):
                if (self.list[i] > self.list[i + 1]):
                    self.list[i], self.list[i + 1] = self.list[i + 1], self.list[i]
                    swapped = True
                    self.speedUpCount += 1
                    if self.speedUpCount >= 20:
                        self.visualizer.run_self(self.list, i, i+1, self.speedUp, "Cocktail Sort", count)
                    else:
                        self.visualizer.run_self(self.list, i, i+1, False, "Cocktail Sort", count)
                    count += 1
    
            # if nothing moved, then array is sorted.
            if (swapped == False):
                break
    
            # otherwise, reset the swapped flag so that it
            # can be used in the next stage
            swapped = False
    
            # move the end point back by one, because
            # item at the end is in its rightful spot
            end = end-1
    
            # from right to left, doing the same
            # comparison as in the previous stage
            for i in range(end-1, start-1, -1):
                if (self.list[i] > self.list[i + 1]):
                    self.list[i], self.list[i + 1] = self.list[i + 1], self.list[i]
                    swapped = True
                    self.speedUpCount += 1
                    if self.speedUpCount >= 20:
                        self.visualizer.run_self(self.list, i, i+1, self.speedUp, "Cocktail Sort", count)
                    else:
                        self.visualizer.run_self(self.list, i, i+1, False, "Cocktail Sort", count)
                    count += 1
    
            # increase the starting point, because
            # the last stage would have moved the next
            # smallest number to its rightful spot.
            start = start + 1
        self.speedUpCount = 0
        return count