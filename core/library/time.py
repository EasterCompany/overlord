# Standard library
from datetime import datetime as _datetime


def get_datetime_str(datetime=None, include_seconds=False):
    """
    Get a standardised date time string for use anywhere in your projects

    :param datetime obj: a datetime object (current time if None)
    :param include_seconds bool: weather or not to count the seconds (0.0 seconds if False)
    :return str: string containing a formated ISO timestamp
    """
    datetime_obj = _datetime.now() if datetime is None else datetime
    if include_seconds:
        return datetime_obj.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    return datetime_obj.strftime("%Y-%m-%dT%H:%M:00.0Z")
