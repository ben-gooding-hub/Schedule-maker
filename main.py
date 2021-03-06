import random

import pendulum

from RandomQueue import RandomQueue


def get_names():
    f = open('names.txt')
    file_names: list = f.read().splitlines()
    f.close()
    return file_names


def get_mondays_of_month(date: pendulum):
    mondays = [date._first_of_month(pendulum.MONDAY)]
    month = mondays[0].month
    next_monday = mondays[0].next(pendulum.MONDAY)
    while month == next_monday.month:
        mondays.append(next_monday)
        next_monday = mondays[-1].next(pendulum.MONDAY)
    return mondays


def pretty_print(items):
    for item in items:
        print(item)


def fill_mondays(mondays: list, queue: RandomQueue, bucket_size, should_throw):
    person_count = 0
    monday_count = len(mondays)
    buckets = []
    for i in range(monday_count):
        buckets.append([])
    max_person_count = monday_count * bucket_size
    while person_count < max_person_count:
        added = False
        person = queue.next()
        attempt_count = 0
        while not added:
            bucket_index = random.randrange(monday_count)
            if person not in buckets[bucket_index] and len(buckets[bucket_index]) != bucket_size:
                buckets[bucket_index].append(person)
                added = True
            if attempt_count >= 100:
                if should_throw:
                    raise Exception("Failed to pick names")
                else:
                    print("skipped " + person)
                break
            attempt_count += 1
        person_count += 1
    return buckets


if __name__ == '__main__':
    bucket_size = 3
    months = 6
    should_throw = False  # throw an exception if an error occurs, else print it instead

    names: list = get_names()
    if len(names) < 2:
        raise Exception("Not enough names")
    queue = RandomQueue(names)

    date = pendulum.now().subtract(months=1)
    monthCount = 0
    while monthCount < months:
        date = date.add(months=1)
        mon = get_mondays_of_month(date)
        pretty_print(fill_mondays(mon, queue, bucket_size, should_throw))
        print("")
        monthCount += 1
