import pytest
from userService.app import app as user_app
from chatService.app import app as chat_app
from notificationService.app import app as notify_app

@pytest.fixture
def user_client():
    return user_app.test_client()

@pytest.fixture
def chat_client():
    return chat_app.test_client()

def test_user_health(user_client):
    res = user_client.get('/health')
    assert res.status_code == 200
    assert b"User Service is Up" in res.data

def test_chat_messages(chat_client):
    res = chat_client.get('/messages')
    assert res.status_code == 200
    assert len(res.get_json()['messages']) > 0
