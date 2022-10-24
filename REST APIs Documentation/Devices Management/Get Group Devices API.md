
# Device API Design

## ***GET*** /V1/CMDB/Devices/GroupDevices
Call this API to get all devices from a device group.

## Detail Information

> **Title** : Get Group Devices API<br>

> **Version** : 03/18/2022

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Devices/GroupDevices

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Body Parameters(****required***)

> No request body.

## Path Parameters(****required***)

> No parameter required.

## Query Parameters(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
| path | string  | Full path of a specific device group |

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
|devices| string[] | A list of devices. |
|devices.id | string | The device ID. |
|devices.mgmtIP| string | The management IP address of the returned device. |
|devices.hostname| string | The hostname of returned device. |


> ***Example***



```python
# Successful response with groupPath = "Shared Device Groups/NICUseCaseTrain/training_case4_check_eigrp_interface_hello_timer_mismatch"

{
    "devices": [
        {
            "id": "10fcca98-610b-48c3-b380-335f7cc83a78",
            "mgmtIP": "10.20.0.82",
            "hostname": "EIGRP-R13-C3725"
        },
        {
            "id": "1ac62c06-5046-480f-a824-c2627506b332",
            "mgmtIP": "10.20.0.21",
            "hostname": "EIGRP-R1"
        },
        {
            "id": "623efdc7-fbc9-4dfa-9bf7-99e29464e8c8",
            "mgmtIP": "10.20.0.14",
            "hostname": "EIGRP-R3"
        },
        {
            "id": "71892107-bc65-490c-b54f-f4d50c7314ce",
            "mgmtIP": "10.20.0.17",
            "hostname": "EIGRP-R2"
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
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the request inputs
token = "9670caa0-ec51-4fb8-89f8-b3f94c60372d"
full_url = "https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/Devices/GroupDevices"
data = {
    "path": "Shared Device Groups/NICUseCaseTrain/training_case4_check_eigrp_interface_hello_timer_mismatch"
}
# Set proper headers
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token
try:
    # Do the HTTP request
    response = requests.get(full_url, params = data, headers=headers, verify=False)
    # Check for HTTP codes other than 200
    if response.status_code == 200:
        # Decode the JSON response into a dictionary and use the data
        result = response.json()
        print (result)
    else:
        print ("Get devices from a device group failed- " + str(response.text))

except Exception as e: print (str(e))

```
	{'devices': [{'id': '10fcca98-610b-48c3-b380-335f7cc83a78', 'mgmtIP': '10.20.0.82', 'hostname': 'EIGRP-R13-C3725'}, {'id': '1ac62c06-5046-480f-a824-c2627506b332', 'mgmtIP': '10.20.0.21', 'hostname': 'EIGRP-R1'}, {'id': '623efdc7-fbc9-4dfa-9bf7-99e29464e8c8', 'mgmtIP': '10.20.0.14', 'hostname': 'EIGRP-R3'}, {'id': '71892107-bc65-490c-b54f-f4d50c7314ce', 'mgmtIP': '10.20.0.17', 'hostname': 'EIGRP-R2'}], 'statusCode': 790200, 'statusDescription': 'Success.'}

# cURL Code from Postman
```python
curl --location --request GET 'https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/Devices/GroupDevices?path=Shared Device Groups/NICUseCaseTrain/training_case4_check_eigrp_interface_hello_timer_mismatch' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'token: 9670caa0-ec51-4fb8-89f8-b3f94c60372d' \
--data-raw ''
```


