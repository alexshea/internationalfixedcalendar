import time

ts = time.time()
year_wo_leaps = 1970 + (ts/31536000)
num_leap_years = int((year_wo_leaps-1968)/4)
years_w_leaps = 1970 + (ts-(num_leap_years*86400))/(31536000)
currentyear = int(years_w_leaps)
if currentyear % 4 == 0:
  julianday = int((366 * (years_w_leaps-currentyear))+1)
else:
  julianday = int((365 * (years_w_leaps-currentyear))+1)

ifcmonthnum = int(julianday/28)
ifcdaynum = int(julianday%28)

ifcmonthnum = str(ifcmonthnum)
ifcdaynum = str(ifcdaynum)
currentyear = str(currentyear)
print("Today is " + ifcmonthnum + "-" + ifcdaynum + "-" + currentyear)
