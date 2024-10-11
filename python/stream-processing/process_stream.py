from typing import Optional, Dict, ByteString
import json

def data_event_parser(byte_str: ByteString) -> Optional[Dict]:
    """
    Takes a byte string and checks the event type
    If not, returns None
    If data event, parses it as a dict and returns that
    :param byte_str:
    :return:
    """
    decoded_str = byte_str.decode('utf-8')
    if not decoded_str.startswith('data: '):
        return None

    # remove the "data: " and then try json.loads
    data_dict = json.loads(decoded_str[6:])

    return data_dict



