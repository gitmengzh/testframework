import datetime


def lastDay():
    todaydate = datetime.date.today()
    if todaydate.month  in [1, 3, 5, 7, 8, 10, 12] and todaydate.day == 31:
        return True
    elif todaydate.month in [4,6,9,11] and todaydate.day == 30:
        return True
    elif todaydate.month == 2:
        if todaydate.year % 4 == 0 and todaydate.year % 100 !=0 and todaydate.day == 29:
            return True
        elif todaydate.year % 400 == 0 and todaydate.day == 29:
            return True
        elif todaydate.day == 28:
            return True
    else:
        return False

def calcDay(day):      # 判断输入日期是今年的第几天 (年份范围1900~2099)
    if not day or not day.isdigit() or len(day) != 8 or not day[0].isdigit():
        return '输入日期不正确，eg:‘20200222'
    leap = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    normal = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    res = 0
    year = int(day[:4])
    month = int(day[4:6])
    day = int(day[6:])
    if 1900 <= year <= 2099:
        if (month in [1, 3, 5, 7, 8, 10, 12] and day <= 31) or (month in [4, 6, 9, 11] and day <= 30) or month == 2:
            if month == 1:
                res = day
            elif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):      # 判断闰年

                if month == 2 and day > 29:
                    return '输入日期不正确'
                else:
                    for i in range(1, month+1):
                        res += leap[i]
            else:
                if month == 2 and day > 28:
                    return '输入日期不正确'
                else:
                    for i in range(1, month+1):
                        res += normal[i]
        else:
            return '输入日期不正确'
    else:
        return '输入日期不正确'
    return res


if __name__ == "__main__":
    # print(lastDay())
    s1 = ''
    s2 = '202002e1'
    s3 = '-1231233'
    s4 = '2020111'
    s5 = '20200101'
    s6 = '19000229'
    s7 = '20010430'
    # print(calcDay(s7))
    import requests, json
    data = {'price': 10.0,
            'tax': 1.0}
    res = requests.post("127.0.0.1:8000/get_tax", json.dumps(data))
    print(res.content())