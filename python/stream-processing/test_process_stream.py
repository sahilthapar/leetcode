import pytest
from process_stream import data_event_parser

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






