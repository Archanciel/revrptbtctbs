import unittest
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from gainparser import BtcTbsGainParser

class TestBtcTbsGainParser(unittest.TestCase):        
    def setUp(self):
        self.gainData = "107/08/2017 03:005.50#13444014416-> Profit, 2.50% of 220.00 deposited [31/60]207/08/2017 03:0010.83#13444013925-> Profit, 2.50% of 433.00 deposited [33/60]307/08/2017 03:002.55#13444013099-> Profit, 2.50% of 102.00 deposited [35/60]407/08/2017 03:002.85#13444012708-> Profit, 2.50% of 114.00 deposited [36/60]507/08/2017 03:003.65#13444012418-> Profit, 2.50% of 146.00 deposited [37/60]607/08/2017 03:003.63#13444011590-> Profit, 2.50% of 145.00 deposited [39/60]707/08/2017 03:003.05#13444010889-> Profit, 2.50% of 122.00 deposited [41/60]807/08/2017 03:003.08#13444010355-> Profit, 2.50% of 123.00 deposited [42/60]907/08/2017 03:003.35#1344409712-> Profit, 2.50% of 134.00 deposited [44/60]1007/08/2017 03:006.45#1344409081-> Profit, 2.50% of 258.00 deposited [46/60]1107/08/2017 03:002.50#1344407046-> Profit, 2.50% of 100.00 deposited [53/60]"
        self.parser = BtcTbsGainParser(self.gainData)
        
    def testGetDailyRevs(self):
        res = self.parser.getDailyRevs()
        self.assertEqual("['5.50', '10.83', '2.55', '2.85', '3.65', '3.63', '3.05', '3.08', '3.35', '6.45', '2.50']", str(res))
  
    def testGetRemainingRevPeriods(self):
       res = self.parser.getRemainingRevPeriods()
       self.assertEqual("[('31', '60'), ('33', '60'), ('35', '60'), ('36', '60'), ('37', '60'), ('39', '60'), ('41', '60'), ('42', '60'), ('44', '60'), ('46', '60'), ('53', '60')]", str(res))
    
    def testGetInvestments(self):
       res = self.parser.getInvestments()
       self.assertEqual("['220.00', '433.00', '102.00', '114.00', '146.00', '145.00', '122.00', '123.00', '134.00', '258.00', '100.00']", str(res))

    def testGetDate(self):
       res = self.parser.getDate()
       self.assertEqual("07/08/2017", res)

if __name__ == "__main__":
    unittest.main()