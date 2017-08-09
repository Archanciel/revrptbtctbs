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

'''        

s = "107/08/2017 03:005.50#13444014416-> Profit, 2.50% of 220.00 deposited [31/60]207/08/2017 03:0010.83#13444013925-> Profit, 2.50% of 433.00 deposited [33/60]307/08/2017 03:002.55#13444013099-> Profit, 2.50% of 102.00 deposited [35/60]407/08/2017 03:002.85#13444012708-> Profit, 2.50% of 114.00 deposited [36/60]507/08/2017 03:003.65#13444012418-> Profit, 2.50% of 146.00 deposited [37/60]607/08/2017 03:003.63#13444011590-> Profit, 2.50% of 145.00 deposited [39/60]707/08/2017 03:003.05#13444010889-> Profit, 2.50% of 122.00 deposited [41/60]807/08/2017 03:003.08#13444010355-> Profit, 2.50% of 123.00 deposited [42/60]907/08/2017 03:003.35#1344409712-> Profit, 2.50% of 134.00 deposited [44/60]1007/08/2017 03:006.45#1344409081-> Profit, 2.50% of 258.00 deposited [46/60]1107/08/2017 03:002.50"
tbsData="107/08/2017 03:005.50#13444014416-> Profit, 2.50% of 220.00 deposited [31/60]207/08/2017 03:0010.83#13444013925-> Profit, 2.50% of 433.00 deposited [33/60]307/08/2017 03:002.55#13444013099-> Profit, 2.50% of 102.00 deposited [35/60]407/08/2017 03:002.85#13444012708-> Profit, 2.50% of 114.00 deposited [36/60]507/08/2017 03:003.65#13444012418-> Profit, 2.50% of 146.00 deposited [37/60]607/08/2017 03:003.63#13444011590-> Profit, 2.50% of 145.00 deposited [39/60]707/08/2017 03:003.05#13444010889-> Profit, 2.50% of 122.00 deposited [41/60]807/08/2017 03:003.08#13444010355-> Profit, 2.50% of 123.00 deposited [42/60]907/08/2017 03:003.35#1344409712-> Profit, 2.50% of 134.00 deposited [44/60]1007/08/2017 03:006.45#1344409081-> Profit, 2.50% of 258.00 deposited [46/60]1107/08/2017 03:002.50#1344407046-> Profit, 2.50% of 100.00 deposited [53/60]"

patternRev = r"3:00([0-9\.]+)#"
patternInv = r"([0-9\.]+) d"
patternRank = r"\[([0-9\./]+)]" 
patternRankSplitted = r"\[([0-9\.]+)/([0-9\.]+)]" 
patternDate = r"(\d\d/\d\d/\d\d\d\d) "
dailyRev = re.findall(patternRev, tbsData)
f = open('/storage/emulated/0/download/out.txt','a')
f.write('dailyRev\n' + str(dailyRev))
f.write('\n')
print(dailyRev)
investments = re.findall(patternInv, tbsData)
f.write('investments\n' + str(investments))
f.write('\n')
print(investments)
ranks = re.findall(patternRank, tbsData)
print(ranks)
ranksSplitted = re.findall(patternRankSplitted, tbsData)
f.write('ranksSplitted\n' + str(ranksSplitted))
f.write('\n')


date = re.search(patternDate, tbsData).group()
f.write('date\n' + date)


print(date)

'''