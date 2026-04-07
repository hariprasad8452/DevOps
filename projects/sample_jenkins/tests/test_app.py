from backend.app import app

def test_message():
    client = app.test_client()
    res = client.post("/message", json={"msg": "hi"})
    assert res.status_code == 200
