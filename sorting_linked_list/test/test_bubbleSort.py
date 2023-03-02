import pytest

import sys
sys.path.append("..")

from src.ListNode import toListNode, ln2List
from src.bubble_sort import bubbleSort

def compareAfterBubbleSort(l):
    head = bubbleSort(toListNode(l))
    assert ln2List(head) == sorted(l)

def test_emptyList():
    compareAfterBubbleSort([])

def test_oneElementList():
    compareAfterBubbleSort([1])

def test_twoSortedElementList():
    compareAfterBubbleSort([1,2])

def test_twoUnsortedElementList():
    compareAfterBubbleSort([2,1])

def test_threeSingleUnsortedElementList():
    compareAfterBubbleSort([2,1,3])