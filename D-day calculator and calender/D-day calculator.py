
import datetime

def dday(day1, day2) :
    calculation = day2 - day1 + datetime.timedelta(days=1)
    return calculation.days
def plustime(day1, day) :
    plus = datetime.timedelta(days=day)
    add = day1 + plus
    return add.strftime('%Y-%m-%d')

if __name__ == "__main__":
    ref_day = input('reference date (20xx-xx-xx) (if today, write "today"): ')
    if ref_day == 'today' :
        day1 = datetime.datetime.now()
    else :
        day1 = datetime.datetime.strptime(ref_day, '%Y-%m-%d')
    check_function= int(input(
        'if you want D-day counting, press 1 or if you want to check the date of n-day after, press 2 : '))
    if check_function == 1 :
        check_date = input('write down the date (20xx-xx-xx): ')
        day2 = datetime.datetime.strptime(check_date, '%Y-%m-%d')
        print('D-Day :', dday(day1,day2))
    if check_function == 2:
        check_days = int(input('How many days after?: '))
        day = check_days
        print(plustime(day1, day))
