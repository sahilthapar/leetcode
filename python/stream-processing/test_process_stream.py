import pytest
from process_stream import data_event_parser, process_stream

class TestProcessStream:

    @pytest.mark.parametrize(
        argnames=("stream_string", "expected_response"),
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
    def test_data_event_parser(self, stream_string, expected_response):
        assert data_event_parser(stream_string) == expected_response

    @pytest.mark.parametrize(
        argnames=("stream", "max_size", "expected_stats"),
        argvalues=[
            (
                ['data: {"user":"BotMultichill","bot":true}'],
                200,
                {'event_count': 1, 'bot_count': 1}
            ),
            (
                ['data: {"user":"BotMultichill","bot":false}'],
                200,
                {'event_count': 1, 'bot_count': 0}
            ),
            (
                ['data: {"user":"BotMultichill","bot":false}', 'data: {"user":"BotMultichill","bot":true}'],
                200,
                {'event_count': 2, 'bot_count': 1}
            ),
            (
                [':ok', 'data: {"user":"BotMultichill","bot":true}'],
                200,
                {'event_count': 1, 'bot_count': 1}
            )
        ],
        ids=[
            "single_bot_message",
            "single_non_bot_message",
            "bot_and_non_bot_message",
            "bot_message_with_non_data_message"
        ]
    )
    def test_process_stream(self, stream, max_size, expected_stats):
        assert process_stream(stream, max_size) == expected_stats

