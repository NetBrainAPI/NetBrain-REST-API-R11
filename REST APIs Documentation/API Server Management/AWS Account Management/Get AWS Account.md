
# AWS Account Management Design

## ***GET*** /V1/CMDB/ApiServers/AWSAccounts/{id}
Using this API call to get an AWS account in API Server Manager. The encrypted field are not returned.

## Detail Information

> **Title** : Get AWS Account API<br>

> **Version** : 03/09/2022

> **API Server URL** : http(s):// IP address of your NetBrain Web API Server /ServicesAPI/API/V1/CMDB/ApiServers/AWSAccounts/{id}

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

> No parameters required.

## Parameters(****required***)

> No parameters required.

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
|id| string | The API Server ID.|
|accountId | string  |  The account ID(Endpoint) of AWS |
|name|string|API Server Name|
|desc|string|Description of API Server|
|AccessMethod|string|Access Method of AWS account.|
|AWS_SERVER_PUBLIC_KEY|string|Access Key ID.|
|RoleName|string|Role Name.|
|ExternalId|string|External ID.|
|SessionName|string|Session Name|
|frontServerAndGroupId|string|Front Server name|
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code. |

> ***Example1***
```python
{
    "account": {
        "id": "fdf263b5-701e-4312-857d-e3e55b0305ea",
        "accountId": "111111111",
        "name": "AWS API Account",
        "desc": "own by dev team",
        "frontServerAndGroupId": "netbrainfs",
        "AccessMethod": "KeyBased",
        "AWS_SERVER_PUBLIC_KEY": "AAAAAAAAAAAAAAAAAAA"
    },
    "statusCode": 790200,
    "statusDescription": "Success."
}

```

> ***Example2***
```python
{
    "account": {
        "id": "c21dfe6a-34b1-4501-b1db-9ee6d90630e4",
        "accountId": "44444",
        "name": "AWS API TEST3",
        "desc": "Test API call",
        "frontServerAndGroupId": "netbrainfs",
        "AccessMethod": "RoleBased",
        "RoleName": "AccessByMonitorAccount",
        "ExternalId": "ExternalIdSample",
        "SessionName": "NetbrainMonitor"
    },
    "statusCode": 790200,
    "statusDescription": "Success."
}
```
## Response Codes
|**Code**|**Message**|**Description**|
|------|------|------|
| 790200 | OK |  |
| 793404 | NotFound | Not found|

# Full Example :
```python
# import python modules 
import requests
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the request inputs
token = "3a7b2475-70f7-4a60-953c-c69626772959"
api_Server_id = "c21dfe6a-34b1-4501-b1db-9ee6d90630e4"
full_url = "https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/ApiServers/AWSAccounts/" + api_Server_id
# Set proper headers
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token
try:
    # Do the HTTP request
    response = requests.get(full_url, headers=headers, verify=False)
    # Check for HTTP codes other than 200
    if response.status_code == 200:
        # Decode the JSON response into a dictionary and use the data
        result = response.json()
        print (result)
    else:
        print ("Get AWS account failed! - " + str(response.text))

except Exception as e: print (str(e))
```
	{'account': {'id': 'c21dfe6a-34b1-4501-b1db-9ee6d90630e4', 'accountId': '44444', 'name': 'AWS API TEST3', 'desc': 'Test API call', 'frontServerAndGroupId': 'netbrainfs', 'AccessMethod': 'RoleBased', 'RoleName': 'AccessByMonitorAccount', 'ExternalId': 'ExternalIdSample', 'SessionName': 'NetbrainMonitor'}, 'statusCode': 790200, 'statusDescription': 'Success.'}

# cURL Code from Postman
```python
curl --location --request GET 'https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/ApiServers/AWSAccounts/c21dfe6a-34b1-4501-b1db-9ee6d90630e4' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'token: 3a7b2475-70f7-4a60-953c-c69626772959'
```
