
# Domain API

## ***PUT*** /V3/CMDB/Domains
Use this API to update a domain of a NetBrain tenant.

## Detail Information

> **Title** : Update Domain API

> **Version** : 03/07/2022

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V3/CMDB/Domains

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
| tenantId* | String | Tenant ID |
| domainId* | String | Domain ID |
| domainName* | String | The new domain name |
| description | String | The new domain description |
| licenseInfo* | Object | Domain license information |
| licenseInfo.modules* | Array of objects | Module list |
| licenseInfo.modules.name* | String | Module name. Module name includes: <br>Foundation<br>Change Management<br>Application Assurance<br>Intent Based Automation |
| licenseInfo.modules.amount* | Integer | Module license amount to be assigned |
| licenseInfo.networkTechs | Array of objects | Network technology list |
| licenseInfo.networkTechs.name | String | Network Technology name. Network Technology name includes:<br>Cisco ACI<br>WAP<br>vCenter<br>NSX-v<br>Amazon AWS<br>Microsoft Azure<br>Google Cloud Platform |
| licenseInfo.networkTechs.amount | Integer | Network Technology license amount to be assigned |

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
| 791000 | ParameterNull | Null parameter: the parameter 'tenantId' cannot be null.<br>Null parameter: the parameter 'domainName' cannot be null.<br>Null parameter: the parameter 'licenseInfo' cannot be null.<br>Null parameter: the parameter 'request body' cannot be null. |
| 792007 | InvaliSpecialCharacters | Invalid {0}, the {0} can't contain any of the following characters {1}. |
| 792004 | InvalidStrLen | The value length of '{0}' should be between {1} and {2} inclusive. |
| 793001 | InternalServerError | System framework level error |
| 791006 | NoDataInSystem | The tenant with id {0} does not exist.<br>domain with id {0} does not exist. |
| 795011 | LicenseOverLimit | ACI ports amount 10 can not be smaller than 20<br>ACI ports amount 10 can not be greater than 100 |
| 795003 | NoPermission | Insufficient permissions: the current user has insufficient permissions to perform the requested operation. |

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
tenantId = "94f04b73-7368-e833-e4be-0a2bc6d44780"
domainId = "96b943fb-3b73-4432-8b8a-80255e4e592f"

full_url = "https://unicorn-new.netbraintech.com/ServicesAPI/API/V3/CMDB/Domains"

# Set proper headers
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token
body = {
    "tenantId":tenantId,
    "domainId":domainId,
    "domainName":"API test",
    "licenseInfo":{
        "modules":[
            {
                "name":"Foundation",
                "amount":100
               
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
        print ("Update domain failed! - " + str(response.text))

except Exception as e: print (str(e))
```

    {'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman:


```python
curl --location --request PUT 'https://unicorn-new.netbraintech.com/ServicesAPI/API/V3/CMDB/Domains' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'token: q7372946-48c4-4291-90ea-4c808633e989' \
--data-raw '{
    "tenantId":"94f04b73-7368-e833-e4be-0a2bc6d44780",
    "domainId":"96b943fb-3b73-4432-8b8a-80255e4e592f",
    "domainName":"API test",
    "licenseInfo":{
        "modules":[
            {
                "name":"Foundation",
                "amount":100
            }
        ]
    }
    
}
'
```

