from bloomdata.helper_functions import random_phrase
import pytest


def test_random_phrase_string():
    list1 = ['Ryan']
    list2 = ['Allred']
    assert type(random_phrase(list1, list2)) == str


def test_random_phrase_small_lists():
    list1 = ['Ryan']
    list2 = ['Allred']
    assert random_phrase(list1, list2) == 'Ryan Allred'


def test_random_phrase_medium_lists():
    list1 = ['Ryan', 'Austen']
    list2 = ['Allred', 'Lee']
    assert random_phrase(list1, list2) in [
        'Ryan Lee', 'Ryan Allred', 'Austen Allred', 'Austin Lee']


def test_random_phrase_int():
    list1 = [1, 2]
    list2 = [3, 4]
    assert random_phrase(list1, list2) in ['1 4', '1 3', '2 3', '2 4']
