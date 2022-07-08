import csv
from datetime import datetime, date
from pprint import pp


def load_data(filepath):
    with open(filepath) as f:
        csv_data = csv.DictReader(f)
        return [l for l in csv_data]


def find_dt_actions(record: dict):
    name = record.pop('name')
    case_id = record.pop('case_id')
    result = {}
    for action, dt in record.items():
        if not dt:
            continue
        try:
            action_dt = datetime.fromtimestamp(dt)
        except Exception as ex:
            print(f"Action {dt} is not a date")
            continue
        else:
            result[action] = action_dt
    return case_id, name, result


def filter_by_date(on_date: date, record: dict):
    result = {}
    for action, dt in record:
        if dt.date() == on_date:
            result[action] = dt
    return result


def sort_by_newest(dates: dict):
    return sorted(dates, key=dates.get, reverse=True)


if __name__ == '__main__':
    FILENAME = 'data.csv'
    ON_DATE = date.today()
    persons_results = {}
    records = load_data(filepath=FILENAME)
    for record in records:
        case_id, name, dates = find_dt_actions(record)
        by_dates = filter_by_date(ON_DATE, dates)
        sorted_dates = sort_by_newest(by_dates)
        persons_results[name] = {case_id: sorted_dates}

    pp(persons_results)
