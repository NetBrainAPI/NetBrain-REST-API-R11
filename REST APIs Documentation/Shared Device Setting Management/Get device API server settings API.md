Shared Device Setting REST API Design
=====================================

GET /ServicesAPI/API/V1/CMDB/SharedDeviceSettings/APIServerSetting
------------------------------------------------------------------

This API is used to get device API server settings in current domain. The
response of this API will return a list in JSON format.

Detail Information
------------------

>   **Title:** Get device API server settings API

>   **Version:** 03/8/2022

>   **API Server URL:** http(s)://IP Address of NetBrain Web API
>   Server/ServicesAPI/API/V1/CMDB/SharedDeviceSettings/APIServerSetting

>   **Authentication:**

| **Type**              | **In**  | **Name**             |
|-----------------------|---------|----------------------|
| Bearer Authentication | Headers | Authentication token |

Request body (\*required)
-------------------------

>   No request body.

Query Parameters (\*required)
-----------------------------

| **Name** | **Type**                 | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| hostname | string OR list of string | A list of device hostnames                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ip       | string OR list of string | A list of device management IPs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|          |                          | If provided both of hostname and ip, hostname has higher priority. If any of the devices are not found from the provided query parameter, return the found devices as a list in response and add another json key "deviceNotFound", the value is a mixed list of hostnames and IPs that are not found. If both of hostname and ip are as empty, response would depends on the "skip" and "limit" values customer insert.                                                                                                                                                  |
| skip     | integer                  | The amount of records to be skipped. The value must not be negative. If the value is negative, API throws exception {"statusCode":791001,"statusDescription":"Parameter 'skip' cannot be negative"}. No upper bound for this parameter.                                                                                                                                                                                                                                                                                                                                   |
| limit    | integer                  | The up limit amount of device records to return per API call. The value must not be negative. If the value is negative, API throws exception {"statusCode":791001,"statusDescription":"Parameter 'limit' cannot be negative"}. No upper bound for this parameter. If the parameter is not specified in API call, it means there is not limitation setting on the call.                                                                                                                                                                                                    |
|          |                          | If only provide skip value, return the device list with 50 devices information start from the skip number. If only provide limit value, return from the first device in DB. If provided both skip and limit, return as required. Error exceptions follow each parameter's description.                                                                                                                                                                                                                                                                                    |
|          |                          | Skip and limit parameters are based on the search result from DB. The "limit" value valid range is 10 - 100, if the assigned value exceeds the range, the server will respond error message: "Parameter 'limit' must be greater than or equal to 10 and less than or equal to 100."                                                                                                                                                                                                                                                                                       |

Headers
-------

>   **Data Format Headers**

| **Name**     | **Type** | **Description**            |
|--------------|----------|----------------------------|
| Content-Type | string   | support "application/json" |
| Accept       | string   | support "application/json" |

>   **Authorization Headers**

| **Name** | **Type** | **Description**                           |
|----------|----------|-------------------------------------------|
| token    | string   | Authentication token, get from login API. |

Response
--------

