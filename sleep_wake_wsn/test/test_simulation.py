"""
The tests for the simulator module and the functions therein go here
"""
import sys
sys.path.append('..')

import src.simulator as simulator
import unittest


class TestSimulator(unittest.TestCase):

    def test_get_arguments(self):
        """
        Ensures argument values are available in parsed arguments
        :return:
        """
        arguments = simulator._get_arguments(['7', '50', 'tqsaa'])
        self.assertEqual(arguments.num_rows, 7)
        self.assertEqual(arguments.num_cols, 50)
        self.assertEqual(arguments.scheduling_strategy, 'tqsaa')