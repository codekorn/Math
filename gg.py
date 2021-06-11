
import calendar
import time
from datetime import datetime, timedelta
import subprocess
import random

date = [2021, 6, 11]
count = 2
random_number = 8
file = False
def create_git_message(y,m,d):

    day_of_week = datetime(y, m, d).strftime('%a')
    month = calendar.month_abbr[m]
    time = datetime.now().strftime("%H:%M:%S")
    date_message = f"{day_of_week} {month} {d} {time} {y} -0400"
    return f"""GIT_AUTHOR_DATE='{date_message}' GIT_COMMITTER_DATE='{date_message}' git commit -m 'added files'"""

if __name__ == '__main__':
    while int(date[1]) != 5:
        date = list(map(int, date))
        if file:
            subprocess.call('rm random.py', shell=True)
            file = False
        else:
            subprocess.call('touch random.py', shell=True)
            file = True
        subprocess.call('git add -A', shell=True)
        subprocess.call(create_git_message(*date), shell=True)
        subprocess.call('git push', shell=True)



        if random_number == count:
            date = (datetime(*date) + timedelta(days=1))

            if date.strftime('%w') == '6':
                rand_range = (1,4)
            else:
                rand_range = (5,17)
            date = date.strftime('%Y:%m:%d').split(':')
            count = 0
            random_number = random.randint(*rand_range)


        else:
            count += 1

