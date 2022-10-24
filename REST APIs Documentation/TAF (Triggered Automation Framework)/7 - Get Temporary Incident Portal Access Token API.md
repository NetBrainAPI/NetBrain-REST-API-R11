
# Get Temporary Incident Portal Access Token API Design

## ***POST*** /V1/portal-auth-ticket
Use this API to get a temporary Incident Portal access token.
The token will be appended into the URL to automatically get users into an Incident Portal record.
This API can be used for a particular 3rd party system integration to automatically authenticate the 3rd party system users to a NetBrain Incident Portal record, which is triggered by the 3rd party system instance.

## Detail Information

> **Title** : Get Temporary Incident Portal Access Token API

> **Version** : 03/01/2022

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/portal-auth-ticket

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
| portalId | String | Incident Portal record UUID. |


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
|ticket| string | The temporary Incident Portal access token.<br> Sample Incident Portal URL using token: <br> https://netbrain-endpoint.com/portal/i/10017G?token=a6b84168-dee0-46c3-8c7c-6d85b6d0f634 |
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

def GetTemporaryAccessToken(endpoint, API_Body):
    API_URL = r"/V1/portal-auth-ticket"
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
    "portalId":"10017G"
}

headers = {
    "Accepted":"application/json",
    "Content-Type":"application/json"
}

token = getTokens(nb_endpoint, nb_username, nb_password)
headers["token"] = token

print(GetTemporaryAccessToken(nb_endpoint, api_body))
```

    {'ticket': '8f249cbd-f8b4-4329-8e2e-ec13780ebb9d', 'statusCode': 0}
    
