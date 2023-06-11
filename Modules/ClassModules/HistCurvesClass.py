import numpy as np
import pandas as pd
from DateModule import future_date as futureDate, months_between as monthsBetween  # Import the functions from your module

class HistCurvesClass:
    def __init__(self):
        self.firstDate = 0
        self.l_numCurves = 0
        self.curves = pd.DataFrame() 
        self.maturities = np.array([0.25, 0.5, 1.0, 2.0, 3.0, 5.0, 7.0, 10.0, 20.0, 30.0])

    def initialize(self, wkSheet):
        data = wkSheet.values[5:]
        self.firstDate = int(data[0, 0] * 100 + data[0, 1])
        self.l_numCurves = np.where(data[:, 4] > 0)[0][-1] + 1
        self.curves = pd.DataFrame(data[:self.l_numCurves, 3:13])

    @property
    def lastDate(self):
        return futureDate(self.firstDate, self.l_numCurves - 1)  # Use the imported function

    def histCurveRateByDate(self, year, month, maturityIndex):
        desiredDate = year * 100 + month
        index = 1 + monthsBetween(self.firstDate, desiredDate)  # Use the imported function
        return self.curves.loc[index, maturityIndex]

    def histCurveRateByIndex(self, curveIndex, maturityIndex):
        return self.curves.loc[curveIndex, maturityIndex]

    def bestFittingCurve(self, d_shortRate, d_midRate, d_longRate, l_fitMethod):
        d_weightShort = 40
        d_weightMid = 20
        d_weightLong = 40
        d_MinDiff = 1000000

        for l_YC_Counter in range(self.l_numCurves):
            d_histShortRate = self.curves.loc[l_YC_Counter, 2]
            d_histMidRate = self.curves.loc[l_YC_Counter, 6]
            d_histLongRate = self.curves.loc[l_YC_Counter, 8]

            d_Diff_S = d_shortRate - d_histShortRate
            d_Diff_M = d_midRate - d_histMidRate
            d_Diff_L = d_longRate - d_histLongRate

            if l_fitMethod == 1:  
                d_Diff_S = np.abs(d_Diff_S)
                d_Diff_M = np.abs(d_Diff_M)
                d_Diff_L = np.abs(d_Diff_L)
            else:
                d_Diff_S = d_Diff_S * d_Diff_S
                d_Diff_M = d_Diff_M * d_Diff_M
                d_Diff_L = d_Diff_L * d_Diff_L

            d_Diff_YC = d_weightShort * d_Diff_S + d_weightMid * d_Diff_M + d_weightLong * d_Diff_L

            if d_Diff_YC < d_MinDiff:
                d_MinDiff = d_Diff_YC
                l_Best_YC = l_YC_Counter

        return l_Best_YC
