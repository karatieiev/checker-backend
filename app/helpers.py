import datetime


def timestamp_convertor(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
