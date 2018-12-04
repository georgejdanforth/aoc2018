from utils import (
    get_guard_periods,
    lines_to_records,
    read_input
)

def get_sleepiest_guard(guard_periods):
    return sorted(
        [guard_id for guard_id in guard_periods.keys()],
        key=lambda guard_id: sum(guard_periods[guard_id])
    )[-1]


if __name__ == '__main__':
    records = lines_to_records(read_input())
    guard_periods = get_guard_periods(records)
    sleepiest_guard = get_sleepiest_guard(guard_periods)
    sleepiest_minute = guard_periods[sleepiest_guard].index(
        max(guard_periods[sleepiest_guard])
    )

    print(sleepiest_guard * sleepiest_minute)
