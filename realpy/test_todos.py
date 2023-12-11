from nose.tools import assert_true,assert_is_not_none, assert_list_equal, assert_equal
from todos import get_todos,get_uncompleted_todos
import requests
from unittest.mock import Mock, patch


# def test_request_response():
#     response = requests.get('http://jsonplaceholder.typicode.com/todos')
#     assert_true(response.ok)

# def test_request_response_refactor():
#     response = get_todos()
#     assert_is_not_none(response)

# @patch("todos.requests.get")
# def test_getting_mocked_todos(mock_get):
#     headers = {"BNPL-Authorization": "fake_underwriting_api_key"}
#     mock_get.return_value.status_code = 400
#     response = get_todos()
#     # import pdb;pdb.set_trace()

#     assert_is_not_none(response)

# # other ways to patch 


# def test_getting_todos():
#     mock_get_patcher = patch('todos.requests.get')
#     # start patching requests.get
#     mock_get = mock_get_patcher.start()
#     # configure mock to return an ok status code
#     mock_get.return_value.ok = True
#     # call the service which will send a request to the server
#     response = get_todos()
#     #stop patcher
#     mock_get_patcher.stop()
#     #test response
#     assert_is_not_none(response)


# Complete the test service
@patch('todos.requests.get')
def test_getting_todos_when_response_is_ok(mock_get):
    todos = [{
        'userId': 1,
        'id': 1,
        'title': 'Make the bed',
        'completed': False
    }]  
    # configure a mock to return a response with an OK status code.
    mock_get.return_value = Mock(ok=True)
    # A json method that returns a list of todos
    mock_get.return_value.json.return_value = todos
    mock_get.headers = {"X-Authorization": "graham"} 

    # call the service which sends the request
    response = get_todos()
    import pdb;pdb.set_trace()
    assert_list_equal(response.json(), todos)
    assert_equal(response.headers['"X-Authorization"'], mock_get.headers['"X-Authorization"'])

# @patch('todos.requests.get')
# def test_getting_todos_when_response_is_not_ok(mock_get):
#     # configure the mock to return a not OK status code
#     mock_get.return_value.ok = False
#     response = get_todos()
#     import pdb;pdb.set_trace()
#     assert_is_not_none(response)
    

@patch('todos.requests.get')
def test_getting_uncompleted_todos_is_not_none(mock_get_todos):
    todo1 = {
        'userId': 1,
        'id': 1,
        'title': 'Make the bed',
        'completed': False
    }
    todo2 = {
        'userId': 1,
        'id': 2,
        'title': 'Walk the dog',
        'completed': True
    }
    mock_get_todos.return_value = Mock()
    # mock_get_todos.return_value.status_code = 200
    mock_get_todos.return_value.json.return_value = [todo1, todo2]
    mock_get_todos.headers = {"X-Authorization": "graham"}

    uncompleted_todos = get_uncompleted_todos()
    # import pdb;pdb.set_trace()
    assert_equal(mock_get_todos.headers['X-Authorization'], uncompleted_todos.headers['X-Authorization'])
    assert_true(mock_get_todos.called)
    assert_list_equal(uncompleted_todos, [todo1])

# @patch('todos.requests.get')
# def test_getting_uncompleted_todos_when_todos_is_none(mock_get_todos):
#     mock_get_todos.return_value = None
#     uncompleted_todos = get_uncompleted_todos()
#     assert_true(mock_get_todos.called)
#     assert_list_equal(uncompleted_todos, [])
























# class FakeAngazaService(object):
# 	def __init__(
# 		self, valid_prospect_qid="PP000001", has_existing_account=False
# 	):
# 		self.valid_prospect_qid = valid_prospect_qid
# 		self.has_existing_account=has_existing_account
# 		self.fake_api_key = "releasethekracken"
# 		self.headers = {"BNPL-Authorization": f"{self.fake_api_key}"}
# 		os.environ["UNDERWRITING_API_KEY"] = self.fake_api_key

# 	def is_valid_prospect(self, prospect_qid):
# 		return  {"headers": {"content-type": "application/json"}, "status_code": 200}

# 	@httmock.urlmatch(netloc="payg.angazadesign.com", path="/api/query_prospects")
# 	def endpoint(self, url, request):
# 		request_args = parse.parse_qs(parse.urlparse(request.url).query)

        
# 		assert_equal(request.method, "GET")
# 		assert_equal(request.headers['BNPL-Authorization'], self.headers['BNPL-Authorization'])
#         import pdb;pdb.set_trace()
# 		# prospect_qid = request_args["prospect_qid"][0]

# 		# assert_true(prospect_qid)
# 		# return self.is_valid_prospect(prospect_qid)

# 	@contextlib.contextmanager
# 	def installed(self):
# 		with httmock.HTTMock(self.endpoint):
# 			yield
