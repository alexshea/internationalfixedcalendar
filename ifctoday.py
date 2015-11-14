import time

def main():
  ts = time.time()
  year_wo_leaps = 1970 + (ts/31536000)
  num_leap_years = int((year_wo_leaps-1968)/4)
  years_w_leaps = 1970 + (ts-(num_leap_years*86400))/(31536000)
  currentyear = int(years_w_leaps)
  if currentyear % 4 == 0:
    julian = int((366 * (years_w_leaps-currentyear))+1)
  else:
    julian = int((365 * (years_w_leaps-currentyear))+1)

  ifc_month = int((julian/28)+1)
  ifc_day = int(julian%28)

  if ifc_month == 1 and ifc_day == 1:
    print("Today is International Party Day!")
    return 0
  if ifc_month == 14 and ifc_day == 1:
    print("Today is Leap Year Day!")
    return 0

  ifc_month = str(ifc_month)
  ifc_day = str(ifc_day)
  currentyear = str(currentyear)
  print("Today is " + ifc_month + "-" + ifc_day + "-" + currentyear)

main()
