#coding=utf-8
# pylint: skip-file
"""
Checks the first profile loading function
"""

import unittest
import os
from main import load_profile


class LoadProfileTest(unittest.TestCase):
    """
    Tests profile loading function
    """

    PATH_TO_LAB_FOLDER = os.path.dirname(os.path.abspath(__file__))
    PATH_TO_PROFILES_FOLDER = os.path.join(PATH_TO_LAB_FOLDER, 'profiles')

    def test_load_profile_ideal(self):
        """
        Ideal scenario
        """
        expected = {'name': 'en', 
                    'freq': {'place': 2, 'relation': 1, 'number': 1, 'gravity': 1, 
                             'directions': 1, 'distance': 1, 'as': 1, 'instead': 1, 
                             'waggle': 1, 'then': 1, 'on': 4, 'be': 1, 'further': 1, 
                             'which': 1, 'discoveries': 1, 'sisters': 2, 'vertical': 2, 
                             'inside': 2, 'remarkable': 3, 'however': 1, 'a': 2, 'home': 1, 
                             'danced': 1, 'for': 1, 'about': 2, 'hive': 4, 'tell': 2, 
                             'discover': 1, 'cannot': 1, 'point': 1, 'animal': 1, 
                             'outside': 2, 'how': 1, 'communicate': 1, 'behaviour': 1, 
                             'to': 10, 'platform': 1, 'would': 5, 'portion': 2, 'was': 2, 
                             'horizontal': 1, 'uses': 1, 'bees': 3, 'she': 2, 'frischs': 1, 
                             'so': 3, 'when': 2, 'in': 5, 'and': 4, 'sometimes': 2, 'food': 4, 
                             'inner': 1, 'run': 1, 'other': 1, 'method': 1, 'study': 1, 
                             'represented': 1, 'scout': 1, 'of': 12, 'their': 2, 'studying': 1, 
                             'find': 1, 'soon': 1, 'depending': 1, 'wall': 3, 'pointed': 1, 
                             'that': 2, 'this': 2, 'he': 1, 'fly': 1, 'generally': 1, 'also': 1, 
                             'first': 1, 'but': 1, 'off': 1, 'if': 2, 'line': 1, 'straight': 3, 
                             'example': 1, 'top': 1, 'fairly': 1, 'something': 1, 'decode': 2, 
                             'message': 1, 'direction': 4, 'easy': 1, 'came': 1, 'source': 2, 
                             'used': 1, 'dance': 5, 'they': 2, 'where': 1, 'dancer': 3, 
                             'have': 1, 'von': 3, 'different': 1, 'directly': 1, 'the': 38, 
                             'noted': 1, 'entrance': 1, 'by': 2, 'up': 1, 'same': 1, 'her': 1, 
                             'merely': 1, 'doing': 1, 'revolutionise': 1, 'means': 1, 'facts': 1, 
                             'runs': 1, 'left': 2, 'use': 1, 'feeding': 2, 'frisch': 2, 
                             'discovered': 1, 'is': 3, 'sun': 5}, 
                    'n_words': 117}

        path_to_profile = os.path.join(LoadProfileTest.PATH_TO_PROFILES_FOLDER, 'en.json')
        actual = load_profile(path_to_profile)
        self.assertEqual(expected, actual)

    def test_load_profile_bad_input(self):
        """
        Bad input scenario
        """
        expected = None

        path_to_profile = os.path.join(LoadProfileTest.PATH_TO_PROFILES_FOLDER, 'noneexistent.json')
        actual = load_profile(path_to_profile)
        self.assertEqual(expected, actual)

    def test_load_profile_bad_input_type(self):
        """
        Bad input scenario
        """
        expected = None

        path_to_profile = []
        actual = load_profile(path_to_profile)
        self.assertEqual(expected, actual)
