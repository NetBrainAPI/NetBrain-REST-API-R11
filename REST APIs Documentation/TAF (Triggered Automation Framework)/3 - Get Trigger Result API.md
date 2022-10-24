
# Get Trigger Result API Design

## ***POST*** /V1/TAF/Result
Use this API to query triggered task results.

## Detail Information

> **Title** : Get Trigger Result API

> **Version** : 01/31/2022

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/TAF/Result

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|options.scope | String  | Mandatory parameter in multi-tenancy scenario, if the tenantId and domainId are not indicated in the request to specify a particular working domain.<br> If there is only 1 domain in the entire NetBrain system, this parameter is not required. |
|options.tenantId | String  | To specify a particular working tenant. |
|options.domainId | String  | To specify a particular working domain. |
|*options.taskId | String  | The taskId returned from a particular trigger. |


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
|tenantId| String | The task execution context - Tenant ID. |
|domainId| String | The task execution context - Domain ID. |
|status| Integer | The task execution status.<br>0: Pending;<br>1: Running<br>2: Finished<br>3: Failed<br>4: Aborted |
|statusDesc| String | The task execution status description. |
|NIResults| Array | Results of Network Intent (NI) execution. |
|NIResults[].id| String | NI ID. |
|NIResults[].name| String | NI name. |
|NIResults[].niResultId| String | NI result ID. |
|NIResults[].mapId| String | Map ID of the NI. |
|NIResults[].mapName| String | Map name of the NI. |
|NIResults[].messages| Array | The status code and message of the NI execution. |
|NIResults[].messages[].type| Integer | Status code types.<br>1: Success<br>2: Error |
|NIResults[].messages[].message| String | The message details of a status code. |

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
    
def GetTriggerResult(endpoint, API_Body):
    API_URL = r"/V1/TAF/Result"
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
    "option": {
        "taskId":"5c8930f8-c5c4-4645-94b9-d0f1a4c80a76"
    }
}

headers = {
    "Accepted":"application/json",
    "Content-Type":"application/json"
}

token = getTokens(nb_endpoint, nb_username, nb_password)
headers["token"] = token

print(GetTriggerResult(nb_endpoint, api_body))
```

    {'domainId': '311cd0e7-4482-4af9-9e4f-5783becad33f', 'tenantId': 'de3935a3-831b-9d33-e8a5-bc12302b562a', 'status': 2, 'statusDesc': 'Finished', 'NIResults': [{'id': 'd7983990-e91f-4103-8795-fbd0daf28858', 'name': 'Device Reboot US-BOS-R1', 'messages': [{'type': 2, 'message': 'US-BOS-R1 was rebooted recently. Uptime: 35 weeks, 1 day, 11 hours, 26 minutes Last reload reason: Unknown reason  '}], 'mapId': '052e2271-3d97-4ab8-a413-b5674f3a04a6', 'niResultId': 'c2ac05cd-de61-4662-805f-0da397963752'}], 'statusCode': 790200, 'statusDescription': 'Success.'}
    

## Formatted Sample JSON Response


```python
{
  "domainId": "311cd0e7-4482-4af9-9e4f-5783becad33f",
  "tenantId": "de3935a3-831b-9d33-e8a5-bc12302b562a",
  "status": 2,
  "statusDesc": "Finished",
  "NIResults": [
    {
      "id": "d7983990-e91f-4103-8795-fbd0daf28858",
      "name": "Device Reboot US-BOS-R1",
      "messages": [
        {
          "type": 2,
          "message": "US-BOS-R1 was rebooted recently. Uptime: 35 weeks, 1 day, 11 hours, 26 minutes Last reload reason: Unknown reason  "
        }
      ],
      "mapId": "052e2271-3d97-4ab8-a413-b5674f3a04a6",
      "niResultId": "c2ac05cd-de61-4662-805f-0da397963752"
    }
  ],
  "statusCode": 790200,
  "statusDescription": "Success."
}
```
