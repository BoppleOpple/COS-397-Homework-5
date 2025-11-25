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
        sorted_list, cpu_time = int_sort.cpu_time(int_sort.bubble, int_list)
        assert is_sorted(sorted_list)
        assert cpu_time >= 0


def test_quick(int_lists):
    for int_list in int_lists:
        runtime_ms = int_sort.runtime(int_list)
        sorted_list = int_sort.quick(int_list)
        assert is_sorted(sorted_list)


def test_insertion(int_lists):
    for int_list in int_lists:
        mem_used = int_sort.mem_usage(int_list)
        sorted_list = int_sort.insertion(int_list)
        assert is_sorted(sorted_list)
