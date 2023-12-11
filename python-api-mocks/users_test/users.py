import requests

USERS_URL = 'http://jsonplaceholder.typicode.com/users'
HUB_API_ENDPOINT_URL = "https://payg.angazadesign.com/api/query_prospects"
import os

def get_users():
    response = requests.get(USERS_URL)
    if response.ok:
        return response
    else: 
        return None
    

def get_user(user_id):
    all_users=get_users().json()
    for user in all_users:
        if user["id"] == user_id:
            return user 
        
def query_hub_for_prospects(client_phone_suffix, statement_timestamp):
    auth_key = os.environ['UNDERWRITING_API_KEY']
    request_headers = {"BNPL-Authorization": f"{auth_key}"}
    params = {
        "client_phone_suffix": client_phone_suffix,
        "statement_timestamp": statement_timestamp,
    }
    response = requests.get(
        HUB_API_ENDPOINT_URL, params=params, verify=False, timeout=300,headers=request_headers
    )
    if hasattr(response, "status_code"):
        if 200 <= response.status_code < 300:
            return response.json()
    response.raise_for_status()