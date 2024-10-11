from typing import Optional, Dict, ByteString, Iterable
import json
import requests
from functools import reduce

def read_stream(url: str) -> Iterable:
    """
    Reads an url and returns an iterable
    the number of events to read from the stream
    :param url:
    :return:
    """
    response = requests.get(url, stream=True)
    return response.iter_lines(decode_unicode=True)


def data_event_parser(message_line: str) -> Optional[Dict]:
    """
    Takes a byte string and checks the event type
    If not, returns None
    If data event, parses it as a dict and returns that
    :param byte_str:
    :return:
    """
    if not message_line.startswith('data: '):
        return None

    # remove the "data: " and then try json.loads
    data_dict = json.loads(message_line[6:])

    return data_dict


def process_stream(stream: Iterable, max_size: int = 200):
    """
    Process stream to collect stats
    :param stream:
    :param max_size:
    :return:
    """
    stats = {
        'event_count': 0,
        'bot_count': 0
    }
    for message in stream:
        event = data_event_parser(message)
        print(message, event)
        if not event:
            continue
        is_bot = event['bot']
        stats['event_count'] += 1
        stats['bot_count'] += (1 if is_bot else 0)
        if stats['event_count'] == max_size:
            return stats
    # if stream has ended
    return stats

def print_stats(stats: dict):
    event_count = stats['event_count']
    bot_count = stats['bot_count']
    bot_rate = bot_count / float(event_count)

    stats_str = f'''
    Total events: {event_count}
    Bot events: {bot_count}
    Bot rate: {bot_rate}
    '''

    print(stats_str)


def main():
    """
    Reads a stream
    Maps over the stream to parse data events
    Filters only for data events
    Reduces to collect stats
    :return:
    """
    url = 'https://stream.wikimedia.org/v2/stream/recentchange'

    stream = read_stream(url)
    stats = process_stream(stream, 200)
    print_stats(stats)

main()
