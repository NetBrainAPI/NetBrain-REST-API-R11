Shared Device Setting REST API Design 
==========================

## PUT /ServicesAPI/API/V1/CMDB/SharedDeviceSettings/BasicSetting

This API is used to update device basic settings in current domain. The response of this API will return a list in JSON format.<br>

**Note:** the privilege requirement is following UI setting: except Guest role, all other roles can access these three PUT APIs.

## Detail Information

>**Title:** Update device basic settings API

>**Version:** 03/08/2022

>**API Server URL:** http(s)://IP Address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/SharedDeviceSettings/BasicSetting

>**Authentication:**

|**Type**|**In**|**Name**|
|------|------|------|
|Bearer Authentication|Headers|Authentication token|

## Request body (*required)

|**Name**|**Type**|**Description**|
|------|------|------|
|HostName*| string | Device hostname. It is required if no input on ManageIp|
|ManageIp* | string | Device management IP address. It is required if no input on HostName|
|ApplianceId | string | Name of front server. |
|Locked | bool | WARNING: With the NetBrain 10.1 release, the device setting main lock feature has been upgraded to 3 individual separate locks on Management IP, Front Server, and CLI/SNMP/API settings. Considering backward compatibility, this parameter is remained in 10.1 version, and will be deprecated in a near future version. According to the feature upgrade, the meaning of this parameter values is slightly different from older versions. Code upgrade is not mandatory in this version. However, it is highly recommended to read the updated description carefully and prepare for your code upgrade soon before the deprecation to take advantages from utilizing the more flexible setting capabilities.<br>To lock the device settings.<br>true – Set Management IP, Front Server, CLI/SNMP/API all as locked.<br>false – Set Management IP, Front Server, CLI/SNMP/API all as unlocked.<br>This parameter will overwrite Locked_manageIp/Locked_applianceId/Locked_cli_snmp_api settings. Don't use them mixed.|
|Locked_manageIp | bool | Whether the Management IP setting is locked. |
|Locked_applianceId | bool | Whether the Front Server setting is locked. |
|Locked_cli_snmp_api | bool | Whether the CLI/SNMP/API settings are locked. |
|LiveStatus| integer | live status of current device. |

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


## Response

| Code | Message | Description |
|--------|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 790200 | OK ||
| 794011 | OperationFailed | There is no match hostname or managementip founded.<br>This device is locked, can not be updated.<br>Invalid Manage IP.|
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
full_url = "https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/SharedDeviceSettings/BasicSetting"
body = {
    "HostName": "US-BOS-R1",
    "ManageIp": "10.8.1.51",
    "Locked" : "false",
    "Locked_manageIp":False,
    "Locked_applianceId":False,
    "Locked_cli_snmp_api":False,
    "LiveStatus" : 1,
    "ApplianceId" : "netbrainfs"
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
        print ("Update device basic settings failed! - " + str(response.text))

except Exception as e: print (str(e))
 ```
	{'statusCode': 790200, 'statusDescription': 'Success.'}

# cURL Code from Postman:
```python
curl --location --request PUT 'https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/SharedDeviceSettings/BasicSetting' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'token: 609299f6-abbe-4a8c-a9ff-deb6a69451c2' \
--data-raw '{
    "HostName": "US-BOS-R1",
    "ManageIp": "10.8.1.51",
    "Locked" : false,
    "Locked_manageIp":false,
    "Locked_applianceId":false,
    "Locked_cli_snmp_api":false,
    "LiveStatus" : 1,
    "ApplianceId" : "netbrainfs"
}'
```
