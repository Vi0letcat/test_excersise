import pytest
import json
class TestAPI:
    def test_api_get_key(self, api_requests):
        assert api_requests.get_api_key() is not None, "API key should not be None"

    @pytest.mark.parametrize('execution_number', range(5))
    def test_api_create_user(self, execution_number, create_test_user): # run test 5 times
        user_data = create_test_user
        assert user_data[0]["user"]["login_name"] == f"test_name_{user_data[1]}".lower(), f"User was not created. Response:\n{json.dumps(user_data[0])}"
    
    @pytest.mark.parametrize("type", [1, 0, 3])
    def test_api_create_conference(self, type, api_requests, random_string):
        users = []
        for i in range(3): # отдельно генерим трёх юзеров (владельца и двух гостей) через API чтобы не зависить от теста создания юзеров. Не хотел для этого создавать отдельную фикстуру.
            user_data = api_requests.create_user(
                name=f"test_name_{random_string}_{i}",
                password=f"password_{random_string}_{i}",
                email=f"test_{random_string}_{i}@test.ru"
            )
            users.append(user_data["user"]["uid"])
        conf_data = {
            "id": f"test_conf_{random_string}",
            "type": type,
            "topic": f"Test Conference {random_string}",
            "owner": users[0],
            "max_podiums": 10,
            "schedule":{"type": -1},
            "invitations": [
                {"id": users[0]},
                {"id": users[1]},
                {"id": users[2]}
            ]
        }
        response = api_requests.create_conference(conf_data)
        assert response["conference"]["id"] == f"test_conf_{random_string}", f"Conference was not created. Response:\n{json.dumps(response)}"
        for i in range(3):
            assert response["conference"]["invitations"][i]["display_name"] == users[i], f"Invited user {users[i]} is on on the list"
