from utils import (
    get_guard_periods,
    lines_to_records,
    read_input
)


def get_most_asleep_guard_on_same_minute(guard_periods):
    return sorted(
        [guard_id for guard_id in guard_periods.keys()],
        key=lambda guard_id: max(guard_periods[guard_id])
    )[-1]


if __name__ == '__main__':
    records = lines_to_records(read_input())
    guard_periods = get_guard_periods(records)

    most_asleep_guard_on_same_minute = get_most_asleep_guard_on_same_minute(
        guard_periods
    )

    minute = guard_periods[most_asleep_guard_on_same_minute].index(
        max(guard_periods[most_asleep_guard_on_same_minute])
    )

    print(most_asleep_guard_on_same_minute * minute)
