import datetime
import time

def convert_hours_to_nano(hrs):
    return hrs*3.6e12

def convert_nano_to_timestamp(nano):
    return int(nano*1e-9)

def convert_nano_to_datetime(nano):
    return datetime.datetime.fromtimestamp(convert_nano_to_timestamp(nano))

print(convert_nano_to_timestamp(1584060974909259269))
print(convert_nano_to_datetime(15839717797210000))