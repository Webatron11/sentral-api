from timetable import *


def convertlesson(lessoninput):
    if lessoninput:
        try:
            return Lesson(lessoninput[0]['room_name'], lessoninput[0]['lesson_class_name'], lessoninput[0]['teachers'][0])
        except KeyError:
            return Lesson("N/A", lessoninput[0]['lesson_class_name'], "N/A")
    else:
        return Lesson('', '', '')


def convertperiod(periodinput):
    periods = Periods()
    for i in periodinput:
        if i['name'] != 'am' and i['name'] != 'R' and i['name'] != 'L1' and i['name'] != 'L2' and i['name'] != 'pm':
            x = Period(convertlesson(i['lessons']), i['start_time'], i['end_time'], int(i['name']))
            periods.updateperiod(x)
    return periods


def convertday(dayinput):
    if dayinput['day_name'] != 'Holiday':
        return Day(convertperiod(dayinput['period']), dayinput['date_name'])
    else:
        return Day(Periods(), dayinput['date_name'])


def convertweek(weekinput, letter):
    days = Days()
    for i in weekinput['dates']:
        x = convertday(weekinput['dates'][i])
        days.updateday(x, i)
    return Week(days, letter)


def convertjson(jsoninput):
    return Fornight(convertweek(jsoninput[0], 'a'), convertweek(jsoninput[1], 'b'))
