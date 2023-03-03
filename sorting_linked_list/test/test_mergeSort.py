import pytest
import time

import sys
sys.path.append("..")

from src.ListNode import toListNode, ln2List
from src.merge_sort import mergeSort

def compareAfterMergeSort(l):
    head = mergeSort(toListNode(l))
    assert ln2List(head) == sorted(l)

def test_emptyList():
    compareAfterMergeSort([])

def test_oneElementList():
    compareAfterMergeSort([1])

def test_twoSortedElementList():
    compareAfterMergeSort([1,2])