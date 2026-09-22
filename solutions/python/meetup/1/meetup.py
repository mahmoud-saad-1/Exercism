# subclassing the built-in ValueError to create MeetupDayException
import calendar
import datetime

class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message
    

week_indexes = {
    'first': 0,
    'second': 1,
    'third': 2,
    'fourth': 3,
    'fifth': 4,
    'last': -1
}
def meetup(year, month, week, day_of_week):
    matching_days = []
    for i in range(1, calendar.monthrange(year,month)[1] + 1):
        if calendar.day_name[calendar.weekday(year,month,i)] == day_of_week:
            matching_days.append(i)
    try:
        if week == 'teenth':
            for day in matching_days:
                if 13 <= day <=19:
                    return datetime.date(year, month, day)
        else:
            return datetime.date(year, month, matching_days[week_indexes[week]])
    except (IndexError, KeyError):
        raise MeetupDayException("That day does not exist.")