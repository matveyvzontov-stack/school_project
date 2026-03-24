import sys
sys.path.append('c:/Users/Schüler/Projekten/school_project')
from app.schemas.user import UserResponse
from app.models import User

user_model = User(id=10, username="tester", email="test@test.com", hashed_password="s")
# Test Pydantic mapping
try:
    user_response = UserResponse.model_validate(user_model)
    print("SUCCESS: ", user_response.model_dump_json())
except Exception as e:
    print("ERROR: ", str(e))
