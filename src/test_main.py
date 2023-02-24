import json
from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def when_acessed_it_should_return_the_up_state_and_the_200_status_code():
    response = client.post("/generate_prompt")
    assert response.status_code == 200

def when_given_prompt_it_should_return_a_response_from_chat_gpt_and_the_200_status_code():
    response = client.post("/generate_prompt")
    assert response.status_code == 200
    assert json.loads(response.json())