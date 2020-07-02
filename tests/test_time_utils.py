from terminus.utils import time
from datetime import datetime, timezone


def test_milliseconds_from_datetime():
    dd = datetime(2018, 1, 1, 16, 40, 34, 456000, tzinfo=timezone.utc)
    milliseconds = time.milliseconds_from_datetime(dd)
    assert milliseconds == 1514824834456


def test_milliseconds_from_timestamp():
    ts = "2018-01-01T16:40:34.456Z"
    milliseconds = time.milliseconds_from_timestamp(ts)
    assert milliseconds == 1514824834456
    ts = "2018-01-01T18:40:34.456+02:00"
    milliseconds = time.milliseconds_from_timestamp(ts)
    assert milliseconds == 1514824834456


def test_milliseconds_to_datetime():
    datetime_instance = time.milliseconds_to_datetime(1514824834456)
    expected_datetime_instance = datetime(
        2018, 1, 1, 16, 40, 34, 456000, tzinfo=timezone.utc
    )
    assert datetime_instance == expected_datetime_instance
