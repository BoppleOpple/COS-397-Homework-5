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
        if (last_value > i): return False
        last_value = i
    
    return True

@pytest.fixture
def int_lists():
    # fixture which creates testing data for all tests
    return [[3,2,1],
            [1,1,1],
            np.random.randint(low=-10, high=200, size=5)]

def test_bubble(int_lists):
    for int_list in int_lists:
        sorted_list = int_sort.bubble(int_list)
        assert is_sorted(sorted_list)
    assert True

def test_quick(int_lists):
    assert True

def test_insertion(int_lists):
    assert True
