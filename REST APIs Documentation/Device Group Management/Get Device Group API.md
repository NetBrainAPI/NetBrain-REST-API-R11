
# Device API Design

## ***GET*** /V1/CMDB/DeviceGroups
This API is used to get device groups information. <br>
Calling this API returns `id` of each devices. These `id` can be used as `deviceGroupID` as a crucial parameter used to call other APIs such as [Get Devices of Group](https://github.com/NetBrainAPI/NetBrain-REST-API-R12.1/blob/main/REST%20APIs%20Documentation/Device%20Group%20Management/Get%20Devices%20of%20Group.md), [Add Devices to Group](https://github.com/NetBrainAPI/NetBrain-REST-API-R12.1/blob/main/REST%20APIs%20Documentation/Device%20Group%20Management/Add%20Devices%20to%20Group.md), [Delete Devices from Group](https://github.com/NetBrainAPI/NetBrain-REST-API-R12.1/blob/main/REST%20APIs%20Documentation/Device%20Group%20Management/Delete%20Devices%20from%20Group.md), etc.
## Detail Information

> **Title** : Get Device Groups API<br>

> **Version** : 03/07/2022

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/DeviceGroups

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

> No request body.

## Path Parameters(****required***)

> No parameters required.

## Query Parameters(****required***)

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
|statusCode| integer | Code issued by NetBrain server indicating the execution result.  |
|statusDescription| string | The explanation of the status code. |
|id| string | The ID of the device group. <br>Use this ID as `deviceGroupID` to call other `Device Group Management APIs`. |
|name| string | The full path of the device group. |
|type | integer | The type of device group<br>`0`: Public group<br>`1`: Private group<br>`2`: System group<br>`4`: Policy device group|

> ***Example***
```python
{
    "deviceGroups": [
        {
            "id": "d6fb1de4-f092-41dd-a8f7-80832b4b253d",
            "name": "System Device Groups/#BGP 12076",
            "type": 2
        },
        {
            "id": "f6dfac40-ea61-4cf1-9f46-777bb5cfec03",
            "name": "System Device Groups/#BGP 64515",
            "type": 2
        },
        {
            "id": "56c1f8a6-9762-062c-3e99-8055f969e4ae",
            "name": "Shared Device Groups/Test for Demo",
            "type": 0
        },
        {
            "id": "6b4fe54d-28be-bed9-daf9-65144861ef6e",
            "name": "Shared Device Groups/NICUseCaseTrain/training_case2_check_ospf_neighbor_interface_cost_mismatch",
            "type": 0
        },
        {
            "id": "907691ce-09e8-19cb-7b3e-f47b74152f44",
            "name": "Shared Device Groups/NICUseCaseTrain/training_case3_check_ibgp_reflector_and_clients_connectivity",
            "type": 0
        },
        {
            "id": "c3a81388-18d3-4be0-91f4-de6ea9b38596",
            "name": "System Device Groups/#Device Per Driver",
            "type": 2
        }
    ],
    "statusCode": 790200,
    "statusDescription": "Success."
}
```
# Full Example
```python
# import python modules 
import requests
import json

# Set the request inputs
token = "1f93390b-9b11-41b5-9d89-3fc0b1e8af10"
full_url = "https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/DeviceGroups"

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
        print ("Get Device Groups failed! - " + str(response.text))

except Exception as e: print (str(e))
```

# cURL Code from Postman
```python
curl --location --request GET 'https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/DeviceGroups' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'token: 0f93390b-9b11-41b5-9d89-3fc0b1e8af10' \
--data-raw ''
```

