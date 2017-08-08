import re
from prettytable import PrettyTable
from prettytable import PLAIN_COLUMNS
import sys

s = "107/08/2017 03:005.50#13444014416-> Profit, 2.50% of 220.00 deposited [31/60]207/08/2017 03:0010.83#13444013925-> Profit, 2.50% of 433.00 deposited [33/60]307/08/2017 03:002.55#13444013099-> Profit, 2.50% of 102.00 deposited [35/60]407/08/2017 03:002.85#13444012708-> Profit, 2.50% of 114.00 deposited [36/60]507/08/2017 03:003.65#13444012418-> Profit, 2.50% of 146.00 deposited [37/60]607/08/2017 03:003.63#13444011590-> Profit, 2.50% of 145.00 deposited [39/60]707/08/2017 03:003.05#13444010889-> Profit, 2.50% of 122.00 deposited [41/60]807/08/2017 03:003.08#13444010355-> Profit, 2.50% of 123.00 deposited [42/60]907/08/2017 03:003.35#1344409712-> Profit, 2.50% of 134.00 deposited [44/60]1007/08/2017 03:006.45#1344409081-> Profit, 2.50% of 258.00 deposited [46/60]1107/08/2017 03:002.50"
tbsData="107/08/2017 03:005.50#13444014416-> Profit, 2.50% of 220.00 deposited [31/60]207/08/2017 03:0010.83#13444013925-> Profit, 2.50% of 433.00 deposited [33/60]307/08/2017 03:002.55#13444013099-> Profit, 2.50% of 102.00 deposited [35/60]407/08/2017 03:002.85#13444012708-> Profit, 2.50% of 114.00 deposited [36/60]507/08/2017 03:003.65#13444012418-> Profit, 2.50% of 146.00 deposited [37/60]607/08/2017 03:003.63#13444011590-> Profit, 2.50% of 145.00 deposited [39/60]707/08/2017 03:003.05#13444010889-> Profit, 2.50% of 122.00 deposited [41/60]807/08/2017 03:003.08#13444010355-> Profit, 2.50% of 123.00 deposited [42/60]907/08/2017 03:003.35#1344409712-> Profit, 2.50% of 134.00 deposited [44/60]1007/08/2017 03:006.45#1344409081-> Profit, 2.50% of 258.00 deposited [46/60]1107/08/2017 03:002.50#1344407046-> Profit, 2.50% of 100.00 deposited [53/60]"
patternRev = r"3:00([0-9\.]+)#"
patternInv = r"([0-9\.]+) d"
patternRank = r"\[([0-9\./]+)]" 
patternDate = r"(\d\d/\d\d/\d\d\d\d) "
dailyRev = re.findall(patternRev, tbsData)
print(dailyRev)
investments = re.findall(patternInv, tbsData)
print(investments)
ranks = re.findall(patternRank, tbsData)
print(ranks)
print(re.search(patternDate, tbsData).group())

#sys.exit()

dayTot = sum(float(i) for i in dailyRev)
weekTot = dayTot * 5
monthTot = dayTot * 22

tblSumary = PrettyTable(["Period", "Revenue"]) 
tblSumary.align["Period"] = "r" # Right align
tblSumary.align["Revenue"] = "r" # Right align
tblSumary.padding_width = 0 # Zero space between column edges and contents (default) 
tblSumary.set_style(PLAIN_COLUMNS)
tblSumary.float_format=".2"
tblSumary.add_row(["daily",dayTot]) 
tblSumary.add_row(["weekly",weekTot]) 
tblSumary.add_row(["monthly",monthTot]) 

print(tblSumary)