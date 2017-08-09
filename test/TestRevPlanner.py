import unittest
import os,sys,inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from revplanner import RevPlanner

class TestRevPlanner(unittest.TestCase):
	def testPlanRevNormalData(self):
		dailyRevs = [5, 20]
		ranks = [2, 4]
		rp = RevPlanner(dailyRevs, ranks)
		self.assertEqual(rp.planRev(), [25.0, 25.0, 20.0, 20.0])


	def testPlanRevOneRevOneRank(self):
		dailyRevs = [5]
		ranks = [1]
		rp = RevPlanner(dailyRevs, ranks)
		self.assertEqual(rp.planRev(), [5.0])

	def testPlanRevTwoRevSameRank(self):
		dailyRevs = [5, 20]
		ranks = [1, 1]
		rp = RevPlanner(dailyRevs, ranks)
		self.assertEqual(rp.planRev(), [25.0])


	def testPlanRevTwoRevOneZeroRank(self):
		dailyRevs = [5, 20]
		ranks = [1, 0]
		rp = RevPlanner(dailyRevs, ranks)
		self.assertEqual(rp.planRev(), [5.0])

	def testPlanRevTwoRevOneEmptyRank(self):
		dailyRevs = [5, 20]
		ranks = [1]
		rp = RevPlanner(dailyRevs, ranks)
		self.assertEqual(rp.planRev(), [5.0])

	def testPlanRevNormalDataBis(self):
		dailyRevs = [5, 20]
		ranks = [6, 2]
		rp = RevPlanner(dailyRevs, ranks)
		self.assertEqual(rp.planRev(), [25.0, 25.0, 5.0, 5.0, 5.0, 5.0])

	def testPlanRevExceptionEmptyDailyRevs(self):
		dailyRevs = []
		ranks = [1]

		with self.assertRaises(ValueError):
			rp = RevPlanner(dailyRevs, ranks)

	def testPlanRevExceptionEmptyRanks(self):
		dailyRevs = [5.0]
		ranks = []

		with self.assertRaises(ValueError):
			rp = RevPlanner(dailyRevs, ranks)


if __name__ == "__main__":
	unittest.main()
