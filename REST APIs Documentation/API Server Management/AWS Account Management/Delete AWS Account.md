
# AWS Account Management Design

## ***DELETE*** /V1/CMDB/ApiServers/AWSAccounts/{id}
Using this API call to delete an AWS account in API Server Manager.

## Detail Information

> **Title** : Delete AWS Account API<br>

> **Version** : 03/09/2022

> **API Server URL** : http(s):// IP address of your NetBrain Web API Server /ServicesAPI/V1/CMDB/ApiServers/AWSAccounts/{id}

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
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code. |

> ***Example***
```python
{
    "statusCode": 790200,
    "statusDescription": "Success."
}

```
## Response Codes
|**Code**|**Message**|**Description**|
|------|------|------|
| 790200 | OK |  |
| 793404 | NotFound | not found|

# Full Example :

> ***Example***

```python
# import python modules 
import requests
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the request inputs
token = "3a7b2475-70f7-4a60-953c-c69626772959"
api_Server_id = "426c1589-6d04-438a-bd1a-1c1b9fdbf871"
full_url = "https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/ApiServers/AWSAccounts/" + api_Server_id
# Set proper headers
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token
try:
    # Do the HTTP request
    response = requests.delete(full_url, headers=headers, verify=False)
    # Check for HTTP codes other than 200
    if response.status_code == 200:
        # Decode the JSON response into a dictionary and use the data
        result = response.json()
        print (result)
    else:
        print ("Delete AWS account failed! - " + str(response.text))

except Exception as e: print (str(e))

```
	{'statusCode': 790200, 'statusDescription': 'Success.'}

# cURL Code from Postman
```python
curl --location --request DELETE 'https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/ApiServers/AWSAccounts/b772762a-95a4-443b-863b-13207ec85113' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'token: 3a7b2475-70f7-4a60-953c-c69626772959'
```
