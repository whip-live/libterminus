import logging


from terminus import setup_logging


def test_setup_logging():
    """
    Test that setup_logging function configures loggers as expected.
    """
    setup_logging('test', 'ERROR', 'ERROR', 'foo', '3296')
    # check `test` logger has ERROR level
    logger = logging.getLogger('test')
    assert logger.getEffectiveLevel() == logging.ERROR
    # check `kafka` logger has ERROR level
    logger = logging.getLogger('kafka')
    assert logger.getEffectiveLevel() == logging.ERROR
