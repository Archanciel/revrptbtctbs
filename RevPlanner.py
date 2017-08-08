"""
The MIT License (MIT)

Copyright (c) <year> <copyright holders>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
class RevPlanner:
    def __init__(self, dailyRevs, investments, ranks):
        self.dailyRevs = dailyRevs
        self.investments = investments
        self.ranks = ranks

    def planRev(self):
        revSpreadOverPeriods = []
        currentRevs = []
        
        for rev, rank in zip(self.dailyRevs, self.ranks):
             print("%.2f - %d" % (rev, rank))
             for i in range(rank):
                 currentRevs.append(rev)
             revSpreadOverPeriods.append(currentRevs)
             currentRevs = []
         
        print('revSpreadOverPeriods')    
        print(revSpreadOverPeriods)
        
        revByPeriod = self._aggregateRevByPeriod(revSpreadOverPeriods)

        return revByPeriod
        
    def _aggregateRevByPeriod(self, revSpreadOverPeriods):      
        maxPeriodCount = max(len(l) for l in revSpreadOverPeriods)
        revByPeriod = []
        
        for i in range(maxPeriodCount):
            revforPeriod = 0.0
            for revList in revSpreadOverPeriods:
                if len(revList) - 1 >= i:
                    revforPeriod += float(revList[i])
            revByPeriod.append(revforPeriod)
        return revByPeriod

        
'''
dailyRevs = []
investments = []
ranks = []

rp = RevPlanner(dailyRevs, investments, ranks)
revByPeriod = rp.planRev()
print(revByPeriod)
'''

dailyRevs = [5]
investments = []
ranks = [1]

rp = RevPlanner(dailyRevs, investments, ranks)
revByPeriod = rp.planRev()
print(revByPeriod)

dailyRevs = [5, 20]
investments = []
ranks = [1, 1]

rp = RevPlanner(dailyRevs, investments, ranks)
revByPeriod = rp.planRev()
print(revByPeriod)

dailyRevs = [5, 20]
investments = []
ranks = [2, 3]

rp = RevPlanner(dailyRevs, investments, ranks)
revByPeriod = rp.planRev()
print(revByPeriod)

dailyRevs = [5, 20]
investments = []
ranks = [1, 0]

rp = RevPlanner(dailyRevs, investments, ranks)
revByPeriod = rp.planRev()
print(revByPeriod)

dailyRevs = [5, 20]
investments = []
ranks = [1]

rp = RevPlanner(dailyRevs, investments, ranks)
revByPeriod = rp.planRev()
print(revByPeriod)

dailyRevs = [5, 20]
investments = []
ranks = [6, 2]

rp = RevPlanner(dailyRevs, investments, ranks)
revByPeriod = rp.planRev()
print(revByPeriod)