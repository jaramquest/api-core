import os
import pytest

from fastapi.testclient import TestClient
from jquest.core.models import User
from jquest.core import schemas


@pytest.fixture(scope='module')
def init():
    os.unlink('./test.db')


@pytest.fixture(scope='module')
def client(init) -> TestClient:
    import os
    from jquest.core.main import app

    client = TestClient(app)
    return client


@pytest.fixture(scope='module')
def sample_users():
    '''users with password'''
    return [
        User(id='john', name='John', email='john@jquest.com'),
        User(id='love', name='Love', email='love@jquest.com'),
        User(id='joseph', name='Joseph', email='joseph@jquest.com'),
    ]


@pytest.fixture(scope='module')
def db(client, sample_users):
    from jquest.core.main import db

    for user in sample_users:
        client.post('/users',
                    json=schemas.UserCreate(
                        id=user.id,
                        name=user.name,
                        email=user.email,
                    ).dict())

    return db


def test_get_users(client, sample_users, db):
    res = client.get("/users")
    assert res.status_code == 200
    users = [schemas.User.parse_obj(o) for o in res.json()]
    assert users[0].name == 'John'
    assert len(users) == len(sample_users)