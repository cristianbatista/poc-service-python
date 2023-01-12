from loguru import logger


def info_and_latency_only(record):
    """Helper function to filter out all levels except for INFO and LATENCY.
    This is used to control which messages are passed to the sink.
    """
    return record["level"].name == "INFO" or record["level"].name == "LATENCY"


def set_logger_configs() -> None:
    """Set custom logger configurations. Add sinks to record logs in specific files.
    Create levels for Response and Latency where each level has a name,
    a severity number (larger is more severe), and a color.
    Params:
        -
    Returns:
        -
    Raises:
        -
    """
    try:
        logger.level("RESPONSE", no=15, color="<green><bold>")
        logger.level("LATENCY", no=15, color="<blue><bold>")
    except TypeError as e:
        logger.warning(f"Level already exists: {e}")
