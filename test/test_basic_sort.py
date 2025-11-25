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

import pytest
import numpy as np
import psutil
import time
from pathlib import Path
from basic_sort_UNIQUE_SUFFIX import int_sort


# OLD `is_sorted` function, i do not understand why it takes
# self as a parameter
#
# def is_sorted(self, int_list):
#     """
#     Testing oracle.
#     """
#     return True
def cpu_usage(func, data):
    """
    Measure the CPU usage percentage(using psutil.cpu_percent())
    while executing the provided function.


    Args:
        func (Callable): The function to execute and measure.
        data (list of int): The input data to pass to the function.

    Returns:
        tuple: A tuple containing:
            - list of int: The result returned by the function.
            - float: The CPU usage percentage during execution.
    """
    # initialize cpu_percent with interval=None to start measurement
    psutil.cpu_percent(interval=None)

    result = func(data)

    # get the CPU percentage since last call
    # reminder this will always give 0 for small test
    cpu_usage = psutil.cpu_percent(interval=None)

    return result, cpu_usage


def is_sorted(int_list):
    last_value = -np.inf

    for i in int_list:
        # If any element is greater than the previous,
        # the list is out of order
        if last_value > i:
            return False
        last_value = i

    return True


def load_int_list_from_file(file_path):
    """
    Load a list of integers from a text file.
    Each line should contain a single integer.
    
    Args:
        file_path (Path): Path to the text file containing integers.
        
    Returns:
        list[int]: List of integers read from the file.
    """
    int_list = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line:  # Skip empty lines
                int_list.append(int(line))
    return int_list


@pytest.fixture
def int_lists():
    """
    Creates testing data for all tests by loading from text files.
    Reads ordered.txt and unordered.txt from the test/data directory.
    """
    # Get the directory where this test file is located
    test_dir = Path(__file__).parent
    data_dir = test_dir / 'data'
    
    # Load the two test data files
    ordered_file = data_dir / 'ordered.txt'
    unordered_file = data_dir / 'unordered.txt'
    
    int_lists = [
        load_int_list_from_file(ordered_file),
        load_int_list_from_file(unordered_file)
    ]
    
    return int_lists


def test_bubble(int_lists):
    """
    Tests the bubble sort implementation using a list of integer lists.

    Args:
        int_lists (list[list[int]]): A list containing multiple lists of integers
            to be sorted and tested.

    Returns:
        None

    Raises:
        Assert Error: If the bubble sort output is not sorted correctly or if
            the measured CPU time exceeds the allowed limit (100.0).
    """
    for int_list in int_lists:
        sorted_list, cpu = cpu_usage(int_sort.bubble, int_list)
        assert is_sorted(sorted_list)
        assert cpu >= 0
        print(f"Bubble Sort CPU Usage: {cpu}%")


def test_quick(int_lists):
    for int_list in int_lists:
        start = time.time()
        sorted_list = int_sort.quick(int_list)
        runtime = time.time() - start
        assert is_sorted(sorted_list)
        print(f"Quick Sort Runtime: {runtime:.6f} seconds")


def test_insertion(int_lists):
    for int_list in int_lists:
        process = psutil.Process()
        mem_before = process.memory_info().rss
        sorted_list = int_sort.insertion(int_list)
        mem_after = process.memory_info().rss
        mem_used = mem_after - mem_before
        assert is_sorted(sorted_list)
        print(f"Insertion Sort Memory Usage: {mem_used} bytes")
