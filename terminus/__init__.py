from .adapter import RecordingAdapter # noqa
from .pipeline import Pipeline # noqa


import logging
from logging.config import dictConfig


# We get the logging level choices from the logging module.
# WARNING: check they don't change `_levelToName` which is an
# implementation detail.
LOGGING_LEVELS = list(logging._levelToName.values())


def setup_logging(service_name, service_level='DEBUG', kafka_level='DEBUG',
                  logstash_host='localhost', logstash_port='9300'):
    """
    Setup the logger for a service named `service_name`.
    """
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'root': {
            'level': 'ERROR',
            'handlers': ['console', 'logstash'],
        },
        'loggers': {
            service_name: {
                'level': service_level,
                'handlers': ['console', 'logstash'],
                'propagate': False,
            },
            'kafka': {
                'level': kafka_level,
                'handlers': ['console', 'logstash'],
                'propagate': False,
            }
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(name)s [%(process)d] %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(name)s %(message)s'
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'simple',
            },
            'logstash': {
                'class': 'logstash.LogstashHandler',
                'host': logstash_host,
                'port': logstash_port,
                'version': 1,
                'message_type': service_name,
            },
        },
    }
    dictConfig(LOGGING)
