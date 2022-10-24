import requests
import json
import pythonutil
import time, datetime

def extract_param(param):

    # The NetBrain initial parameters with customized fields.
    if isinstance(param, str):
        param = json.loads(param)  
    #username, password, endpoint are build-in keywords in initial param.
    username = ''
    password = ''
    endpoint = ''
    #callParam is customized fields.
    api_params = {}
    apiServerId = ''
    servInfo = {}
    if 'apiServerId' in param:
        apiServerId = param['apiServerId']
        servInfo = pythonutil.GetApiServerInfo(apiServerId)
        username = servInfo['username']
        password = servInfo['password']
        endpoint = servInfo['endpoint']
        api_params = param['api_params']
    else:
        username = param["username"]
        password = param["password"]
        endpoint = param["endpoint"]
        api_params = param['api_params']
    return (endpoint, username, password, api_params)

def post_data(params):
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    endpoint,username,password,api_params = extract_param(params)
    full_url = endpoint + api_params['api_uri']
    api_data = json.dumps(api_params['body_data'])
    try:
        response = requests.post(full_url, auth = (username, password), headers = headers, data = api_data)
        if response.status_code == 201:
            response_json = response.json()
            return response_json
        else:
            return response.text
    except Exception as e:
        return str(e)
        
def get_data(params):
    endpoint,username,password,api_params = extract_param(params)
    result_url = api_params['result_url']
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    try:
        response = requests.get(result_url, auth = (username, password), headers = headers)
        print(response.text)
        if response.status_code == 200:
            response_json = response.json()
            return response_json
        else:
            return response.text
    except Exception as e:
        return str(e)

# API Domain Manager Test function definition.
def _test(param):
    param = json.loads(param)
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    username = param['username']
    password = param['password']
    full_url = param['endpoint'] + '/v6/credentials.json'
    try:
        response = requests.get(full_url, auth=(username,password), headers=headers, verify=False)
        if response.status_code == 200:
            rtn = {'isFailed':False, 'msg':'Endpoint and credentials are verified!'}
        else:
            json_response = response.json()
            rtn = {'isFailed':True, 'msg':json_response['errorMessage']}
        return json.dumps(rtn)
    except:
        rtn = {'isFailed':True, 'msg':'Endpoint is not reachable!'}
        return rtn