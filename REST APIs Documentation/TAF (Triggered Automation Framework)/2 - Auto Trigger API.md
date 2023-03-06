
# Auto Trigger API Design

## ***POST*** /V1/TAF/Auto
Use this API to send a third party system event data to NetBrain.

## Detail Information

> **Title** : Auto Trigger API

> **Version** : 01/31/2022

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/TAF/Auto

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
|*option.source | String  | To specify a trigger source address of an Integrated IT System Data Field definition.<br>The information must be pre-defined in a record of Integrated IT System in System Management.  |
|option.ticketId | String  | To specify the original ticket ID from Integrated IT system. |
|option.category | String  | To specify a category of an Integrated IT System Data Field definition.<br>The information must be pre-defined in the same record of Integrated IT System in System Management as the indicated source of the same request. |
|option.nbIncidentId | String  | Use this parameter to indicate an existing NetBrain incident. <br>This parameter is used to indicate an incident ID returned from an existing triggered task. To do so, a previously matched Incident Type information can be directly picked instead of going through NetBrain incident type lookup process, to prevent a task from utilizing NetBrain system resource unnecessarily.<br>Use as needed to improve event processing performance. **Only use this parameter if you don't want NetBrain system to do the incident type lookup.**  |
|option.taskId | String  | Must be provided with nbIncidentId together. The taskId returned from a particular trigger.<br>This parameter is used to indicate a taskId returned from an existing triggered task. To do so, a previously matched Incident Type information can be directly picked instead of going through NetBrain incident type lookup process, to prevent a task from utilizing NetBrain system resource unnecessarily.<br>Use as needed to improve event processing performance. **Only use this parameter if you don't want NetBrain system to do the incident type lookup.** |


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
    API_URL = r"/V1/TAF/Auto"
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
        "ticketId":"INC000054"
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
