import numpy as np

from simple_functions.constants import my_pi


class TestPi(object):
    '''Class to test our constants are computed correctly'''

    def test_pi(self):
        '''Test computation of pi'''
        my_pi_res = my_pi(2)
        assert np.isclose(my_pi_res, np.pi, atol=1e-12)
