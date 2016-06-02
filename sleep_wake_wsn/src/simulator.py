"""
The Simulator module which coordinates the run of the Sleep Wake experiment and produces results.
It assumes the use of a Rectangular field made of num_rows(M) x num_cols(N) cells each having one sensor and
a single intruder maneuvering across the field moving from one cell to another in one time step. The central
controller makes an assignment of sleep wake time units to each of the M x N sensors at each time step. At time t_i,
a sensor is either asleep (its remaining sleep time r_i being > 0 units) or awake (remaining sleep time r_i = 0 units).
If r_i > 0, any new sleep time assignment by the controller is ignored, else r_i is set to the new r_i and the sensor
starts sleeping for r_i time units. If r_i = 0 when the intruder is at the cell of sensor i, then the intruder
is detected, else it goes undetected. The Goal of the intruder is to escape detection while the Goal of the controller
is to detect the intruder maximum number of times while keeping the minimum number of sensors awake, thereby saving
maximum energy
"""

import time
import sys
import settings as s
from field import Field
from agent import Agent
from controller import Controller
import argparse


class Simulation(object):

    def __init__(self, parsed_arguments):
        self.field = Field(parsed_arguments)
        self.controller = Controller(parsed_arguments)
        self.agent = Agent(parsed_arguments)


def _get_arguments(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('num_rows', choices=range(s.min_dimension, s.max_dimension),
                        help='The number of rows in the 2-D grid of sensor cells', type=int)
    parser.add_argument('num_cols', choices=range(s.min_dimension, s.max_dimension),
                        help='The number of columns in the 2-D grid of sensor cells', type=int)
    parser.add_argument('scheduling_strategy', choices=s.supported_sleep_wake_strategies,
                        help='The Algorithm to be used for Sleep Wake scheduling', type=str)
    parser.add_argument('maneuvering_strategy', choices=s.supported_maneuvering_strategies,
                        help='The Strategy followed by the agent to move from one cell to another')
    parser.add_argument('time_limit', help='Number of Time steps to run the simulation',
                        choices=range(s.min_time_units, s.max_time_units), type=int)
    return parser.parse_args(args)


def run_simulation():
    parsed_args = _get_arguments(sys.argv[1:])
    simulation = Simulation(parsed_args)
    simulation.start()


if __name__ == '__main__':
    run_simulation()