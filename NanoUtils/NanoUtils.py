import datetime
import time

def convert_datetime_to_nano(dt):
    return int(datetime.datetime.timestamp(dt)*1e+9)

def convert_hours_to_nano(hrs):
    return hrs*3.6e12

def convert_nano_to_timestamp(nano):
    return int(nano*1e-9)

def convert_nano_to_datetime(nano):
    return datetime.datetime.fromtimestamp(convert_nano_to_timestamp(nano))
