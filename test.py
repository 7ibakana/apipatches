import bitcoin
import unittest
from unittest.mock import patch
from unittest import patch

class Test(Testcase):
    @patch('bitcoin.requestRate')
    def testConvert(self, mockRate):
        mockRateFloat = 1111.11
        exampleApiResponse = {'bpi': 'USD', 'rateFloat': mockRateFloat}
        mockRateSideEffect = [exampleApiResponse]
        converted = bitcoin.convert(100, mockRateFloat)
        self.assertEqual(111111, converted)
if __name__ =='__main__':
    unittest.main()
