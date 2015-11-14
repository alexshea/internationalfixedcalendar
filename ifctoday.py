import time

ts = time.time()
yearwoleaps = 1970 + (ts/31536000)
numleapyears = int((yearwoleaps-1968)/4)
yearswleaps = 1970 + (ts-(numleapyears*86400))/(31536000)
wholeyears = int(yearswleaps)
if int(yearswleaps) % 4 == 0:
  julianday = int((366 * (yearswleaps-wholeyears))+1)
else:
  julianday = int((365 * (yearswleaps-wholeyears))+1)

ifcmonthnum = int(julianday/28)
ifcdaynum = int(julianday%28)

ifcmonthnum = str(ifcmonthnum)
ifcdaynum = str(ifcdaynum)
wholeyears = str(wholeyears)
print(ifcmonthnum + "-" + ifcdaynum + "-" + wholeyears)
