import random
from visualizer import Visualizer
import time

class Sorters():

    def __init__(self, list, sorted, seeSort):
        self.seeSort = seeSort
        self.list = list
        self.sorted = sorted
        self.visualizer = Visualizer()

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
        time.sleep(.05)
        self.visualizer.run_self(new_list)
        return new_list, count

    def pancake_sort(self, count):
        random.shuffle(self.list)
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

        random.shuffle(self.list)
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
                    count += 1
                    time.sleep(.05)
                    self.visualizer.run_self(self.list)
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
        random.shuffle(self.list)

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
            time.sleep(.05)
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

        random.shuffle(self.list)
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
        random.shuffle(self.list)
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
                    count += 1
                    time.sleep(.05)
                    self.visualizer.run_self(self.list)
                    if self.seeSort:
                        if swapValue:
                            print(self.list, f"\033[91mVALUES SWAPPED\033[0m: \033[91m[{self.list[i+1], self.list[i]}]\033[0m \033[95mITERATION\033[0m: \033[92m{count}\033[0m")
                        else:
                            print(self.list, f"\033[92mVALUES CHECKED\033[0m: \033[92m[{self.list[i+1], self.list[i]}]\033[0m \033[95mITERATION\033[0m: \033[92m{count}\033[0m")         
        return count

    def shell_sort(self):
        shellIntervals = [4, 2, 1]

    def heap_sort(self):
        pass

    def selection_sort(self, count):

        random.shuffle(self.list)

        current_number = ''
        index = 0
        while self.list != self.sorted:
            for i in range(0, len(self.list)-index):
                if current_number == '':
                    current_number = self.list[i]
                if self.list[i] < current_number:
                    current_number = self.list[i]
                count += 1
            indexOfI = self.list.index(current_number)
            self.list.pop(indexOfI)
            self.list.append(current_number)
            current_number = ''
            index += 1
            time.sleep(.05)
            self.visualizer.run_self(self.list)
            if self.seeSort:
                print(f"FOUND {current_number} IN INDEX {indexOfI} OF {self.list}")
        if self.seeSort:
            print(f"SORTED LIST: {self.list}")
        return count