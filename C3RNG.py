# To use this class, create an instance then call its methods.
# rng = C3RNG()
# rng.reseed(123)
# print(rng.get_next())

class C3RNG:

    # Constants used in generation
    _cm1 = 259200
    _cia1 = 7141
    _cic1 = 54773
    _crm1 = 0.0000038580247
    _cm2 = 134456
    _cia2 = 8121
    _cic2 = 28411
    _crm2 = 0.0000074373773
    _cm3 = 243000
    _cia3 = 4561
    _cic3 = 51349

    def __init__(self):
        self._mStateArray = [0.0]*97
        self._mIX1 = self._mIX2 = self._mIX3 = 0
        self._mbInitialized = False
        self._mCurrentSeed = 0

    def reseed(self, nSeed):
        self._mIX1 = self._cic1 - nSeed
        self._mIX1 = (self._cia1 * self._mIX1 + self._cic1) % self._cm1
        self._mIX2 = self._mIX1 % self._cm2
        self._mIX1 = (self._cia1 * self._mIX1 + self._cic1) % self._cm1
        self._mIX3 = self._mIX1 % self._cm3
        for j in range(97):
            self._mIX1 = (self._cia1 * self._mIX1 + self._cic1) % self._cm1
            self._mIX2 = (self._cia2 * self._mIX2 + self._cic2) % self._cm2
            self._mStateArray[j] = (self._mIX1 + self._mIX2 * self._crm2) * self._crm1

        self._mCurrentSeed = nSeed
        self._mbInitialized = True

    def get_next(self):
        if not self._mbInitialized:
            raise Exception('The random number generator was called without being seeded.')

        self._mIX1 = (self._cia1 * self._mIX1 + self._cic1) % self._cm1
        self._mIX2 = (self._cia2 * self._mIX2 + self._cic2) % self._cm2
        self._mIX3 = (self._cia3 * self._mIX3 + self._cic3) % self._cm3
        j = int(1 + (97 * self._mIX3) / self._cm3)
        u = (self._mIX1 + self._mIX2 * self._crm2) * self._crm1
        if u <= 0 or u >= 1:
            u = 1 + int(u) - u
        self._mStateArray[j] = u
        return self._mStateArray[j]
