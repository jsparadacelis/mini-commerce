import datetime
import calendar

def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day,calendar.monthrange(year,month)[1])
    date = datetime.datetime(year,month,day,sourcedate.hour, sourcedate.minute, sourcedate.second, sourcedate.microsecond, sourcedate.tzinfo)
    return date.isoformat()