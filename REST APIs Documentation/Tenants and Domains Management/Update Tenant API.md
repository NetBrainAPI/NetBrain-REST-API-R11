
# Tenant API

## ***PUT*** /V3/CMDB/Tenants
Use this API to update a tenant of Netbrain system.

## Detail Information

> **Title** : Update Tenant API

> **Version** : 02/02/2022

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V3/CMDB/Tenants

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body (\*required)
-------------------------

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
| tenantId*   | String | Tenant ID |
| tenantName* | String | The new tenant name |
| description | String | The new tenant description |
| licenseInfo* | Object | Tenant license information |
| licenseInfo.modules* | Array of objects | Module list |
| licenseInfo.modules.name* | String | Module name. Module name includes: <br>Foundation<br>Change Management<br>Application Assurance<br>Intent Based Automation |
| licenseInfo.modules.amount* | Integer | Module license amount to be assigned |
| licenseInfo.modules,enable | Boolean | Whether or not to enable the module |
| licenseInfo.networkTechs | Array of objects | Network technology list |
| licenseInfo.networkTechs.name | String | Network Technology name. Network Technology name includes:<br>Cisco ACI<br>WAP<br>vCenter<br>NSX-v<br>Amazon AWS<br>Microsoft Azure<br>Google Cloud Platform |
| licenseInfo.networkTechs.amount | Integer | Network Technology license amount to be assigned |
| advancedOptions | Object | Tenant advanced setting |
| advancedOptions.tenantConnSetting | Object | Tenant data DB setting |
| advancedOptions.tenantConnSetting.servers | Array of Strings | MongoDB server IPs |
| advancedOptions.tenantConnSetting.replicaSet | String | MongoDB Replica Set name |
| advancedOptions.tenantConnSetting.user | String | MongoDB username |
| advancedOptions.tenantConnSetting.password | String | MongoDB password |
| advancedOptions.liveDataConnSetting | Object | Live data DB setting |
| advancedOptions.liveDataConnSetting.servers | Array of Strings | MongoDB server IPs |
| advancedOptions.liveDataConnSetting.replicaSet | String | MongoDB Replica Set name |
| advancedOptions.liveDataConnSetting.user | String | MongoDB username |
| advancedOptions.liveDataConnSetting.password | String | Mongodb password |

## Query Parameters (\*required)

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
|statusCode| Integer | Status code. |
|statusDescription| String | Status description |

## Response Codes
|**Code**|**Message**|**Description**|
|------|------|------|
| 790200 | OK |  |
| 791000 | ParameterNull | Null parameter: the parameter 'tenantName' cannot be null.<br>Null parameter: the parameter 'licenseInfo' cannot be null.<br>Null parameter: the parameter 'tenantId' cannot be null.<br>Null parameter: the parameter 'request body' cannot be null. |
| 792007 | InvaliSpecialCharacters | Invalid {0}, the {0} can't contain any of the following characters {1}. |
| 792004 | InvalidStrLen | The value length of 'tenantName' should be between 2 and 20 inclusive.<br>The value length of 'description' should be between 0 and 1024 inclusive. |
| 791007 | ExistedDataInSystem | The tenant {0} already exists.<br>The tenant with ID {0} is using this name {1} already exists. |
| 793001 | InternalServerError | System framework level error |
| 791006 | NoDataInSystem | The tenant with ID {0} does not exist. |
| 795011 | LicenseOverLimit | {0} {1} amount {2} is out of range {3} - {4} <br>e.g :  ACI ports amount 10 is out of range 2 - 5<br>{0} nodes amount {1} is out of range {2} - {3}<br>e.g:   Change Management nodes amount 20 is out of range  30 -50 |

> ***Example***


```python
{
    "statusCode": 790200,
    "statusDescription": "success"
}
```

# Full Example:


```python
# import python modules 
import requests
import json

# Set the request inputs
token = "q7372946-48c4-4291-90ea-4c808633e989"
tenantId = "177bdf8f-b5af-4298-83d8-b388254b2609"
full_url = "https://unicorn-new.netbraintech.com/ServicesAPI/API/V3/CMDB/Tenants"

# Set proper headers
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token
body = {
    "tenantId": "277bdf8f-b5af-4298-83d8-b388254b2609",
    "tenantName": "API test2",
    "licenseInfo":{
        "modules":[
            {
                "name":"Foundation",
                "amount":55
            }
        ]
    }
}
try:
    # Do the HTTP request
    response = requests.put(full_url, headers=headers, data = json.dumps(body), verify=False)
    # Check for HTTP codes other than 200
    if response.status_code == 200:
        # Decode the JSON response into a dictionary and use the data
        result = response.json()
        print (result)
    else:
        print ("Update Tenant failed! - " + str(response.text))

except Exception as e: print (str(e))
```

    {'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman:


```python
curl --location --request PUT 'https://unicorn-new.netbraintech.com/ServicesAPI/API/V3/CMDB/Tenants' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'token: q7372946-48c4-4291-90ea-4c808633e989' \
--data-raw '{
    "tenantId": "177bdf8f-b5af-4298-83d8-b388254b2609",
    "tenantName": "API test2",
    "licenseInfo":{
        "modules":[
            {
                "name":"Foundation",
                "amount":55
            }
        ]
    }
}'
```
