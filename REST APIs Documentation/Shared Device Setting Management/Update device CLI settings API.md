Shared Device Setting REST API Design 
==========================

## PUT /ServicesAPI/API/V1/CMDB/SharedDeviceSettings/CLISetting

This API is used to update device CLI settings in current domain. The response of this API will return a list in JSON format.<br>

**Note:** the privilege requirement is following UI setting: except Guest role, all other roles can access these three PUT APIs.

## Detail Information

>**Title:** Update device CLI settings API

>**Version:** 03/08/2022

>**API Server URL:** http(s)://IP Address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/SharedDeviceSettings/CLISetting

>**Authentication:**

|**Type**|**In**|**Name**|
|------|------|------|
|Bearer Authentication|Headers|Authentication token|

## Request body (*required)

|**Name**|**Type**|**Description**|
|------|------|------|
|HostName*| string | Device hostname.It is required if no input on ManageIp |
|ManageIp* | string | Device management IP address. It is required if no input on HostName|
|CLI_setting| object | CLI setting of current device. |
|CLI_setting.mode| integer | mode for cli access. <br> 0 : DirectAccess <br> 1 : ViaOtherDevice|
|CLI_setting.access_mode| integer | access mode. <br> 0 : Telnet <br> 1 : SSH <br> 2 : SSHPubicKey|
|CLI_setting.access_mode_port| integer | port number of access mode. |
|CLI_setting.CLI_credential_username| string | usename for CLI credential. |
|CLI_setting.CLI_credential_password| string | password for CLI credential. |
|CLI_setting.privilege_username| string | device privilege username. |
|CLI_setting.privilege_password| string | device privilege password. |
|CLI_setting.Telnet_Proxy_Id| string | Telnet_Proxy_Id. |
|CLI_setting.Telnet_Proxy_Id_For_Smart_CLI| string | Telnet_Proxy_Id_For_Smart_CLI. |
|CLI_setting.prompt_settings| object | object for CLI prompt settings. |
|CLI_setting.prompt_settings.non_privilege_prompt| string | non_privilege_prompt. |
|CLI_setting.prompt_settings.privilege_prompt| string | privilege_prompt. |
|CLI_setting.prompt_settings.login_prompt_username| string | login_prompt_username. |
|CLI_setting.prompt_settings.login_prompt_password| string | login_prompt_password. |
|CLI_setting.prompt_settings.privilege_login_prompt| string | privilege_login_prompt_username. |
|CLI_setting.prompt_settings.privilege_password_prompt| string | privilege_password_prompt. |
|CLI_setting.advenced_setting| object | object for CLI advanced settings. |
|CLI_setting.advenced_setting.ForceTimeout| integer | force time out for CLI access |
|CLI_setting.advenced_setting.SSH_key_setting| object | object for CLI SSH finger print settings. |
|CLI_setting.advenced_setting.SSH_key_setting.checkSSHFingerprint| bool | enable or not for SSH Fingerprint key. |
|CLI_setting.advenced_setting.SSH_key_setting.SSHFingerprintKey| string | SSH fingerprint key value. |



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
        "CLI_setting" : {
            "mode":0\1,
            "access_mode":0\1\2,
            "access_mode_port":"string"/int,
            "CLI_credential_username":"string",
            "CLI_credential_Password":"string",
            "privilege_username":"string",
            "privilege_password":"string",           
            "Telnet_Proxy_Id" : "string",
            "Telnet_Proxy_Id_For_Smart_CLI" : "string"，
            "prompt_settings":{
                "non_privilege_prompt":"string",
                "privilege_prompt":"string",
                "login_prompt_username":"string",
                "login_prompt_password":"string",
                "privilege_login_prompt":"string"
                "privilege_password_prompt":"string"
            },
            "advenced_setting":{
                "ForceTimeout" : int,
                "SSH_key_setting":{
                    "checkSSHFingerprint" : true,
                    "SSHFingerprintKey" : "xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx"
                }
            }
        }
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
| 794011 | OperationFailed | There is no match hostname or managementip founded.<br>This device is locked, can not be updated.<br>Invalid IP.<br>Please insert a correct cli access method value.<br>Please insert a correct cli setting mode value.<br>The privateKey can not null.<br>The cli setting privateKey can not null.<br>There is no match cli setting privateKey. |
| 791000 | ParameterNull | CLI Setting is required |
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
full_url = "https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/SharedDeviceSettings/CLISetting"
body = {
    "HostName": "US-BOS-R1",
    "CLI_setting":{
        "access_mode":1
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
        print ("Update device CLI settings failed! - " + str(response.text))

except Exception as e: print (str(e))
```
	{'statusCode': 790200, 'statusDescription': 'Success.'}
	
# cURL Code from Postman:
```python
curl --location --request PUT 'https://unicorn-new.netbraintech.com/ServicesAPI/API/V1/CMDB/SharedDeviceSettings/CLISetting' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'token: 609299f6-abbe-4a8c-a9ff-deb6a69451c2' \
--data-raw '{
    "HostName": "US-BOS-R1",
    "CLI_setting":{
        "access_mode":1
    }
}'
```