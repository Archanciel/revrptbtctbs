from unittest import TestLoader, TextTestRunner, TestSuite 

from testbtctbsgainparser import TestBtcTbsGainParser
from testrevplanner import TestRevPlanner

if __name__ == "__main__":
    loader = TestLoader() 
    suite = TestSuite((loader.loadTestsFromTestCase(TestBtcTbsGainParser), 
    	                  loader.loadTestsFromTestCase(TestRevPlanner),
    	                  ))
    runner = TextTestRunner(verbosity = 2) 
    runner.run(suite)