from datetime import datetime
from datetime import timedelta

def convert_datetime_to_string(dtime):
    if not dtime:
        return None
    dstring = ''
    if isinstance(dtime, datetime):
        dstring = dtime.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(dtime, timedelta):
        dstring = str(dtime)
    return dstring

def convert_string_to_datetime(dstring, dtype):
    if not dstring:
        return None
    dtime = None
    if dtype == 'datetime':
        dtime = datetime.strptime(dstring, '%Y-%m-%d %H:%M:%S')
    elif dtype == 'timedelta':
        dtime = datetime.strptime(dstring, '%H:%M:%S')
        dtime = timedelta(hours=dtime.hour, minutes=dtime.minute, seconds=dtime.second)
    return dtime