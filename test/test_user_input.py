import pytest
import sys
sys.path.append('src')
from datetime import datetime
from user_input import UserInputHandler

from datetime import datetime

def test_parse_date_valid_date():
    user_input_handler = UserInputHandler()
    date_str = "2023/10/27"
    parsed_date = user_input_handler._parse_date(date_str)
    assert parsed_date == datetime(2023, 10, 27)

def test_parse_date_invalid_date():
    user_input_handler = UserInputHandler()
    date_str = "abc/123/456"
    parsed_date = user_input_handler._parse_date(date_str)
    assert parsed_date is None

def test_parse_date_today():
    user_input_handler = UserInputHandler()
    date_str = "today"
    parsed_date = user_input_handler._parse_date(date_str)
    assert parsed_date.date() == datetime.today().date()

def test_parse_time_invalid_time():
    user_input_handler = UserInputHandler()
    time_str = "abc:def"
    parsed_time = user_input_handler._parse_time(time_str)
    assert parsed_time is None

def test_parse_time_without_ampm():
    user_input_handler = UserInputHandler()
    time_str = "10:30"
    parsed_time = user_input_handler._parse_time(time_str)
    assert parsed_time == datetime.strptime(time_str + "AM", user_input_handler.time_format)
