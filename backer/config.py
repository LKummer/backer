"""Configuration serialization and deserialization."""


def parse_config(config):
    """Parse configuration from serialized string.

    Args:
        config (str): Serialized configuration to parse.

    Returns:
        map: Parsed configuration.

    Raises:
        ValueError: If the serialized string failed the verification.
    """
    return {}


def serialize_config(config):
    """Serialize configuration to string.

    Args:
        config (map): Configuration to serialize.

    Returns:
        str: Serialized configuration.
    """
    return ""


def verify_configuration_types(config):
    """Verify the types of configuration attributes.

    Args:
        config (map): Configuration to verify.

    Returns:
        bool: True when types are valid, False when invalid.
    """
    if not isinstance(config.count, str):
        return False
    return True
