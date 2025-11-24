# =========================================================================
#
#  Copyright Ziv Yaniv
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================

"""
This module sorts lists of integers...
"""
import time
import psutil


def cpu_time(func, data):

    process = psutil.Process()
    start_time = process.cpu_times().user

    result = func(data)

    end_time = process.cpu_times().user
    total_time = end_time - start_time
    print(total_time)
    return result, total_time


def mem_usage(data):
    """
    Tests the amount of memory used from the insertion sort

    Args:
        Data: a dataset of numbers to sort

    Returns:
        memUsed: The amount of memory used in this instance
                    calculated by finding the difference before and after
                    running
    """

    # Grabbing percent of memory used before running the sort
    memBefore = psutil.virtual_memory().used

    insertion(data)

    # Grabbing percent of memory used after running the sort
    memAfter = psutil.virtual_memory().used

    # Calculating used memory by finding the difference between
    # before and after
    memUsed = memAfter - memBefore

    print(f"Amount of memory used: {memUsed}")
    return memUsed


def runtime(data):
    """
    Tests the runtime of the quicksort

    Args:
        data: a dataset of numbers

    Returns:
        runtime: the runtime of quicksort

    """

    starttime = time.time()
    quick(data)
    endtime = time.time()
    runtime = (endtime - starttime) * 1000
    print(f"runtime:  {runtime:.4f} milliseconds")
    return runtime


# I used Google Style Docstring
def bubble(int_list):
    """
    Sorts a list of numbers in ascending order using bubble sort.

    Args:
        int_list (list of int or float): The list to be sorted.

    Returns:
        list: A new list containing the sorted elements.
    """
    n = len(int_list)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if int_list[j] > int_list[j + 1]:
                int_list[j], int_list[j + 1] = int_list[j + 1], int_list[j]
                swapped = True
        # This if statment is only for if the stament is already sorted.
        if not swapped:
            break
    # Print("bubble sort") Do we need this
    return int_list


data = [2, 3, 4, 10, 45, 69, 5, 6]
cpu_time(bubble, data)


def quick(int_list):
    """
    Sorts a list of numbers from smallest to largest using quick Sort

    Args:
        int_list: List of ints or floats unsorted

    Returns:
        int_list: list of previously provided numbers
                    now sorted through quick sort
    """

    if len(int_list) <= 1:
        return int_list
    else:
        pivot = int_list[len(int_list) // 2]
        less = [x for x in int_list if x < pivot]
        equal = [x for x in int_list if x == pivot]
        greater = [x for x in int_list if x > pivot]
        return quick(less) + equal + quick(greater)


runtime(data)


# Used Google Docstring format
def insertion(int_list):
    """
    Sorts a list of numbers from smallest to largest using Insertion Sort

    Args:
        int_list: List of ints or floats unsorted

    Returns:
        sorted_list: list of previously provided numbers
                        now sorted through insertion sort
    """

    # Making a deep copy of list to avoid changing original
    sorted_list = int_list.copy()

    for i in range(1, len(sorted_list)):

        current = sorted_list[i]
        j = i - 1

        # Shift right
        while j >= 0 and sorted_list[j] > current:
            sorted_list[j + 1] = sorted_list[j]
            j -= 1

        sorted_list[j + 1] = current

    return sorted_list


mem_usage(data)
