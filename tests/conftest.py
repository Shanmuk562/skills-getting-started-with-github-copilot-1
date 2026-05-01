import pytest
from fastapi.testclient import TestClient
from src.app import app, activities

INITIAL_ACTIVITIES = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Practice and compete in basketball games",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 15,
        "participants": []
    },
    "Soccer Club": {
        "description": "Learn soccer skills and play matches",
        "schedule": "Wednesdays and Fridays, 3:00 PM - 5:00 PM",
        "max_participants": 20,
        "participants": []
    },
    "Art Club": {
        "description": "Express creativity through painting and drawing",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 10,
        "participants": []
    },
    "Drama Club": {
        "description": "Practice acting and stage performances",
        "schedule": "Tuesdays, 4:00 PM - 5:30 PM",
        "max_participants": 12,
        "participants": []
    },
    "Debate Club": {
        "description": "Develop argumentation and public speaking skills",
        "schedule": "Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 15,
        "participants": []
    },
    "Science Club": {
        "description": "Explore scientific experiments and discoveries",
        "schedule": "Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 18,
        "participants": []
    }
}

@pytest.fixture
def client():
    # Reset activities to initial state
    activities.clear()
    activities.update(INITIAL_ACTIVITIES)
    yield TestClient(app)