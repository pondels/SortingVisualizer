import random
from visualizer import Visualizer
import time

class Sorters():

    def __init__(self, list, sorted, seeSort):
        self.seeSort = seeSort
        self.list = list
        self.sorted = sorted
        self.visualizer = Visualizer()

    def randomize(self):
        random.shuffle(self.list)

    def time_value(self):
        pass
    #     length = len(self.list)
    #     if length < 5:
    #         time.sleep(.5)
    #     elif 5 < length <= 15:
    #         time.sleep(.15)
    #     elif 15 < length <= 30:
    #         time.sleep(.075)
    #     elif 30 < length <= 50:
    #         time.sleep(.025)
    #     else:
    #         time.sleep(.025)

    def flip(self, list, smallest_num, ignoreNums, count, seeSort):
        indexOfI = list.index(smallest_num)
        back_list = list[indexOfI:]
        back_list.reverse()
        count += 1
        front_list = list[:indexOfI]
        new_list = front_list + back_list
        first_values, new_list = new_list[:len(list) - ignoreNums], new_list[len(list) - ignoreNums:]
        if seeSort:
            print(first_values + new_list)
        new_list.reverse()
        count += 1
        new_list = first_values + new_list
        self.time_value()
        self.visualizer.run_self(new_list, smallest_num, -1)
        return new_list, count

    def pancake_sort(self, count):
        backup_list = [i for i in self.list]
        sorted_list = [i for i in self.list]
        sorted_list.sort()
        while self.list != sorted_list:
            smallest_num = min(backup_list)
            self.list, count = self.flip(self.list, smallest_num, len(backup_list), count, self.seeSort)
            if self.seeSort:
                print(self.list)
            backup_list.pop(backup_list.index(smallest_num))
        return count

    def radix_sort(self, count):

        max_length = len(str(max(self.list)))
        items = 0

        for n in range(1, max_length + 1):
            for num in range(10):
                for i in range(len(self.list)):
                    intValue = len(str(self.list[i])) - n
                    indexOfI = self.list.index(self.list[i])
                    currentValue = self.list[indexOfI]
                    if intValue > -1:
                        checkValue = int(str(self.list[i])[intValue])
                    else:
                        checkValue = 0
                    if checkValue == num:
                        self.list.pop(indexOfI)
                        self.list.insert(items, currentValue)
                        items += 1
                        self.time_value()
                        self.visualizer.run_self(self.list, indexOfI, intValue)
                    count += 1
                    if self.seeSort:
                        print(self.list)
                if self.sorted == self.list:
                    break
            items = 0
        return count

    def merge_sort(self):
        pass

    def quick_sort(self):
        pass

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
            self.list[j + 1] = num
            self.time_value()
            self.visualizer.run_self(self.list)

        return count

    def checkForCorrectBogo(self, list):
        totalAmount = 0
        for i in range(len(list)):
            if self.sorted[i] == list[i]:
                totalAmount += 1
        return totalAmount

    def bogo_sort(self, count):
        totalBogo = [[] for _ in range(len(self.list) + 1)]

        while self.list != self.sorted:
            count += 1
            random.shuffle(self.list)

            amount = self.checkForCorrectBogo(self.list)
            totalBogo[amount].append("")
            self.visualizer.run_self(self.list)

        if self.seeSort:
            totalLoops = -1
            for i in totalBogo:
                totalLoops += 1
                print(f"\033[95mThere were a total of \033[92m{len(i)}\033[95m iterations that had \033[92m{totalLoops} \033[95mnumber(s) \033[92mcorrect.\033[0m")
        return count

    def bubble_sort(self, count):

        swapValue = False
        while self.list != self.sorted:
            for i in range(len(self.list)):
                if i + 1 == len(self.list):
                    break
                else:
                    first_value, second_value = self.list[i], self.list[i + 1]
                    if first_value > second_value:
                        self.list[i+1], self.list[i] = self.list[i], self.list[i + 1]
                        swapValue = True
                    else:
                        swapValue = False
                    self.time_value()
                    self.visualizer.run_self(self.list, self.list.index(first_value), self.list.index(second_value))
                    count += 1
                    if self.seeSort:
                        if swapValue:
                            print(self.list, f"\033[91mVALUES SWAPPED\033[0m: \033[91m[{self.list[i+1], self.list[i]}]\033[0m \033[95mITERATION\033[0m: \033[92m{count}\033[0m")
                        else:
                            print(self.list, f"\033[92mVALUES CHECKED\033[0m: \033[92m[{self.list[i+1], self.list[i]}]\033[0m \033[95mITERATION\033[0m: \033[92m{count}\033[0m")         
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

                i += 1
                j += 1
            
                # now, we look back from ith index to the left
                # we swap the values which are not in the right order.
                k = i
                while k - gap > -1:
    
                    if self.list[k - gap] > self.list[k]:
                        self.list[k-gap],self.list[k] = self.list[k],self.list[k-gap]
                    k -= 1
                    count += 1
                self.time_value()
                self.visualizer.run_self(self.list)
            gap //= 2
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
            self.time_value()
            self.visualizer.run_self(self.list, index, index+1)
        return count

    def heap_sort(self):
        pass

    def selection_sort(self, count):

        current_number = ''
        index = 0
        while self.list != self.sorted:
            for i in range(0, len(self.list)-index):
                if current_number == '':
                    current_number = self.list[i]
                if self.list[i] < current_number:
                    current_number = self.list[i]
                count += 1
                self.time_value()
                self.visualizer.run_self(self.list, self.list.index(current_number), i)
            indexOfI = self.list.index(current_number)
            self.list.pop(indexOfI)
            self.list.append(current_number)
            self.time_value()
            self.visualizer.run_self(self.list, self.list.index(current_number), -1)
            current_number = ''
            index += 1
            if self.seeSort:
                print(f"FOUND {current_number} IN INDEX {indexOfI} OF {self.list}")
        if self.seeSort:
            print(f"SORTED LIST: {self.list}")
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
                    self.time_value()
                    self.visualizer.run_self(self.list, i, i+1)
                    
            for i in range(0, n-1, 2):
                if self.list[i] > self.list[i+1]:
                    self.list[i], self.list[i+1] = self.list[i+1], self.list[i]
                    isSorted = 0
                    count += 1
                    self.time_value()
                    self.visualizer.run_self(self.list, i, i+1)
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
            self.time_value()
            self.visualizer.run_self(self.list)
    
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
                    self.time_value()
                    self.visualizer.run_self(self.list, i, i+1)
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
                    self.time_value()
                    self.visualizer.run_self(self.list, i, i+1)
                    count += 1
    
            # increase the starting point, because
            # the last stage would have moved the next
            # smallest number to its rightful spot.
            start = start + 1
        return count