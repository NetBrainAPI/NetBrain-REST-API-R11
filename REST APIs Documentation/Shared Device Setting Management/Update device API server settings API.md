Shared Device Setting REST API Design 
==========================

## PUT /ServicesAPI/API/V1/CMDB/SharedDeviceSettings/APIServerSetting

This API is used to update device API server settings in current domain. The response of this API will return a list in JSON format.<br>

## Detail Information

>**Title:** Update device API server settings API

>**Version:** 03/8/2020

>**API Server URL:** http(s)://IP Address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/SharedDeviceSettings/APIServerSetting

>**Authentication:**

|**Type**|**In**|**Name**|
|------|------|------|
|Bearer Authentication|Headers|Authentication token|

## Request body (*required)

|**Name**|**Type**|**Description**|
|------|------|------|
|HostName*| string | Device hostname. It is required if no input on ManageIp|
|ManageIp* | string | Device management IP address. It is required if no input on HostName  |
|API_setting| object list | API servers applied to current device. |
|API_setting.API_plugin| string | name of applied API plugin. |
|API_setting.API_server| object | applied API server. |
|API_setting.API_server.name| string | applied API servers name. |

## Headers

>**Data Format Headers**

|**Name**|**Type**|**Description**|
|------|------|------|
|Content-Type|string|support "application/json"|  
|Accept|string|support "application/json"|

>**Authorization Headers**

|**Name**|**Type**|**Description**|
|------|------|------|
|token|string|Authentication token, get from login API.|

***Example***
```python
API Body = {  
        "HostName" : "CP-SW1",
        "ManageIp" : "192.168.0.58",
        "API_setting" : [
                {
                    "API_plugin" : "string",
                    "API_server" : {
                        "name" : "string"/null
                    }     
                },
                {
                    "API_plugin" : "string",
                    "API_server" : {
                        "name" : "string"/null
                    }  
                },
                {
                    "API_plugin" : "string",
                    "API_server" : {
                        "name" : "string"/null
                    }     
                },
                .
                .
                .
          ]
}
```

```python 
{
    "statusCode": 790200,
    "statusDescription": "Success."
}
```
## Response

| Code | Message | Description |
|--------|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 790200 | OK ||
| 794011 | OperationFailed | There is no match hostname or managementip founded.<br>This device is locked, can not be updated.<br>Invalid IP. |
| 791000 | ParameterNull | API Setting is required |
| 793001 | InternalServerError | System framework level error |

 ## Full Example : 
 ```python
 # import python modules 
import requests
import time
import urllib3
import pprint
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the request inputs
token = "609299f6-abbe-4a8c-a9ff-deb6a69451c2"
full_url = "https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/SharedDeviceSettings/APIServerSetting"
body = {
    "HostName": "US-BOS-R1",
    "API_setting":[
        {
            "API_plugin":"ServiceNow API Adapter",
            "API_server":{
                "name":"ServiceNow1750"
            }
        }
    ]
}
# Set proper headers
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token
try:
    # Do the HTTP request
    response = requests.put(full_url, data = json.dumps(body), headers=headers, verify=False)
    # Check for HTTP codes other than 200
    if response.status_code == 200:
        # Decode the JSON response into a dictionary and use the data
        result = response.json()
        print (result)
    else:
        print ("Update device API server settings failed! - " + str(response.text))

except Exception as e: print (str(e))
```
	{'statusCode': 790200, 'statusDescription': 'Success.'}

# cURL Code from Postman:
```python
curl --location --request PUT 'https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/SharedDeviceSettings/APIServerSetting' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'token: 609299f6-abbe-4a8c-a9ff-deb6a69451c2' \
--data-raw '{
    "HostName": "US-BOS-R1",

    "API_setting":[
        {
            "API_plugin":"ServiceNow API Adapter",
            "API_server":{
                "name":"ServiceNow1750"
            }
        }

    ]
}'
```
