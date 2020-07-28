from .logutils import RecordingAdapter  # noqa
from .pipeline import Pipeline  # noqa
from .pubsub_utils import create_topic, create_subscription  # noqa


import logging
from logging.config import dictConfig


# We get the logging level choices from the logging module.
# WARNING: check they don't change `_levelToName` which is an
# implementation detail.
LOGGING_LEVELS = list(logging._levelToName.values())


# Define allowed priority levels to be used when consuming or publishing
# to PubSub topics
PRIORITY_LEVEL_LOW = "low"
PRIORITY_LEVEL_MEDIUM = "medium"
PRIORITY_LEVEL_HIGH = "high"
PRIORITY_LEVELS = (
    PRIORITY_LEVEL_LOW,
    PRIORITY_LEVEL_MEDIUM,
    PRIORITY_LEVEL_HIGH,
)


def setup_logging(
    service_name, service_level="DEBUG", ddagent_host="localhost", ddagent_port=10518
):
    """
    Setup the logger for a service named `service_name`.
    """
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "root": {"level": "ERROR", "handlers": ["console", "ddagent"]},
        "loggers": {
            service_name: {
                "level": service_level,
                "handlers": ["console", "ddagent"],
                "propagate": False,
            },
        },
        "formatters": {"simple": {"format": "%(levelname)s %(name)s %(message)s"}},
        "handlers": {
            "console": {"class": "logging.StreamHandler", "formatter": "simple"},
            "ddagent": {
                "class": "terminus.logutils.JSONDatagramHandler",
                "host": ddagent_host,
                "port": ddagent_port,
                "service": service_name,
            },
        },
    }
    dictConfig(LOGGING)
