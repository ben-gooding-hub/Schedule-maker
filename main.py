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


def fill_mondays(mondays: list, queue: RandomQueue, bucket_size):
    personCount = 0
    monday_count = len(mondays)
    buckets = []
    for i in range(monday_count):
        buckets.append([])
    # print(monday_count, buckets)
    max_person_count = monday_count * bucket_size
    while personCount < max_person_count:
        added = False
        person = queue.next()
        attempt_count = 0
        while not added:
            bucket_index = random.randrange(monday_count)
            # print(buckets, person)
            if person not in buckets[bucket_index] and len(buckets[bucket_index]) != bucket_size:
                buckets[bucket_index].append(person)
                added = True
                # print("added: " + person)
            if attempt_count >= 100:
                print("skipped " + person)
                break
            attempt_count += 1
        personCount += 1
    return buckets


if __name__ == '__main__':
    bucket_size = 3
    months = 6

    names: list = get_names()
    if len(names) < 2:
        raise Exception("Not enough names")
    queue = RandomQueue(names)

    date = pendulum.now().subtract(months=1)
    monthCount = 0
    while monthCount < months:
        date = date.add(months=1)
        mon = get_mondays_of_month(date)
        pretty_print(fill_mondays(mon, queue, bucket_size))
        print("")
        monthCount += 1

    # pretty_print(mon)
    # for i in range(20):
    #     print(queue.next())
