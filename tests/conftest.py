import pytest
import jwt


@pytest.fixture
def encoded_jwt():
    data = {
        'username': 'user',
    }
    return jwt.encode(data, '123456', algorithm='HS256')
