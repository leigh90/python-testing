from urllib.parse import urljoin
import requests
BASE_URL = 'http://jsonplaceholder.typicode.com/todos'
TODOS_URL = urljoin(BASE_URL, "todos")
import os

def get_todos():
    auth_key = os.environ["TEST_KEY"]
    request_headers = {"X-Authorization": f"{auth_key}"}
    response = requests.get(TODOS_URL, headers=request_headers)
    # import pdb;pdb.set_trace()
    if response.status_code == 200:
        return response.status_code
    else: 
        return response
    
def get_uncompleted_todos():
    response = get_todos()
    if response is None:
        return []
    else: 
        todos = response.json()
        return [todo for todo in todos if todo.get('completed') == False]
