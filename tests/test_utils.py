import pytest

from unittest import mock

from google.api_core import exceptions

from terminus import create_topic, create_subscription


def test_create_topic():
    publisher = mock.Mock()
    create_topic(publisher, "project", "topic")
    assert publisher.create_topic.call_count == 1


def test_create_topic_already_exist():
    """
    Test topic creation with a topic that already exists
    """
    publisher = mock.Mock()
    publisher.create_topic.side_effect = exceptions.AlreadyExists(
        "topic already exists"
    )
    create_topic(publisher, "project", "topic")
    assert publisher.create_topic.call_count == 1


def test_create_topic_fail():
    """
    Test create topic fail for some reason
    """
    publisher = mock.Mock()
    publisher.create_topic.side_effect = exceptions.GoogleAPIError
    with pytest.raises(exceptions.GoogleAPIError):
        create_topic(publisher, "project", "topic")


def test_create_subscription():
    subscriber = mock.Mock()
    create_subscription(subscriber, "project", "topic", "subscription")
    assert subscriber.create_subscription.call_count == 1


def test_create_subscription_fail():
    """
    Test create subscription fail for some reason
    """
    subscriber = mock.Mock()
    subscriber.create_subscription.side_effect = exceptions.GoogleAPIError
    with pytest.raises(exceptions.GoogleAPIError):
        create_subscription(subscriber, "project", "topic", "subscription")


def test_create_subscription_already_exist():
    """
    Test subscription creation with a subscription that already exists
    """
    subscriber = mock.Mock()
    subscriber.create_subscription.side_effect = exceptions.AlreadyExists(
        "topic already exists"
    )
    create_subscription(subscriber, "project", "topic", "subscription")
    assert subscriber.create_subscription.call_count == 1
