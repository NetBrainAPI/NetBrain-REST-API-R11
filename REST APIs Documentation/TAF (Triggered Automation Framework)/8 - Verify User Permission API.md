
# Verify User Permission API Design

## ***POST*** /V1/CMDB/Users/checkPermission
Use this API to verify the current user privileges agains NetBrain system.

## Detail Information

> **Title** : Verify User Permission API

> **Version** : 03/04/2022

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Users/checkPermission

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
| tenantId | String | Tenant UUID. (Not required for system level privileges)|
| domainId | String | Domain UUID. (Not required for system level privileges) |
| *permissions | Array of Strings | The privilege names can be found from NetBrain user management GUI. To convert a GUI name to a name that this API accepts, remove the spaces between the words and set the first character of the first word to lower case, and set the first character of all other words to upper case. <br> For example: <br> Access to Live Network ==> accessToLiveNetwork <br> 1 exceptions:<br> System Administrator ==> systemAdmin|


## Query Parameters(****required***)

> **No query parameter**

## Headers

> **Data Format Headers**

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
| Content-Type | string  | support "application/json" |
| Accept | string  | support "application/json" |

> **Authorization Headers**

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
| token | string  | Authentication token, get from login API. |

## Response

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|privileges| Object | JSON object with the verification result.<br>Key: privilege name<br>Value: Boolean |
|statusCode| integer | The returned status code of executing the API.  |

## Example


```python
import json
import requests
import requests.packages.urllib3 as urllib3
 
urllib3.disable_warnings()

def getTokens(endpoint, user,password):
    login_api_url = r"/V1/Session"
    Login_url = endpoint + login_api_url
    data = {
        "username": user,
        "password": password
    }
    token = requests.post(Login_url, data=json.dumps(
        data), headers=headers, verify=False)
    if token.status_code == 200:
#         print(token.json())
        return token.json()["token"]
    else:
        return "error"

def check_user_permission(endpoint, API_Body):
    API_URL = r"/V1/CMDB/Users/checkPermission"
    api_full_url = endpoint + API_URL
    try:
        api_result = requests.post(api_full_url, data=json.dumps(API_Body), headers=headers, verify=False)
        if api_result.status_code == 200:
            return api_result.json()
        else:
            return api_result.json()
    except Exception as e:
        return str(e)
    
nb_endpoint = "https://netbraintech.com/ServicesAPI/API"
nb_username = ""
nb_password = ""

api_body = {
    "tenantId":"74f04b73-7368-e833-e4be-0a2bc6d44780",
    "domainId":"9791c406-5135-40e2-bd61-3a7903d6b752",
    "permissions":[
        "systemAdmin",
        "systemManagement",
        "domainAdmin",
        "accessToLiveNetwork"
    ]
}

headers = {
    "Accepted":"application/json",
    "Content-Type":"application/json"
}

token = getTokens(nb_endpoint, nb_username, nb_password)
headers["token"] = token

print(check_user_permission(nb_endpoint, api_body))
```

    {'privileges': {'systemAdmin': True, 'systemManagement': True, 'domainAdmin': True, 'accessToLiveNetwork': True}, 'statusCode': 0}
    
