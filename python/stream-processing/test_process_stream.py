import pytest
from process_stream import data_event_parser, read_stream

class TestProcessStream:

    @pytest.mark.parametrize(
        argnames=("byte_str", "expected_response"),
        argvalues=[
            (':ok', None),
            ('', None),
            ('event: message', None),
            ('id: [{"topic":"eqiad.mediawiki.recentchange"}]', None),
            ('data: {"user":"BotMultichill","bot":true}', {"user": "BotMultichill", "bot": True})
        ],
        ids=[
            "ok_message",
            "blank_line",
            "event_message",
            "id_message",
            "data_message"
        ]
    )
    def test_process_stream(self, byte_str, expected_response):
        encoded_str = byte_str.encode()
        assert data_event_parser(encoded_str) == expected_response


    @pytest.mark.parametrize(
        argnames=['max_size','full_stream','expected_response'],
        argvalues=[
            (None, ['this', 'is', 'a', 'mock', 'stream'], ['this', 'is', 'a', 'mock', 'stream']),
            (4, ['this', 'is', 'a', 'mock', 'stream'], ['this', 'is', 'a', 'mock'])
        ],
        ids=[
            "default_max_size",
            "set_max_size"
        ]
    )
    def test_read_stream(self, mocker, max_size, full_stream, expected_response):
        mocker.patch('requests.get', return_value=full_stream)
        actual_response = None
        if max_size:
            response = read_stream('mock-url', max_size)
        else:
            response = read_stream('mock-url')

        assert list[response] == expected_response