| **Name**                                                | **Type**    | **Description**                                                                                                                                         |
|---------------------------------------------------------|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| statusCode                                              | integer     | Code issued by NetBrain server indicating the execution result.                                                                                         |
| statusDescription                                       | string      | The explanation of the status code.                                                                                                                     |
| shareDeviceSettings                                     | object list | A list of device setting object.                                                                                                                        |
| shareDeviceSettings.HostName                            | string      | Device hostname.                                                                                                                                        |
| shareDeviceSettings.ManageIp                            | string      | Device management IP address.                                                                                                                           |
| shareDeviceSettings.ApplianceId                         | string      | Name of front server.                                                                                                                                   |
| shareDeviceSettings.Locked                              | bool        | WARNING: With the NetBrain 10.1 release, the device setting main lock feature has been upgraded to 3 individual separate locks on Management IP, Front Server, and CLI/SNMP/API settings. Considering backward compatibility, this parameter is remained in 10.1 version, and will be deprecated in a near future version. According to the feature upgrade, the meaning of this parameter values is slightly different from older versions. Code upgrade is not mandatory in this version. However, it is highly recommended to read the updated description carefully and prepare for your code upgrade soon before the deprecation to take advantages from utilizing the more flexible setting capabilities.<br>Whether the device setting has been locked.<br>true – 1 or more settings are locked.<br>false – None of Management IP, Front Server, CLI/SNMP/API settings is locked. |
| shareDeviceSettings.Locked_manageIp                     | bool        | Whether the Management IP setting is locked.                                                                                                            |
| shareDeviceSettings.Locked_applianceId                  | bool        | Whether the Front Server setting is locked.                                                                                                             |
| shareDeviceSettings.Locked_liveAccess                 | bool        | Whether the CLI/SNMP/API settings are locked.                                                                                                           |
| shareDeviceSettings.LiveStatus                          | integer     | live status of current device.                                                                                                                          |
| shareDeviceSettings.API_setting                         | object list | API servers applied to current device.                                                                                                                  |
| shareDeviceSettings.API_setting.API_plugin              | string      | name of applied API plugin.                                                                                                                             |
| shareDeviceSettings.API_setting.API_server              | object      | applied API server.                                                                                                                                     |
| shareDeviceSettings.API_setting.API_server.name         | string      | applied API servers name.                                                                                                                               |
| shareDeviceSettings.API_setting.API_server.front_server | string      | front server connect with applied API server.                                                                                                           |

**Example**

```python
{  
    "Shared device setting" : {
        "Locked" : true,
        "Locked_manageIp": true,
        "Locked_applianceId": true,
        "Locked_liveAccess": false,
        "LiveStatus" : 1,
        "HostName" : "CP-SW1",
        "ApplianceId" : "FS1",
        "ManageIp" : "192.168.0.58",
        "API_setting" : {[
                {
                    "API_plugin" : "string",
                    "API_server" : {
                        "name" : "string"/null,
                        "front_server" : "string"/null
                    }     
                },
                {
                    "API_plugin" : "string",
                    "API_server" : {
                        "name" : "string"/null,
                        "front_server" : "string"/null
                    }  
                },
                {
                    "API_plugin" : "string",
                    "API_server" : {
                        "name" : "string"/null,
                        "front_server" : "string"/null
                    }     
                },
                .
                .
                .
            ]
        }
    }
}
```


**Response Code**

| Code   | Message             | Description                                                                                                                                                             |
|--------|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 790200 | OK                  |                                                                                                                                                                         |
| 791001 | InvalidParameter    | Parameter 'skip' must be a positive numeric value.                                                                                                                      |
|        |                     | Parameter 'limit' must be greater than or equal to 10 and less than or equal to 100.                                                                                    |
|        |                     | Invalid IP address provided: {0}.                                                                                                                                       |
| 793001 | InternalServerError | System framework level error                                                                                                                                            |

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
data = {
    "hostname": "US-BOS-R1"
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
        print ("Get device API server settings failed! - " + str(response.text))

except Exception as e: print (str(e))
 ```
	{'shareDeviceSettings': [{'HostName': 'US-BOS-R1', 'ManageIp': '10.8.1.51', 'ApplianceId': 'netbrainfs', 'Locked': False, 'Locked_manageIp': False, 'Locked_applianceId': False, 'Locked_cli_snmp_api': False, 'LiveStatus': 1, 'API_setting': [{'API_plugin': 'ServiceNow API Adapter', 'API_server': {'name': 'ServiceNow1750'}}]}], 'statusCode': 790200, 'statusDescription': 'Success.'}
 
# cURL Code from Postman:
 ```python
curl --location --request GET 'https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/SharedDeviceSettings/APIServerSetting?hostname=US-BOS-R1' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'token: 609299f6-abbe-4a8c-a9ff-deb6a69451c2'
 ```
