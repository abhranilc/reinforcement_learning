import numpy as np

class Field(object):

    def __init__(self, parsed_arguments):
        self.num_rows = parsed_arguments.num_rows
        self.num_cols = parsed_arguments.num_cols
        self.sensors = np.ones(self.num_rows, self.num_cols)

