
# Get Triggered Diagnosis Definition API Design

## ***POST*** /V1/TAF/ManuallyDiagnosis
Use this API to query trigger definition on NetBrain end.

## Detail Information

> **Title** : Get Triggered Diagnosis Definition

> **Version** : 01/31/2022

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/TAF/ManuallyDiagnosis

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|options.scope | String  | Mandatory parameter in multi-tenancy scenario, if the tenantId and domainId are not indicated inteh request to specify a particular working domain.<br> If there is only 1 domain in the entire NetBrain system, this parameter is not required. |
|options.tenantId | String  | To specify a particular working tenant. |
|options.domainId | String  | To specify a particular working domain. |
|*type| Integer | 1: To manually trigger a map<br>2: To manually trigger a diagnosis task. |


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
|diagnosises.id| String | The ID of a Triggered Diagnosis definition. |
|diagnosises.name| String | The name of a Triggered Diagnosis definition. |
|diagnosises.params| Array | Triggered Diagnosis Filter for Member Network Intent setting. |
|diagnosises.params[].name| String | Parameter name. |
|diagnosises.params[].hint| String | Parameter hint. |
|diagnosises.params[].prompt| String | Parameter prompt. |
|diagnosises.params[].allowInput| Boolean | Whether or not the parameter allows the trigger to provide an input. |
|diagnosises.params[].isMandatory| Boolean | Whether or not the parameter is mandatory. |
|diagnosises.params[].canMultiChoice| Boolean | Whether or not the parameter is allowed to be chosen from a multi-choice array. |
|diagnosises.params[].dataScope| Array | An array of strings that indicate the options of a parameter. |

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

def GetTriggerDiagDef(endpoint, API_Body):
    API_URL = r"/V1/TAF/ManuallyDiagnosis"
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
    "type":1,
    "option":{}
}

headers = {
    "Accepted":"application/json",
    "Content-Type":"application/json"
}

token = getTokens(nb_endpoint, nb_username, nb_password)
headers["token"] = token

print(GetTriggerDiagDef(nb_endpoint, api_body))
```

    {'diagnosises': [{'id': '57672924-8460-1f7e-c1e0-043544e2c42d', 'name': 'BGP self-service', 'params': [{'name': 'NIDevice', 'prompt': 'Device', 'hint': 'Input device name, like R1', 'allowInput': True, 'isMandatory': True, 'canMultiChoice': False, 'dataScope': []}]}, {'id': 'c1a91439-5a12-7bda-9dd8-8a37eb2f44bd', 'name': 'Diag-020 - Self Verify CPU Utilization (TOR Voice)', 'params': [{'name': 'NITag', 'prompt': 'Application Name', 'hint': 'Select application', 'allowInput': True, 'isMandatory': True, 'canMultiChoice': True, 'dataScope': ['TOR Voice']}]}, {'id': '79756585-4d0f-ac3b-c26e-aab19bf0eaf1', 'name': 'Python Sample', 'params': [{'name': 'NIDevice', 'prompt': 'Device', 'hint': 'Input device name, like R1', 'allowInput': True, 'isMandatory': True, 'canMultiChoice': False, 'dataScope': []}]}, {'id': 'f246fde9-eda0-4bf5-586d-131e9ea00b1d', 'name': 'Trigger_NIC_enable', 'params': [{'name': 'NIDevice', 'prompt': 'Device', 'hint': 'Input device name, like R1', 'allowInput': True, 'isMandatory': True, 'canMultiChoice': False, 'dataScope': []}]}, {'id': '6be3fea7-59b0-a5f5-57b4-26788395630f', 'name': 'Check CRC error for a device', 'params': [{'name': 'NIDevice', 'prompt': 'Device', 'hint': 'Input device name, like R1', 'allowInput': True, 'isMandatory': True, 'canMultiChoice': False, 'dataScope': []}]}, {'id': '7a323a0d-c80c-ffe2-1d21-a3a1cfe6a144', 'name': 'Verify MTU Mismatch', 'params': [{'name': 'NIDevice', 'prompt': 'Device', 'hint': 'Input device name, like R1', 'allowInput': True, 'isMandatory': True, 'canMultiChoice': False, 'dataScope': []}]}], 'statusCode': 790200, 'statusDescription': 'Success.'}
    

## Formatted Sample JSON Response


```python
{
  "diagnosises": [
    {
      "id": "7a323a0d-c80c-ffe2-1d21-a3a1cfe6a144",
      "name": "Verify MTU Mismatch",
      "params": [
        {
          "name": "NIDevice",
          "prompt": "Device",
          "hint": "Input device name, like R1",
          "allowInput": true,
          "isMandatory": true,
          "canMultiChoice": false,
          "dataScope": []
        }
      ]
    },
    {
      "id": "57672924-8460-1f7e-c1e0-043544e2c42d",
      "name": "BGP self-service",
      "params": [
        {
          "name": "NIDevice",
          "prompt": "Device",
          "hint": "Input device name, like R1",
          "allowInput": true,
          "isMandatory": true,
          "canMultiChoice": false,
          "dataScope": []
        }
      ]
    },
    {
      "id": "f246fde9-eda0-4bf5-586d-131e9ea00b1d",
      "name": "Trigger_NIC_enable",
      "params": [
        {
          "name": "NIDevice",
          "prompt": "Device",
          "hint": "Input device name, like R1",
          "allowInput": true,
          "isMandatory": true,
          "canMultiChoice": false,
          "dataScope": []
        }
      ]
    },
    {
      "id": "c1a91439-5a12-7bda-9dd8-8a37eb2f44bd",
      "name": "Diag-020 - Self Verify CPU Utilization (TOR Voice)",
      "params": [
        {
          "name": "NITag",
          "prompt": "Application Name",
          "hint": "Select application",
          "allowInput": true,
          "isMandatory": true,
          "canMultiChoice": true,
          "dataScope": [
            "TOR Voice"
          ]
        }
      ]
    },
    {
      "id": "6be3fea7-59b0-a5f5-57b4-26788395630f",
      "name": "Check CRC error for a device",
      "params": [
        {
          "name": "NIDevice",
          "prompt": "Device",
          "hint": "Input device name, like R1",
          "allowInput": true,
          "isMandatory": true,
          "canMultiChoice": false,
          "dataScope": []
        }
      ]
    },
    {
      "id": "79756585-4d0f-ac3b-c26e-aab19bf0eaf1",
      "name": "Python Sample",
      "params": [
        {
          "name": "NIDevice",
          "prompt": "Device",
          "hint": "Input device name, like R1",
          "allowInput": true,
          "isMandatory": true,
          "canMultiChoice": false,
          "dataScope": []
        }
      ]
    }
  ],
  "statusCode": 790200,
  "statusDescription": "Success."
}
```
