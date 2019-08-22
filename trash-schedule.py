# script to schedule trash text
# with holidays

import fileinput
from datetime import date, timedelta


today = date.today()


#Monday, September 2 	Labor Day
#Monday, October 14 	Indigenous Peoples’ Day
#Monday, November 11 	Veterans' Day Observed*
#Thursday, November 28 	Thanksgiving Day
#Friday, November 29 	Thanksgiving Friday
#Tuesday, December 24 	Christmas Eve (1/2 day)
#Wednesday, December 25

# to do 
holidays = { date(month=9,day=2,year=2019): True,
            date(month=10, day=14,year = 2019):True,
            date(month=11, day=11,year = 2019):True,
            date(month=11, day=28,year = 2019):True,
            date(month=11, day=29,year = 2019):True,
            date(month=12, day=24,year = 2019):True,
            date(month=12, day=25,year = 2019):True}

file_path = '/var/spool/cron/crontabs/root'

nextline = True

# Read in the file
with open(file_path, 'r') as file :
  filedata = file.read().splitlines()

new_filedata = []
for line in filedata:
    if nextline:
        nextline = False
        # If it was a holiday, set it back to friday
        line = line.replace('FRI','THU')
        # Testing for holiday
        # trying today + i for every day
        for i in range(5):
            if holidays.get(today + timedelta(days=i)) is True:
                print("TRUE")
                line = line.replace('THU', 'FRI')
    if '#TRASH' in line:
        nextline = True
    new_filedata.append(line)

# Write the file out again
with open(file_path, 'w') as file:
  file.write('\n'.join(new_filedata))
