
# Device API Design

## ***POST*** /V1/CMDB/Devices/Attributes	
Call this API to create a customized attribute for certain device types. 

User can use the SetDeviceAttribute API to set a value for the created attribute.

## Detail Information

> **Title** : Create Device Attribute API<br>

> **Version** : 01/25/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Devices/Attributes

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|attributeName* | string  | The name of the attribute.  |
|attributeDisplayName* | string | The display name of the attribute in <i>Device Details</i> of NetBrain IE system. |
|deviceTypeNames | list | Specify the list of device types in which the created attribute would apply to. <br>When it is set to an empty list `[]`, the new device attribute will apply to all device types. <br>The value of this parameter corresponds to Device Type under <i>Multi-Vendor Support</i> in <i>Tenant Management</i>. |
|dataType* | string/double/int/bool/list/table/time/mac  | The supported data types of the attribute.  |
|subDataType | string | This parameter is only available for `list` type property.<br> The data type of each value in a list type property. |
|columns | list of objects | This parameter is only available for `table` type property.<br>▪ `name`(string) - the sub property name (displayed as a column header).<br>▪ `displayName`(string) - the display name (alias) of the sub property (can be null).<br>▪ `dataType`(string) - the data type of the sub property.<br>▪ `isKey` (bool) - control whether to use the sub property as the key when comparing the table type property. The default value is False. |
|isFullSearch* | bool | Set whether to use the property as an index in full scope search, including extended search and default search.  |

> ***Example***


```python
body = {
          "attributeName": "newAttribute",
          "attributeDisplayName": "New Attribute",
          "deviceTypeNames": [],
          "dataType": "string",
          "isFullSearch": True
        }
```

## Parameters(****required***)

> No Parameters Required.

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

> ***Example***


```python
{
    "statusCode": 790200,
    "statusDescription": "Success."
}
```

# Full Example

## Example 1: Successful API Call for `string` type Device Attribute
```python
# import python modules 
import requests
import time
import urllib3
import pprint
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the request inputs
token = "855b2da0-306b-4c29-b37f-be09e33e2d02"
nb_url = "http://192.168.28.79"

# Create device attribute
attributeName = "newAttribute1"
attributeDisplayName = "New Attribute1"
deviceTypeNames = []
dataType = "string"
isFullSearch = True

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"]=token
full_url= nb_url + "/ServicesAPI/API/V1/CMDB/Devices/Attributes"

body={
        "attributeName": attributeName,
        "attributeDisplayName": attributeDisplayName,
        "deviceTypeNames": deviceTypeNames, 
        "dataType": dataType,
        "isFullSearch": isFullSearch
    }

try:
    response = requests.post(full_url, data=json.dumps(body), headers=headers, verify=False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Failed to Create Device Attribute! - " + str(response.text))
    
except Exception as e:
    print (str(e))    
```
```python
    {'statusCode': 790200, 'statusDescription': 'Success.'}
```

## Example 2: Successful API Call for `table` type Device Attribute
```python
attributeName = "newAttribute2"
attributeDisplayName = "New Attribute2"
deviceTypeNames = []
dataType = "table"
isFullSearch = True
columns = [
    {
        "name":"column1",
        "displayName":"CO1",
        "dataType":"string"
    }
]

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"]=token
full_url= nb_url + "/ServicesAPI/API/V1/CMDB/Devices/Attributes"

body={
        "attributeName": attributeName,
        "attributeDisplayName": attributeDisplayName,
        "deviceTypeNames": deviceTypeNames, 
        "dataType": dataType,
        "isFullSearch": isFullSearch,
        "columns": columns
    }

try:
    response = requests.post(full_url, data=json.dumps(body), headers=headers, verify=False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Failed to Create Device Attribute! - " + str(response.text))
    
except Exception as e:
    print (str(e))    

```

```python
    {'statusCode': 790200, 'statusDescription': 'Success.'}
```

# cURL Code from Postman

```python
curl -X POST \
  http://192.168.28.79/ServicesAPI/API/V1/CMDB/Devices/Attributes \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: acd1f616-72f5-49a9-82be-3f1b7d2f82de' \
  -H 'cache-control: no-cache' \
  -H 'token: e074d192-3f21-4ae8-b5f1-405d240b65ca' \
  -d '{
        "attributeName": "attributeName",
        "attributeDisplayName": "attributeDisplayName",
        "deviceTypeNames": "null", 
        "dataType": "string",
        "isFullSearch": true
      }'
```

# Error Examples:

## Error Example 1: Insufficient Privilege
```python
{
    "statusCode":795003,
    "statusDescription":"Insufficient permissions: the current user has insufficient permissions to perform the requested operation. The user has no tenant or domain access permission.sharePolicyManagement"
}
```

## Error Example 2: One or More Required Body Parameters are Empty
```python
Input:
    attributeName = "" # empty required body parameters
    attributeDisplayName = "New Attribute"
    deviceTypeNames = "" # empty required body parameters
    dataType = "string"
    isFullSearch = True
    
Response:
    "Create device attribute failed! - 
        {
            "statusCode":791000,
            "statusDescription":"Null parameter: the parameter 'attributeName' cannot be null."
        }"
```
## Error Example 3: Duplicate Attribute Name
```python
Input:
    attributeName = "newAttribute" # attribute name newAttribute already exista.
    attributeDisplayName = "New Attribute"
    deviceTypeNames = "null" 
    dataType = "string"
    isFullSearch = True
    
Response:
    "Create device attribute failed! - 
        {
            "statusCode":791007,
            "statusDescription":"attribute newAttribute already exists."
        }"
```