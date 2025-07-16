
# Device Group API Design

## ***POST*** /V1/CMDB/DeviceGroups
This API is used to add (create) a device group to the specified path.

## Detail Information

> **Title** : Add Device Group API<br>

> **Version** : 03/08/2022

> **API Server URL** : http(s):// IP address of your NetBrain Web API Server/ServicesAPI/API/V1/CMDB/DeviceGroups

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|name* | string  | The full path of a device group. This parameter is required.  |
|type  | string  | This parameter is only required when full path is not provided in name, and the name is a group name only instead of a group path. The type of device group - private/public/policy. This parameter is required.  |
|description | string  | The description of the task. This field is optional.  |


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
|deviceGroupID| string | The ID of device group |
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code. |


# Full Example :

> ***Example 1***
```python
# import python modules 
import requests
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the request inputs
token = "609299f6-abbe-4a8c-a9ff-deb6a69451c2"
full_url = "https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/DeviceGroups"
body = {
    "name": "Test Device Group",
    "type":"public",
    "description": "This is a test Device Group for API call"
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
        print ("Failed to Create a Device Group! - " + str(response.text))

except Exception as e: print (str(e))
```

> ***Example 2***
```python
# import python modules 
import requests
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the request inputs
token = "609299f6-abbe-4a8c-a9ff-deb6a69451c2"
full_url = "https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/DeviceGroups"
body = {
    "name": "Shared Device Groups/Test Device Group2",
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
        print ("Failed to Create a Device Group! - " + str(response.text))

except Exception as e: print (str(e))

```

# cURL Code from Postman
```python
curl --location --request POST 'https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/DeviceGroups' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'token: 609299f6-abbe-4a8c-a9ff-deb6a69451c2' \
--data-raw '{
    "name":"Shared Device Groups/Test Device Group"  
}
'
```
# Error Examples
## Error Example 1: Null parameter - parameter {} cannot be null
```
Input:
    "name": "",
    "type": "policy"
    
Response:
    "Parameter cannot be null - 
        {
            "statusCode":791000,
            "statusDescription":"Null parameter: the parameter '{}' cannot be null."
        }"
```
## Error Example 2: Device Group: {}, Type: {} Already Exists.
```
Input:
    "name":"Shared Device Groups/Test Device Group",
    "type": "policy"
    
Response:
    "Device Group already exists! - 
        {
            "statusCode":791007,
            "statusDescription":"device group: Test Device Group, location in name: Shared Device Groups already exists."
        }"
```
## Error Example 3: You are not allowed to perform this operation
```
Input:
    User does not have the privilege to make changes to shared device groups.
    
Response:
    Failed to Create a Device Group! - {"statusCode":799001,"statusDescription":"You are not allowed to perform the operation."}
```