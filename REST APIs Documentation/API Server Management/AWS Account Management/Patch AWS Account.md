
# AWS Account Management Design

## ***PATCH*** /V1/CMDB/ApiServers/AWSAccounts
Using this API call to update credential for an AWS account in API Server Manager.

## Detail Information

> **Title** : Patch AWS Account API<br>

> **Version** : 03/10/2022

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
|id* | string  |  The API server id |
|AWS_SERVER_PUBLIC_KEY*|string|Access Key ID. This is required parameter if no input on AWS_SERVER_SECRET_KEY.|
|AWS_SERVER_SECRET_KEY*|string|Secret Access Key. This is required parameter if no input on AWS_SERVER_PUBLIC_KEY.|

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
	'statusCode': 790200, 
	'statusDescription': 'Success.'
}

```
## Response Codes
|**Code**|**Message**|**Description**|
|------|------|------|
| 790200 | OK |  |
| 791000 | ParameterNull | API Server id is missing|
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
body = {
    "id": "c21dfe6a-34b1-4501-b1db-9ee6d90630e4",
    "AWS_SERVER_PUBLIC_KEY":"abcd",
    "AWS_SERVER_SECRET_KEY":"686768768786"
}
# Set proper headers
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token
try:
    # Do the HTTP request
    response = requests.patch(full_url, data = json.dumps(body), headers=headers, verify=False)
    # Check for HTTP codes other than 200
    if response.status_code == 200:
        # Decode the JSON response into a dictionary and use the data
        result = response.json()
        print (result)
    else:
        print ("Patch AWS accounts failed! - " + str(response.text))

except Exception as e: print (str(e))

```
	{'statusCode': 790200, 'statusDescription': 'Success.'}

# cURL Code from Postman
```python
curl --location --request PATCH 'https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/ApiServers/AWSAccounts' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'token: 3a7b2475-70f7-4a60-953c-c69626772959' \
--data-raw '{
    "id": "c21dfe6a-34b1-4501-b1db-9ee6d90630e4",
    "AWS_SERVER_PUBLIC_KEY":"abcd",
    "AWS_SERVER_SECRET_KEY":"686768768786"
}'
```
