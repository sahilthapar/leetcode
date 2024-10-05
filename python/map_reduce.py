import json
from typing import List
from collections import defaultdict
from functools import reduce

from prettytable import PrettyTable

# map reduce to process the data
def process_data(metrics: List[dict]):
    """
    Map reduce method to process the data
    :param metrics:
    :return:
    """
    # map over each record to extract category and metric
    mapped = map(lambda x: (x['category'], x['metric']), metrics)

    # create an accumulator, it's a dict where each value is a dict which can have float values
    # example
    # {
    #     "category1": {"total": 0.0, "count": 0.0},
    #     "category2": {"total": 0.0, "count": 0.0},
    # }
    category_acc = defaultdict(lambda: defaultdict(float))

    # reducer function, adds the total to the category.total and increases the count
    def reducer(acc, item):
        category, metric = item
        acc[category]['total'] += metric
        acc[category]['count'] += 1
        return acc

    # reduce needs a reducer method, an iterable and an accumulator
    reduced = reduce(reducer, mapped, category_acc)

    # for each category, find the average (and possibly any other stats)
    return [(k, round(v['total']/v['count'], 2)) for k, v in reduced.items()]


def read_data(path: str):
    """
    Read json file
    :param path:
    :return:
    """
    with open(path, 'r') as f:
        return json.loads(f.read())

def tabulate(data: List[tuple]):
    """
    Helper method to create a PrettyTable from data
    :param data:
    :return:
    """
    table = PrettyTable()
    table.title = 'Average Metric by Category'
    table.field_names = ['Category', "Avg_metric"]

    for category, metric in data:
        table.add_row([category, metric])
    return table


if __name__ == '__main__':
    data = read_data('data.json')
    processed = process_data(data)
    table = tabulate(processed)
    print(table)

# Output
# +----------------------------+
# | Average Metric by Category |
# +------------+---------------+
# |  Category  |   Avg_metric  |
# +------------+---------------+
# |   Sales    |     123.33    |
# | Marketing  |     93.33     |
# |  Support   |      80.0     |
# |  Product   |     140.0     |
# +------------+---------------+




