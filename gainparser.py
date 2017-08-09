import re

class BtcTbsGainParser:
    def __init__(self, gainData):
        self.gainData = gainData
        
    def getDailyRevs(self):
        patternRev = r"3:00([0-9\.]+)#"
        dailyRevs = re.findall(patternRev, self.gainData)
        
        return dailyRevs
        
    def getRemainingRevPeriods(self):
        patternRankSplitted = r"\[([0-9\.]+)/([0-9\.]+)]" 
        ranksSplitted = re.findall(patternRankSplitted, self.gainData)
        
        return ranksSplitted
    
    def getInvestments(self):
        patternInv = r"([0-9\.]+) d"
        investments = re.findall(patternInv, self.gainData)
        
        return investments
    
    def getDate(self):
        patternDate = r"(\d\d/\d\d/\d\d\d\d) "
        date = re.search(patternDate, self.gainData).group(1)
        
        return str(date)
