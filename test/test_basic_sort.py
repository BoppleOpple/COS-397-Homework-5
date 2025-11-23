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
from basic_sort_UNIQUE_SUFFIX import int_sort


# OLD `is_sorted` function, i do not understand why it takes
# self as a parameter
#
# def is_sorted(self, int_list):
#     """
#     Testing oracle.
#     """
#     return True
def cpu_time(func, data):
    """
    Measure the CPU usage percentage(using psutil.cpu_percent()) while executing the provided function.


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


@pytest.fixture
def int_lists():
    # fixture which creates testing data for all tests
    return [
        [3, 2, 1],
        [1, 1, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        np.random.randint(low=-10, high=200, size=5),
    ]


def test_bubble(int_lists):

    for int_list in int_lists:
        sorted_list, cpu = cpu_time(int_sort.bubble, int_list)
        assert is_sorted(sorted_list)
        # using the cpu somehow
        assert cpu <= 100.0


def test_quick(int_lists):
    assert True


def test_insertion(int_lists):
    assert True
