import logging

from google.api_core import exceptions


logger = logging.getLogger(__name__)


def create_topic(publisher, google_project_id, topic):
    """
    Create pubsub topic from google project id and topic.

    :param Publisher publisher: Publisher instance.
    :param string project: google project id.
    :param string topic: topic name.
    """
    topic_path = publisher.topic_path(google_project_id, topic)
    try:
        topic = publisher.create_topic(topic_path)
        logger.info("Topic %s correclty created", topic)
    except exceptions.AlreadyExists:
        logger.warning("Topic already exist")
    except exceptions.GoogleAPIError:
        logger.exception("Something went wrong while creating topic")
        raise


def create_subscription(subscriber, google_project_id, topic, subscription, **kwargs):
    """
    Create subscription where we are going to pull messages.

    Subscription is a string built using:
    - google_project_id
    - topic
    - subscription name.

    :param Subscriber subscriber: Subscriber instance.
    :param string project: google project id.
    :param string topic: topic name.
    :param string subscription: subscription name.
    """
    topic_path = subscriber.topic_path(google_project_id, topic)
    subscription_path = subscriber.subscription_path(google_project_id, subscription)
    try:
        subscription = subscriber.create_subscription(
            subscription_path, topic_path, **kwargs
        )
        logger.info("Subscription %s correctly created", subscription)
    except exceptions.AlreadyExists:
        logger.warning("Subscription already exist")
    except exceptions.GoogleAPIError:
        logger.exception("Somethings went wrong while creating subscription")
        raise
