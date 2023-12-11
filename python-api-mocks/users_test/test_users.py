import unittest
from users import get_users,get_user,query_hub_for_prospects
from unittest.mock import patch,Mock
import os

MATCHING_PROSPECTS_RESPONSE = {
    "count": 2,
    "prospects": [
        {"mpesa_unlock_code": "456789", "prospect_qid": "PP000071"},
        {"mpesa_unlock_code": "403113", "prospect_qid": "PP000096"},
    ],
}


class BasicTests(unittest.TestCase):
    def setUp(self) -> None:
        os.environ["UNDERWRITING_API_KEY"] = "fake_underwriting_api_key"
        self.auth_key = os.environ['UNDERWRITING_API_KEY']
    

    def test_request_response(self):
        response = get_users()

        self.assertEqual(response.status_code, 200)


    @patch("users.requests.get")  # Mock 'requests' module 'get' method.
    def test_request_response_with_decorator(self,mock_get):
        mock_get.return_value.status_code = 200 
        mock_get.headers = {"BNPL-Authorization": "fake_underwriting_api_key"}
        response = get_users()

        self.assertEqual(response.status_code,200)


    def test_request_response_with_context_manager(self):
        with patch("users.requests.get") as mock_get:
            mock_get.return_value.status_code = 200
            response = get_users()
        self.assertEqual(response.status_code, 200)


    def test_request_response_with_patcher(self):
        mock_get_patcher = patch('users.requests.get')
        mock_get = mock_get_patcher.start()
        mock_get.return_value.status_code = 200
        response = get_users()
        mock_get_patcher.stop()
        self.assertEqual(response.status_code, 200)


    def test_mock_whole_function(self):
        mock_get_patcher = patch('users.requests.get')
        users = [{
            "id": 0,
            "first_name": "Dell",
            "last_name": "Norval",
            "phone": "994-979-3976"
        }]

        mock_get = mock_get_patcher.start()
        mock_get.return_value = Mock(status_code = 200)
        mock_get.return_value.json.return_value = users

        response = get_users()
        mock_get_patcher.stop()

        # import pdb;pdb.set_trace()s

        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(), users)

    @patch("users.get_users")
    def test_get_one_user(self, mock_get_users):
        users =  [
            {'phone': '514-794-6957', 'first_name': 'Brant', 'last_name': 'Mekhi', 'id': 0},
            {'phone': '772-370-0117', 'first_name': 'Thalia', 'last_name': 'Kenyatta', 'id': 1},
            {'phone': '176-290-7637', 'first_name': 'Destin', 'last_name': 'Soledad', 'id': 2}
        ]
        mock_get_users.return_value = Mock()
        mock_get_users.return_value.json.return_value = users
        user = get_user(2)
        # import pdb;pdb.set_trace() # Mock status code of response.
        
        self.assertEqual(user,users[2])

    @patch(
        "users.query_hub_for_prospects",
        return_value=MATCHING_PROSPECTS_RESPONSE,
    )
    def test_get_one_user(self, mock_get):
        
        mock_get.return_value = Mock()
        mock_get.headers = {"BNPL-Authorization": "fake_underwriting_api_key"}
        mock_get.return_value.json.return_value = MATCHING_PROSPECTS_RESPONSE
        response = query_hub_for_prospects({"client_phone_suffix": "191"},{"statement_timestamp": "2023-05-18T00:00:00"})
        # import pdb;pdb.set_trace() # Mock status code of response.
        
        self.assertEqual(mock_get.headers["BNPL-Authorization"],"fake_underwriting_api_keys")







    # def test_request_response_with_patcher(self):
    #     mock_get_patcher = patch("users.requests.get")
    #     mock_get = mock_get_patcher.start()
    #     mock_get.return_value.status_code = 200
    #     response = get_users()
    #     mock_get_patcher.stop()
    #     self.assertEqual(response.status_code,200)




if __name__ == "__main__":
    unittest.main()       


# class BasicTests(unittest.TestCase):
#     def test_mock_whole_function(self):
#         mock_get_patcher = patch('users.requests.get')
#         users = [{
#             "id": 0,
#             "first_name": "Dell",
#             "last_name": "Norval",
#             "phone": "994-979-3976"
#         }]
#         mock_get = mock_get_patcher.start()
#         mock_get.return_value = Mock(status_code = 200)
#         mock_get.return_value.json.return_value = users

#         response  = get_users()
#         mock_get_patcher.stop()

#         self.assertEqual(response.status_code,200)
#         self.assertEqual(response.json(),users)


# if __name__ == "__main__":
#     unittest.main()  