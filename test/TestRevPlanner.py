import unittest
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from RevPlanner import RevPlanner

class TestRevPlanner(unittest.TestCase):
    def testPlanRevNormalData(self):
        dailyRevs = [5, 20]
        investments = []
        ranks = [2, 3]
        rp = RevPlanner(dailyRevs, investments, ranks)
        self.assertEqual(rp.planRev(), [25.0, 25.0, 20.0])

if __name__ == "__main__":
    unittest.main()
