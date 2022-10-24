
# Benchmark API Design

## ***POST*** /V1/CMDB/Benchmark/Result/DeviceList
Use this API to get device name list for benchmark run result.

## Detail Information

> **Title** : Get Benchmark Run Result Device List by Filter API<br>

> **Version** : 05/16/2022.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Benchmark/Result/DeviceList

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|task | string  | The name of the task.  |
|RunId | string  | optional, ID of the execution. If null, the API will return last run result  |
|filterBy | int  | Filter of the device list. Default value is 0. <br>Possible values:<br>0: all deivces<br>1: retrieval failure devices<br>2: config retrieval failure devices<br>3: hostname changed devices  |
|includeDeviceGroup | string  | Full path of the device group  |
|excludeDeviceGroup | string  | Full path of the device group  |

> includeDeviceGroup and excludeDeviceGroup is mutually exclusive.

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
|devices| list of Strings | List of device name   |

> ***Example***


```python
{
    "devices": [
      "US-BOS-R1",
      "US-BOS-R2",
      "US-BOS-SW1",
      "US-BOS-SW2"
  ],
    "statusCode": 790200,
    "statusDescription": "Success."
}
```

# Full Example:


```python
# import python modules 
import requests
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the request inputs

url = "https://192.168.28.79/ServicesAPI/API/V1/CMDB/Benchmark/Result/DeviceList"

payload = json.dumps({
  "task": "Basic System Benchmark",
  "runId": ""
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'token': '7ff6218c-6583-459c-87cd-6da5d90252ea'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```    

# cURL Code from Postman


```python
curl --location --request POST 'https://192.168.28.79/ServicesAPI/API/V1/CMDB/Benchmark/Result/DeviceList' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'token: 7ff6218c-6583-459c-87cd-6da5d90252ea' \
--data-raw '{
  "task": "Basic System Benchmark",
  "runId":""
}'
```

# Error Examples:


```python

```
