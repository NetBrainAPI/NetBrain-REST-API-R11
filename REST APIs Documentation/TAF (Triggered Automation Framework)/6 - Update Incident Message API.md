
# Update Incident Message API Design

## ***POST*** /V1/TAF/Updated
Use this API to update event data to an existing NetBrain incident as incident message.
The event data will be transformed to NetBrain incident message by the target incident related Incident Type Incident Message setting.

## Detail Information

> **Title** : Update Incident Message API

> **Version** : 02/24/2022

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/TAF/Updated

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|*specificData | Object  | JSON type. The event data from a third party system. |
|option.scope | String  | Mandatory parameter in multi-tenancy scenario, if the tenantId and domainId are not indicated in the request to specify a particular working domain.<br> If there is only 1 domain in the entire NetBrain system, this parameter is not required. |
|option.tenantId | String  | To specify a particular working tenant. |
|option.domainId | String  | To specify a particular working domain. |
|*option.source | String  | To specify a trigger source address of an Integrated IT System Data Field definition.<br>The information must be pre-defined in a record of Integrated IT System in System Management.  |
|options.category | String  | To specify a category of an Integrated IT System Data Field definition.<br>The information must be pre-defined in the same record of Integrated IT System in System Management as the indicated source of the same request. |
|*option.nbIncidentId | String  | Incident indicator. Use this or option.taksId. If both are provided, the incidentId and the taskId must match 1 same task data. Use this parameter to indicate a particular existing incident. |
|*option.taskId | String  | Task indicator. Use this or option.nbIncidentId. If both are provided, the incidentId and the taskId must match 1 same task data. Use this parameter to indicate a particular existing incident. |


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
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code.  |


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

def UpdateIncidentMessage(endpoint, API_Body):
    API_URL = r"/V1/TAF/Updated"
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
tenantId = ""
domainId = ""
source = "Python Sample"

specificData = {
    "hostname":"US-BOS-R1",
    "status":"rebooted"
}

api_body = {
    "specificData":specificData,
    "option": {
        "scope":"Demo",
        "source":"https://notapplicable.com",
        "category":"Event",
        "nbIncidentId":"100155"
    }
}

headers = {
    "Accepted":"application/json",
    "Content-Type":"application/json"
}

token = getTokens(nb_endpoint, nb_username, nb_password)
headers["token"] = token

print(UpdateIncidentMessage(nb_endpoint, api_body))
```

    {'statusCode': 790200, 'statusDescription': 'Success.'}
    
