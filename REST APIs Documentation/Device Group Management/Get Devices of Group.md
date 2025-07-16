
# Device Group API Design

## ***GET*** /V1/CMDB/DeviceGroups/{deviceGroupID}/devices
This API is used to get devices from a device group.<br>
The `deviceGroupID` used to call this API can be retrieved from [Get Device Group API](https://github.com/NetBrainAPI/NetBrain-REST-API-R12.1/blob/main/REST%20APIs%20Documentation/Device%20Group%20Management/Get%20Device%20Group%20API.md)

## Detail Information

> **Title** : Get devices of Device Group API<br>

> **Version** : 10/08/2019.

> **API Server URL** : http(s):// IP address of your NetBrain Web API Server /ServicesAPI/API/V1//CMDB/DeviceGroups/{deviceGroupID}/devices

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

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
|devices| string[] | Device name list |
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code. |


> ***Example***


```python
{
    'devices': ['Bos-Core-6500', 'CA-YVR-R1', 'CA-YVR-R2', 'NBLAB-IOS-CE1', 'bjta002114-SW7', 'bjta002115-SW6', 'bjta002303-SW9', 'bjta002444-SW13'], 'statusCode': 790200, 'statusDescription': 'Success.'
}
```

# Full Example :


```python
# import python modules 
import requests
import time
import urllib3
import pprint
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the request inputs
token = "ad3c616e-5f3d-45e9-9ba1-bb71f003a098"
deviceGroupID = '9732dca7-9709-4c49-91e1-a2310b8364d9' # get from Get Device Group API 
nb_url = "http://192.168.28.143"
full_url = nb_url + "/ServicesAPI/API/V1/CMDB/DeviceGroups/"+deviceGroupID+"/devices"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

try:
    response = requests.get(full_url, headers = headers, verify = False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Failed to Get Devices from the Device Group! - " + str(response.text))
    
except Exception as e:
    print (str(e)) 

```
```
{'statusCode': 790200, 'statusDescription': 'Success.'}
``` 

# cURL Code from Postman


```python
curl -X GET \
  http://192.168.28.143/ServicesAPI/API/V1/CMDB/DeviceGroups/9732dca7-9709-4c49-91e1-a2310b8364d9/devices \
  -H 'accept: application/json' \
  -H 'content-type: application/json' \
  -H 'token: ad3c616e-5f3d-45e9-9ba1-bb71f003a098' \
}'
```

# Error Examples
## Error Example 1: You are not allowed to perform this operation
```
Input:
    User does not have the privilege to make changes to shared device groups.
    
Response:
    "Failed to Get Devices from the Device Group! - 
    {
        "statusCode":799001,
        "statusDescription":"You are not allowed to perform the operation."
    }"
```
