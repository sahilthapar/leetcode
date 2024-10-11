from typing import Tuple, AnyStr, Optional, Dict

def data_event_parser(byte_str: bytes) -> Optional[dict]:
    """
    Takes a byte string and returns an event type and a dict of tha parsed message
    :param text:
    :return:
    """
    decoded_str = byte_str.decode('utf-8')
    if not decoded_str.startswith('data: '):
        return None



