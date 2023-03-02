import pytest

import sys
sys.path.append("..")

from src.ListNode import toListNode, ln2List

def test_fullListConversion():
    l = [1,2,3,4]
    assert ln2List(toListNode(l)) == l

def test_oneElementListConversion():
    l = [1]
    assert ln2List(toListNode(l)) == l

def test_emptyListConversion():
    l = []
    assert ln2List(toListNode(l)) == l