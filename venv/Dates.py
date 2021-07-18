from datetime import datetime

from dateutil.relativedelta import relativedelta

td= datetime.today().weekday()

days_in_gym = ['Monday','Wednesday','Friday','Tuesday','Saturday']

days_of_week_code = {
              'Monday': 0 ,
              'Tuesday': 1,
              'Wednesday': 2,
              'Thursday': 3,
              'Friday': 4,
              'Saturday': 5,
              'Sunday': 6,
}

name_of_days = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday',
]
coded_day_in_gym= []
for day in days_in_gym:
    coded_day_in_gym.append(days_of_week_code[day])

Days_for_booking = []
for coded_day in coded_day_in_gym:
    Days_for_booking.append(coded_day+1)

#check if current day is a day to make a booking and define next day in the gym

next_day_to_book = datetime.now() + relativedelta(days=6)
next_day_formatted = next_day_to_book.strftime("%d/%m/%Y")
next_day_string = name_of_days[next_day_to_book.weekday()]
next_day_javaformat = next_day_to_book.strftime("%Y-%m-%d")

if td in Days_for_booking:
    print(' I need to book today for ' + next_day_formatted)
    test = True
else:
    print ('Today is not a booking day')
    test = False
