from fastapi.testclient import TestClient

from src.app import app, activities


client = TestClient(app)


def test_delete_participant_removes_student_from_activity():
    original_participants = activities["Chess Club"]["participants"]
    activities["Chess Club"]["participants"] = ["michael@mergington.edu"]

    try:
        response = client.delete(
            "/activities/Chess Club/signup?email=michael@mergington.edu"
        )

        assert response.status_code == 200
        assert activities["Chess Club"]["participants"] == []
        assert response.json()["message"] == "Removed michael@mergington.edu from Chess Club"
    finally:
        activities["Chess Club"]["participants"] = original_participants
