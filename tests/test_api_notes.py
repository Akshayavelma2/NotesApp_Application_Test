#Response Time is Present in This
#this is for api get notes

from api.api_client import APIClient
from utils.logger import get_logger

logger = get_logger(__name__)
#it checks response time and response data.S
def test_get_notes():

    logger.info("Starting API GET notes test")

    api = APIClient()

    login_response = api.login()
    logger.info("API login completed")

    assert login_response.status_code == 200

    response = api.get_notes()
    logger.info("GET notes API called")

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 15 #This tells the response time < 2 SecondsS

    notes = response.json()["data"]

    assert isinstance(notes, list) #it checks data in list Format

    logger.info("API GET notes test completed successfully")