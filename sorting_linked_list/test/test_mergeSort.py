import pytest
import time

import sys
sys.path.append("..")

from src.ListNode import toListNode, ln2List
from src.merge_sort import mergeSort, sizeOfListNode

def compareAfterMergeSort(l):
    head = mergeSort(toListNode(l))
    assert ln2List(head) == sorted(l)

def compareSize(l):
    s = sizeOfListNode(toListNode(l))
    assert s == len(l)

def test_emptyList():
    compareAfterMergeSort([])

def test_oneElementList():
    compareAfterMergeSort([1])

def test_twoSortedElementList():
    compareAfterMergeSort([1,2])

def test_twoUnsortedElementList():
    compareAfterMergeSort([2,1])

def test_threeUnsortedElementList():
    compareAfterMergeSort([2,1,3])

def test_sizeOfEmptyList():
    compareSize([])

def test_sizeOfFullList():
    compareSize([1,2,3,4,5,6,7])