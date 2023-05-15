import time
import re
from datetime import datetime

from humanfriendly import coerce_seconds, format_timespan


def get_current_time(time_format="%I:%M:%S %p"):
    return datetime.now().strftime(time_format)


def get_monotonic_time(should_round=True, as_seconds=False):
    multiplication_factor = 1 if as_seconds else 1000

    if should_round:
        return round(time.monotonic() * multiplication_factor)

    return time.monotonic() * multiplication_factor


def format_time(time, compact=False):
    formatted_time = format_timespan(coerce_seconds(time))

    if compact:
        replacements = {
            r"\s+\b(seconds?)\b": "s",
            r"\s+\b(minutes?)\b": "m",
            r"\s+\b(hours?)\b": "h",
            r"\s+\b(days?)\b": "d",
            r"\s+\b(weeks?)\b": "w",
            r"\s+\b(years?)\b": "y",
            r"\s*,|(and)\s+": "" # remove commas and the word "and"
        }

        for pattern, replacement in replacements.items():
            formatted_time = re.sub(pattern, replacement, formatted_time)

    return formatted_time
