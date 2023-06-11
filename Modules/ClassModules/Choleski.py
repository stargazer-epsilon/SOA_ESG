import numpy as np
from math import sqrt

class CorrelationMatrix:
    """
    This class uses the Choleski factorization method to
    determine a matrix mA such that mA*transpose(mA) = mCorr,
    where mCorr is a correlation matrix.
    The matrix mA can then be multiplied by an array of
    uncorrelated random numbers U to get an array of
    correlated random numbers C as in mA * U = C.
    The columns of U and C represent trials or observations (or time periods)
    and each row represents a sequence of trials for one variable
    of a set of variables, where the variables are either
    correlated or uncorrelated. The rows or C will be
    correlated to the degree specified by mCorr.
    """
    def __init__(self):
        self.num_vars = 0
        self.num_obs = 0
        self.mCorr = np.array([])
        self.mA = np.array([])
        self.mRandom = np.array([])
        self.mCorrelated = np.array([])

    def setup(self, nVars, nObs, correlations):
        """
        This function initializes the size of the matrices and specifies correlations.
        Then generate uncorrelated random numbers to fill the matrix mRandom.
        """
        self.num_vars = nVars
        self.num_obs = nObs
        self.mRandom = np.zeros((nVars, nObs))
        self.mCorrelated = np.zeros((nVars, nObs))
        self.mCorr = np.array(correlations)
        self.mA = np.zeros((nVars, nVars))

        self.calc_conversion_matrix()

    def calc_conversion_matrix(self):
        """
        Performs Choleski factorization of mCorr to get mA.
        """
        self.mA[0][0] = sqrt(self.mCorr[0][0])

        for i in range(1, self.num_vars):
            for j in range(i):
                self.mA[i][j] = self.mCorr[i][j]
                for k in range(j):
                    self.mA[i][j] -= self.mA[i][k] * self.mA[j][k]
                self.mA[i][j] /= self.mA[j][j]

            self.mA[i][i] = self.mCorr[i][i]
            for k in range(i):
                self.mA[i][i] -= self.mA[i][k] * self.mA[i][k]
            self.mA[i][i] = sqrt(self.mA[i][i])

    def correlate(self):
        """
        Multiplies the factored correlation matrix by the uncorrelated random number array.
        """
        self.mCorrelated = np.matmul(self.mA, self.mRandom)

    @property
    def randNum(self):
        """
        Getter for mRandom matrix.
        """
        return self.mRandom

    @randNum.setter
    def randNum(self, row_col_num):
        """
        Setter for mRandom matrix.
        """
        row, col, num = row_col_num
        self.mRandom[row][col] = num

    @property
    def corrNum(self):
        """
        Getter for mCorrelated matrix.
        """
        return self.mCorrelated

    # Uncomment the following to print the conversion matrix
    # def show_conversion_matrix(self):
    #     print(self.mA)

# In this python class:

# The input uncorrelated random matrix U is referred to as mRandom and the output correlated random matrix C as mCorrelated.
# The functions randNum and corrNum are replaced by @property decorators and their corresponding setters in Python, allowing you to get and set the values in the same way you would access an attribute.
# setup function is called in the constructor __init__.
# The 'correlations' parameter should be a nested list or a numpy array.
# The VBA For loop is replaced by Python's range function.
# VBA 2D arrays are replaced by 2D numpy arrays, with element-wise operations available by default.
# The correlate function uses numpy's matmul function to multiply two matrices.
# Python indexes from 0, so the indices in loops have been adjusted accordingly.
# Note: This python class assumes numpy library is used for array manipulations, which is the standard in scientific Python and is far more efficient than using nested lists.