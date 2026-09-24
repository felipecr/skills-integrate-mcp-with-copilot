from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_github_skills_activity_is_listed():
    response = client.get("/activities")

    assert response.status_code == 200

    activities = response.json()
    assert "GitHub Skills" in activities
    assert activities["GitHub Skills"]["max_participants"] > 0
    assert activities["GitHub Skills"]["participants"] == []
