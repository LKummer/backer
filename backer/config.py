"""Configuration serialization and deserialization."""

from json import dumps, loads


def parse_config(config):
    """Parse configuration from serialized string.

    Args:
        config (str): Serialized configuration to parse.

    Returns:
        map: Parsed configuration.

    Raises:
        ValueError: If the serialized string failed the verification.
    """
    unverified_config = loads(config)
    if not verify_configuration_types(unverified_config):
        raise ValueError("Configuration verification failed.")
    result = {"count": unverified_config["count"]}
    return result


def serialize_config(config):
    """Serialize configuration to string.

    Args:
        config (map): Configuration to serialize.

    Returns:
        str: Serialized configuration.
    """
    return dumps(config)


def verify_configuration_types(config):
    """Verify the types of configuration attributes.

    Args:
        config (map): Configuration to verify.

    Returns:
        bool: True when types are valid, False when invalid.
    """
    if not isinstance(config["count"], int):
        return False
    return True
