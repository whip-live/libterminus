import logging


from terminus import setup_logging


def test_setup_logging():
    """
    Test that setup_logging function configures loggers as expected.
    """
    setup_logging("test", "ERROR")
    # check `test` logger has ERROR level
    logger = logging.getLogger("test")
    assert logger.getEffectiveLevel() == logging.ERROR
