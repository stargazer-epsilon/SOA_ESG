import math
import numpy as np

class EquityFundReturn:
    """This class stores the parameters for generating returns for a class of equities.
    It also stores the current state (volatility) of an equity class and provides
    a method to generate the return for the next period, given the current state
    and shocks to the return and its volatility.
    """

    def __init__(self, target_vol, current_vol, min_vol, max_vol_before, max_vol_after,
                 mean_rev_strength, vol_std_dev, a, b, c, SET_median_return, SET_volatility):
        self.target_vol = target_vol
        self.current_vol = current_vol
        self.min_vol = min_vol
        self.max_vol_before = max_vol_before
        self.max_vol_after = max_vol_after
        self.mean_rev_strength = mean_rev_strength
        self.vol_std_dev = vol_std_dev
        self.a = a
        self.b = b
        self.c = c
        self.SET_median_return = SET_median_return
        self.SET_volatility = SET_volatility

    def get_next_return(self, return_shock, vol_shock):
        """Calculate the next return based on the current volatility and shocks to the return and volatility."""
        curr_log_vol = math.log(self.current_vol)
        target_log_vol = math.log(self.target_vol)

        # First update the volatility
        curr_log_vol = (1 - self.mean_rev_strength) * curr_log_vol + (self.mean_rev_strength * target_log_vol)
        self.current_vol = math.exp(curr_log_vol)
        self.current_vol = min(self.max_vol_before, self.current_vol)
        curr_log_vol = math.log(self.current_vol)

        curr_log_vol = curr_log_vol + vol_shock * self.vol_std_dev
        self.current_vol = math.exp(curr_log_vol)
        self.current_vol = min(self.max_vol_after, self.current_vol)
        self.current_vol = max(self.min_vol, self.current_vol)

        # Next compute the log return based on the volatility and shock
        next_mean_return = self.a + self.b * self.current_vol + self.c * self.current_vol * self.current_vol
        next_return = (next_mean_return / 12) + return_shock * (self.current_vol / (12 ** 0.5))

        return math.exp(next_return) - 1

    def get_next_return_SET(self, return_shock):
        """Calculate the next return based on the SET median return and return shock."""
        return ((1 + self.SET_median_return) ** (1 / 12) - 1) + return_shock * (self.SET_volatility / (12 ** 0.5))


# All public properties of the original VBA class have been converted to attributes of the Python class, which are set in the __init__ method.
# All function procedures have been converted to methods of the Python class.
# VBA's Application.WorksheetFunction.min() and Application.WorksheetFunction.max() functions have been replaced with Python's built-in min() and max() functions.
# The Log() and Exp() functions have been replaced with math.log() and math.exp(), respectively.