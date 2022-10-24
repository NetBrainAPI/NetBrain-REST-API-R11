
# AWS Account Management Design

## ***GET*** /V1/CMDB/ApiServers/AWSAccounts
Using this API call to get AWS accounts in API Server Manager. The encrypted field are not returned.

## Detail Information

> **Title** : Get AWS Accounts API<br>

> **Version** : 03/09/2022

> **API Server URL** : http(s):// IP address of your NetBrain Web API Server /ServicesAPI/V1/CMDB/ApiServers/AWSAccounts

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

> No parameters required.

## Parameters(****required***)  
|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|accountId|string|The account ID(Endpoint) of AWS |
|name|string|API Server Name |

> **Note** : The API call will return all AWS accounts if not specify any accountId or name in parameters. If both parameters are provided in the request, NetBrain primarily picks accountId.

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

> ***Example***
```python
{
    "accounts": [
        {
            "id": "c21dfe6a-34b1-4501-b1db-9ee6d90630e4",
            "accountId": "123456789",
            "name": "AWS API TEST3",
            "desc": "Test API call",
            "frontServerAndGroupId": "netbrainfs",
            "AccessMethod": "RoleBased",
            "RoleName": "AccessByMonitorAccount",
            "ExternalId": "ExternalIdSample",
            "SessionName": "NetbrainMonitor"
        },
        {
            "id": "fdf263b5-701e-4312-857d-e3e55b0305ea",
            "accountId": "987654321",
            "name": "AWS API Account",
            "desc": "own by dev team",
            "frontServerAndGroupId": "netbrainfs",
            "AccessMethod": "KeyBased",
            "AWS_SERVER_PUBLIC_KEY": "AAAAAAAAAAAAAAAAAAA"
        }
    ],
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
token = "b0049a91-5d6f-4f8d-9bde-43270d9678c7"
full_url = "https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/ApiServers/AWSAccounts"
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
        print ("Get AWS accounts failed! - " + str(response.text))

except Exception as e: print (str(e))
```
	{'accounts': [{'id': 'c21dfe6a-34b1-4501-b1db-9ee6d90630e4', 'accountId': '44444', 'name': 'AWS API TEST3', 'desc': 'Test API call', 'frontServerAndGroupId': 'netbrainfs', 'AccessMethod': 'RoleBased', 'RoleName': 'AccessByMonitorAccount', 'ExternalId': 'ExternalIdSample', 'SessionName': 'NetbrainMonitor'}, {'id': 'fdf263b5-701e-4312-857d-e3e55b0305ea', 'accountId': '111111111', 'name': 'AWS API Account', 'desc': 'own by dev team', 'frontServerAndGroupId': 'netbrainfs', 'AccessMethod': 'KeyBased', 'AWS_SERVER_PUBLIC_KEY': 'AAAAAAAAAAAAAAAAAAA'}], 'statusCode': 790200, 'statusDescription': 'Success.'}

# cURL Code from Postman
```python
curl --location --request GET 'https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/ApiServers/AWSAccounts' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'token: b0049a91-5d6f-4f8d-9bde-43270d9678c7'
```
