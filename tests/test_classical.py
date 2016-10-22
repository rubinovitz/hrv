# coding: utf-8
import unittest

import numpy as np

from hrv.classical import time_domain
from tests.test_utils import FAKE_RRI


class ClassicalIndexesTestCase(unittest.TestCase):

    def test_right_function_call(self):
        response = time_domain(FAKE_RRI)
        expected = {'rmssd': 38.07,
                    'sdnn': 41.93,
                    'nn50': 1,
                    'pnn50': 0.33,
                    'mrri':  793.75,
                    'mhr': 75.67}
        np.testing.assert_almost_equal(sorted(response.values()),
                                       sorted(expected.values()),
                                       decimal=2)
