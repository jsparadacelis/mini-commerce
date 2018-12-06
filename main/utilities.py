import datetime
import calendar
from operator import itemgetter
import itertools

def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day,calendar.monthrange(year,month)[1])
    date = datetime.datetime(

        year,
        month,
        day,
        sourcedate.hour, 
        sourcedate.minute, 
        sourcedate.second, 
        sourcedate.microsecond, 
        sourcedate.tzinfo
        
    )
    return date.isoformat()


def listing_order(arr_items):

    data_list = []
    
    #Ordering item's info for render
    arr_items = sorted(arr_items, key = itemgetter('name'))
    for key, group in itertools.groupby(arr_items, key = lambda x : x['name']):
        l = list(group)
        d = l[0]
        data = {
            "name" : key,
            "quantity" : len(l),
            "value" : d["value"]
        }
        data_list.append(data)
    
    return data_list