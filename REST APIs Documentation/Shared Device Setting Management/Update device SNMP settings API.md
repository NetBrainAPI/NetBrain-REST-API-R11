Shared Device Setting REST API Design 
==========================

## PUT /ServicesAPI/API/V1/CMDB/SharedDeviceSettings/SNMPSetting

This API is used to update device SNMP settings in current domain. The response of this API will return a list in JSON format.<br>

## Detail Information

>**Title:** Update device SNMP settings API

>**Version:** 03/08/2022

>**API Server URL:** http(s)://IP Address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/SharedDeviceSettings/SNMPSetting

>**Authentication:**

|**Type**|**In**|**Name**|
|------|------|------|
|Bearer Authentication|Headers|Authentication token|

## Request body (*required)

|**Name**|**Type**|**Description**|
|------|------|------|
|HostName| string | Device hostname. It is required if no input on ManageIp|
|ManageIp | string | Device management IP address. It is required if no input on HostName |
|SNMP_setting| object | SNMP setting of current device. |
|SNMP_setting.roString| string  | value of device snmp RO.  |
|SNMP_setting.rwString| string | value of device snmp RWq. |
|SNMP_setting.snmpPort| integer | SNMP port number. |
|SNMP_setting.snmpVersion| integer | version number of snmp version for current device |
|SNMP_setting.UseCustomizedManagementIp| bool | whether current device using the customized management IP.|
|SNMP_setting.v3| string | Alies name. |
|SNMP_setting.retrieve_CPU_OID| string | value of customized management IP retrieve CPU OID. |
|SNMP_setting.retrieve_memory_OID| string | value of customized management IP retrieve memory OID.|
|SNMP_setting.CustomizedManagementIp| object | SNMP customized management IP setting . |
|SNMP_setting.CustomizedManagementIp.ManageIp| string | value of customized management IP. |
|SNMP_setting.CustomizedManagementIp.snmpVersion| string | customized SNMP version. |
|SNMP_setting.CustomizedManagementIp.LiveStatus| integer | SNMP setting of current device. |
|SNMP_setting.CustomizedManagementIp.ro| string | value of customized management IP RO. |
|SNMP_setting.CustomizedManagementIp.rw| string | value of customized management IP RW. |

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
        "SNMP_setting" : {
          "roString": "=",
          "rwString": "=",
          "snmpVersion": 1/2/3,
          "snmpPort": 161,
          "v3": "AliesName",
          "UseCustomizedManagementIp": false,
          "retrieve_CPU":"string",
          "retrieve_memory":"string",
          "CustomizedManagementIp": {            
            "ManageIp": "",
            "LiveStatus": int,
            "snmpVersion": "string",
            "ro": "string",
            "rw": "string",
            "v3": "AliesName"
          }  
        }
}
```

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
full_url = "https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/SharedDeviceSettings/SNMPSetting"
body = {
    "HostName": "US-BOS-R1",
    "SNMP_setting":{
        "roString":"public"
    }
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
        print ("Update device SNMP settings failed! - " + str(response.text))

except Exception as e: print (str(e))
 ```
	{'statusCode': 790200, 'statusDescription': 'Success.'}
	

## Response

| Code | Message | Description |
|--------|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 790200 | OK ||
| 794011 | OperationFailed | There is no match hostname or managementip founded.<br>This device is locked, can not be updated.<br>Invalid IP.<br>Please insert a correct snmp version.<br>Please insert a correct snmp customized management ip version. |
| 791000 | ParameterNull | SNMP Setting is required |
| 793001 | InternalServerError | System framework level error |

# cURL Code from Postman:
```python
curl --location --request PUT 'https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/SharedDeviceSettings/SNMPSetting' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'token: 609299f6-abbe-4a8c-a9ff-deb6a69451c2' \
--data-raw '{
    "HostName": "US-BOS-R1",
    "SNMP_setting":{
        "roString":"public"
    }
}'
```
