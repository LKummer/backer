"""Config module tests."""

from pytest import fixture, raises

from backer.config import parse_config, serialize_config


class TestConfigSerialization:
    """Test the config serialization functionality."""

    def test_serialization(self):
        serialized = serialize_config({"count": 3})
        assert serialized == '{"count": 3}'

    def test_parsing(self):
        config = parse_config('{"count": 3}')
        assert config.count == 3
        assert len(config) == 1

    def test_parsing_wrong_type(self):
        with raises(ValueError):
            parse_config('{"count": "hello"}')
