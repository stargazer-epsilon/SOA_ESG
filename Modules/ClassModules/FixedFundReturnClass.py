from YieldCurveClass import YieldCurveClass

class FixedFundReturnClass:
    def __init__(self):
        self.maturity = None       # maturity in years for bonds in this fund
        self.monthlyFactor = None  # usually 1/12 = 0.0833333
        self.monthlySpread = None
        self.duration = None       # measured in years
        self.volatility = None     # volatility due to credit spreads

    def get_next_return(self, prevYldCurve: YieldCurveClass, currYldCurve: YieldCurveClass, shock: float) -> float:
        prevIntRate = prevYldCurve.rateAtMaturity(self.maturity)
        currIntRate = currYldCurve.rateAtMaturity(self.maturity)

        currReturn = self.monthlyFactor * (prevIntRate + self.monthlySpread) + self.duration * (prevIntRate - currIntRate) + shock * (prevIntRate ** 0.5) * self.volatility

        return currReturn