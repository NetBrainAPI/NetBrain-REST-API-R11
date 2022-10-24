
# Run Specific Incident Type API Design

## ***POST*** /V1/TAF/Run
Use this API to run a specific incident type instead of going through incident type lookup process.

## Detail Information

> **Title** : Run Diagnosis API

> **Version** : 07/19/2022

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/TAF/Run

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
|option.scope | String  | Mandatory parameter in multi-tenancy scenario, if the tenantId and domainId are not indicated inteh request to specify a particular working domain.<br> If there is only 1 domain in the entire NetBrain system, this parameter is not required. |
|option.tenantId | String  | To specify a particular working tenant. |
|option.domainId | String  | To specify a particular working domain. |
|*option.incidentTypeName | String  | To specify an existing Incident Type to be executed. The incident type lookup process will be skipped.|
|option.nbIncidentId | String  | Use this parameter to indicate an existing NetBrain incident. With this parameter provided, the system will update the incident and diagnosis messages into the incident being provided. |


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
|incidentId| String | Trigger task generated incident ID. |
|incidentUrl| String | Trigger task generated incident URL. |
|incidentPortalUrl| String | Trigger task generated incident portal URL. |
|taskId| String | Trigger created task ID.  |


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

def PublishEvent(endpoint, API_Body):
    API_URL = r"/V1/TAF/Run"
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
        "incidentTypeName":"Python Sample"
    }
}

headers = {
    "Accepted":"application/json",
    "Content-Type":"application/json"
}

token = getTokens(nb_endpoint, nb_username, nb_password)
headers["token"] = token

print(PublishEvent(nb_endpoint, api_body))
```

    {'incidentId': '10017G', 'incidentUrl': 'i.html?id=10017G', 'incidentPortalUrl': 'i/10017G', 'taskId': 'f21e2e16-3bcb-4770-aa8f-9d9d0456882c', 'statusCode': 790200, 'statusDescription': 'Success.'}
    

## Formatted Sample JSON Response


```python
{
  "incidentId": "100033",
  "incidentUrl": "i.html?id=100033",
  "incidentPortalUrl": "i/100033",
  "taskId": "5c8930f8-c5c4-4645-94b9-d0f1a4c80a76",
  "statusCode": 790200,
  "statusDescription": "Success."
}
```
