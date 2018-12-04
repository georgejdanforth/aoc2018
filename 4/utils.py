import dateparser
import datetime
import re

from dataclasses import dataclass


record_regex = r'\[(?P<date_time>.+?)\] (?P<text>.+?)$'
guard_regex = r'Guard #(\d+)'


@dataclass
class Record:
    date_time: datetime.datetime
    text: str
    guard_id: int = None

    def __post_init__(self):
        self.date_time = dateparser.parse(self.date_time)
        guard_match = re.search(guard_regex, self.text)
        if guard_match:
            self.guard_id = int(guard_match.group(1))


def read_input():
    with open('input-4') as input_file:
        return input_file.read().strip().split('\n')


def lines_to_records(lines):
    return sorted([
        Record(*re.search(record_regex, line).group('date_time', 'text'))
        for line in lines
    ], key=lambda record: record.date_time)


def get_guard_periods(records):
    guard_periods = {}
    asleep_times = set()
    guard_id, start = None, None
    while records:
        record = records.pop(0)
        if record.guard_id:
            if guard_id:
                period = [1 if i in asleep_times else 0 for i in range(60)]
                guard_periods[guard_id] = [
                    sum(pair)
                    for pair in zip(guard_periods[guard_id], period)
                ]

                asleep_times = set()

            guard_id = record.guard_id

            if guard_id not in guard_periods:
                guard_periods[guard_id] = [0 for _ in range(60)]

        elif record.text == 'falls asleep':
            start = record.date_time.minute

        elif record.text == 'wakes up':
            asleep_times |= set(range(start, record.date_time.minute))

    return guard_periods
