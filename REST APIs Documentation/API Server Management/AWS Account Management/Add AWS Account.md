
# AWS Account Management Design

## ***POST*** /V1/CMDB/ApiServers/AWSAccounts
Using this API call to add an AWS account in API Server Manager.

## Detail Information

> **Title** : Add AWS Account API<br>

> **Version** : 03/09/2022

> **API Server URL** : http(s):// IP address of your NetBrain Web API Server /ServicesAPI/V1/CMDB/ApiServers/AWSAccounts

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|accountId* | string  |  The account ID(Endpoint) of AWS |
|name*|string|API Server Name|
|desc|string|Description of API Server|
|AccessMethod*|string|Access Method of AWS account. The value includes:<br>RoleBased<br>KeyBased|
|AWS_SERVER_PUBLIC_KEY*|string|Access Key ID. This is required parameter under KeyBased Access Method|
|AWS_SERVER_SECRET_KEY*|string|Secret Access Key. This is required parameter under KeyBased Access Method|
|RoleName*|string|Role Name. This is required parameter under RoleBased Access Method|
|ExternalId*|string|External ID. This is required parameter under RoleBased Access Method|
|SessionName|string|Session Name|
|frontServerAndGroupId*|string|Front Server name|

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
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code. |

> ***Example***
```python
{
    "id": "b9283db4-6ce1-4fa8-9f5c-b926fbbe9bef",
    "statusCode": 790200,
    "statusDescription": "Success."
}

```
## Response Codes
|**Code**|**Message**|**Description**|
|------|------|------|
| 790200 | OK |  |
| 791000 | ParameterNull | account id is missing<br>name is missing<br>frontServerAndGroupId is missing|
| 791007 | ExistedDataInSystem | accound id already exists in system<br> name already exists in system|

# Full Example :

> ***Example 1***

```python
# import python modules 
import requests
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the request inputs
token = "3a7b2475-70f7-4a60-953c-c69626772959"
full_url = "https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/ApiServers/AWSAccounts"
body = {
    "accountId": "111111111111",
    "name": "AWS API TEST",
    "desc": "Test API call",
    "AccessMethod": "KeyBased",
    "AWS_SERVER_PUBLIC_KEY": "AAAAAAAAAAAAAAAAAAA",
    "AWS_SERVER_SECRET_KEY": "BBBBBBBBBBBBBBBBBBB",
    "frontServerAndGroupId": "netbrainfs"
}
# Set proper headers
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token
try:
    # Do the HTTP request
    response = requests.post(full_url, data = json.dumps(body), headers=headers, verify=False)
    # Check for HTTP codes other than 200
    if response.status_code == 200:
        # Decode the JSON response into a dictionary and use the data
        result = response.json()
        print (result)
    else:
        print ("Add AWS account failed! - " + str(response.text))

except Exception as e: print (str(e))
```
	{'id': 'e534ab19-cc60-43af-8cc4-7150e8d9e544', 'statusCode': 790200, 'statusDescription': 'Success.'}
	
> ***Example 2***
```python
# import python modules 
import requests
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the request inputs
token = "3a7b2475-70f7-4a60-953c-c69626772959"
full_url = "https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/ApiServers/AWSAccounts"
body = {
    "accountId": "22222222222222",
    "name": "AWS API TEST6",
    "desc": "Test API call",
    "AccessMethod": "RoleBased",
    "RoleName": "AccessByMonitorAccount",
    "ExternalId": "ExternalIdSample",
    "SessionName": "NetbrainMonitor",
    "frontServerAndGroupId": "netbrainfs"

}
# Set proper headers
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token
try:
    # Do the HTTP request
    response = requests.post(full_url, data = json.dumps(body), headers=headers, verify=False)
    # Check for HTTP codes other than 200
    if response.status_code == 200:
        # Decode the JSON response into a dictionary and use the data
        result = response.json()
        print (result)
    else:
        print ("Add AWS account failed! - " + str(response.text))

except Exception as e: print (str(e))
```
	{'id': 'f434ab19-cc60-43af-8cc4-7150e8d9e565', 'statusCode': 790200, 'statusDescription': 'Success.'}

# cURL Code from Postman
```python
curl --location --request POST 'https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/ApiServers/AWSAccounts' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'token: 3a7b2475-70f7-4a60-953c-c69626772959' \
--data-raw '{
    "accountId": "22222222222222",
    "name": "AWS API TEST6",
    "desc": "Test API call",
    "AccessMethod": "RoleBased",
    "RoleName": "AccessByMonitorAccount",
    "ExternalId": "ExternalIdSample",
    "SessionName": "NetbrainMonitor",
    "frontServerAndGroupId": "netbrainfs"

}'
```
