"""
Helper functions to compute milliseconds elapsed from POSIX epoch.

We can convert a datetime instance or a timestamp in ISO format
to the amount of milliseconds from POSIX epoch, and back from milliseconds
to the datetime instance.
"""

from datetime import datetime, timedelta, timezone


_epoch = datetime(1970, 1, 1, tzinfo=timezone.utc)


def milliseconds_from_datetime(datetime_instance):
    """Convert a datetime object to milliseconds."""
    # POSIX epoch
    return (datetime_instance - _epoch) // timedelta(milliseconds=1)


def milliseconds_from_timestamp(timestamp):
    """Convert a timestamp string in iso format to milliseconds."""
    datetime_instance = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    return milliseconds_from_datetime(datetime_instance)


def milliseconds_to_datetime(milliseconds):
    """Convert the number of milliseconds to a datetime instance."""
    return _epoch + timedelta(milliseconds=milliseconds)
