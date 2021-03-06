"""Config module tests."""

from pytest import raises

from backer.config import parse_config, serialize_config


class TestConfigSerialization:
    """Test the config serialization functionality."""

    def test_serialization(self):
        """Serialization of a config map to string."""
        serialized = serialize_config({"count": 3})
        assert serialized == '{"count": 3}'

    def test_parsing(self):
        """Parsing of a string to config map."""
        config = parse_config('{"count": 3}')
        assert config["count"] == 3
        assert len(config) == 1

    def test_parsing_wrong_type(self):
        """Throw when a config attribute type is incorrect."""
        with raises(ValueError):
            parse_config('{"count": "hello"}')

    def test_parsing_empty(self):
        """Throw when parsing an empty string."""
        with raises(ValueError):
            parse_config("")

    def test_parsing_extra_fields(self):
        """Correctly parse the config when extra fields are present."""
        config = parse_config('{"count": 3, "someOddField": 0}')
        assert config["count"] == 3
        assert len(config) == 1
