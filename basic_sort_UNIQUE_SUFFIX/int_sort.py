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
import psutil


def cpu_time(func, data):

    process = psutil.Process()
    start_time = process.cpu_times().user

    result = func(data)

    end_time = process.cpu_times().user
    total_time = end_time - start_time
    print(total_time)
    return result, total_time


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
    qsort docstring
    """

    # TODO: implement quick sort
    return sorted(int_list)


def insertion(int_list):
    """
    insertion docstring
    """
    # TODO: implement insertion sort
    return sorted(int_list)
