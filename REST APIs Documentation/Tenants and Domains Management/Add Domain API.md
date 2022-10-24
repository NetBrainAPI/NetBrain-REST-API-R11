
# Domain API

## ***POST*** /V3/CMDB/Domains
Use this API to add a domain to a NetBrain Tenant.

## Detail Information

> **Title** : Add Domain API

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
| domainName* | String | The new domain name |
| description | String | The new domain description |
| licenseInfo* | Object | Domain license information |
| licenseInfo.modules* | Array of objects | Module list |
| licenseInfo.modules.name* | String | Module name. Module name includes: <br>Foundation<br>Change Management<br>Application Assurance<br>Intent Based Automation|
| licenseInfo.modules.amount* | Integer | Module license amount to be assigned |
| licenseInfo.networkTechs | Array of objects | Network technology list |
| licenseInfo.networkTechs.name | String | Network Technology name. Network Technology name includes:<br>Cisco ACI<br>WAP<br>vCenter<br>NSX-v<br>Amazon AWS<br>Microsoft Azure<br>Google Cloud Platform|
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
|domainId| String | The new domain ID |
|statusCode| Integer | Status code. |
|statusDescription| String | Status description |

## Response Codes
|**Code**|**Message**|**Description**|
|------|------|------|
| 790200 | OK |  |
| 791000 | ParameterNull | Null parameter: the parameter 'tenantId' cannot be null.<br>Null parameter: the parameter 'domainName' cannot be null.<br>Null parameter: the parameter 'licenseInfo' cannot be null.<br>Null parameter: the parameter 'request body' cannot be null. |
| 792007 | InvaliSpecialCharacters | Invalid {0}, the {0} can't contain any of the following characters {1}. |
| 792004 | InvalidStrLen | The value length of '{0}' should be between {1} and {2} inclusive. |
| 791007 | ExistedDataInSystem | {0} already exists. |
| 793001 | InternalServerError | System framework level error |
| 791006 | NoDataInSystem | The tenant with id {0} does not exist. |
| 795011 | LicenseOverLimit | ACI ports amount 10 can not be smaller than 20<br>ACI ports amount 10 can not be greater than 100 |

> ***Example***


```python
{
    "domainId": "e5fa1da2-f9b5-465c-a060-a89a09dc3f8e",
    "statusCode": 790200,
    "statusDescription": "Success."
}
```



# Full Example: 


```python
# import python modules 
import requests
import json

# Set the request inputs
token = "f7372946-48c4-4291-90ea-4c808633e922"
tenantId = "74f678b73-7368-e833-e4be-0a2bc6d44780"
full_url = "https://unicorn-new.netbraintech.com/ServicesAPI/API/V3/CMDB/Domains"

# Set proper headers
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token
body = {
    "tenantId": tenantId,
    "domainName": "API test",
    "licenseInfo":{
        "modules":[
            {
                "name":"Change Management",
                "amount":1
            }
        ],
        "networkTechs":[
            {
                "name":"Amazon AWS",
                "amount":10
            }
        ]
    }
}

try:
    # Do the HTTP request
    response = requests.post(full_url, headers=headers, data = json.dumps(body), verify=False)
    # Check for HTTP codes other than 200
    if response.status_code == 200:
        # Decode the JSON response into a dictionary and use the data
        result = response.json()
        print (result)
    else:
        print ("Add domain failed! - " + str(response.text))

except Exception as e: print (str(e))
```

    {'domainId': '668489d7-54d9-41a9-a04e-0283f46e9135', 'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman:


```python
curl --location --request POST 'https://unicorn-new.netbraintech.com/ServicesAPI/API/V3/CMDB/Domains' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'token: f7372946-48c4-4291-90ea-4c808633e922' \
--data-raw '{
    "tenantId": "74f678b73-7368-e833-e4be-0a2bc6d44780",
    "domainName": "API test",
    "licenseInfo":{
        "modules":[
            {
                "name":"Change Management",
                "amount":1
            }
        ],
        "networkTechs":[
            {
                "name":"Amazon AWS",
                "amount":10
            }
        ]
    }
}
'
```

# Error Examples:


```python
###################################################################################################################    

"""Error 1: empty inputs"""

Input:
        
        "tenantId" = "" # Can not be null
        "domainName" = "" # Can not be null
        "licenseInfo" = None # Can not be null
        
Response:
    
        "Add domain failed! - 
            {
                "statusCode":791000,
                "statusDescription":"Null parameter: the parameter 'tenantId' cannot be null.."
            }"
            
        
        "Add domain failed! - 
            {
                "statusCode":791000,
                "statusDescription":"Null parameter: the parameter 'domainName' cannot be null."
            }"
            
            
        "Add domain failed! - 
            {
                "statusCode":791000
                "statusDescription":"Null parameter: the parameter 'licenseInfo' cannot be null."
            }"

###################################################################################################################    

"""Error 2: wrong inputs"""

Input:
        
        "tenantId" = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # No tenant have a ID like this.
        "domainName" = "testDomain2"
        "licenseInfo":{
			"modules":[
				{
					"name":"Change Management",
					"amount":1
				}
			],
			"networkTechs":[
				{
					"name":"Amazon AWS",
					"amount":10
				}
			]
		}

Response:
    
            "Add domain failed! - 
                {
                    "statusCode":791006,
                    "statusDescription":"tenant with id XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX does not exist."
                }"

###################################################################################################################    

"""Error 3: domain maximumNodes greater than tenant maximumNodes"""""""""""""""""""""""""""""""""""""""""""""""""""""

Input:
        
        "tenantId" = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # No tenant have a ID like this.
        "domainName" = "testDomain2"
        "licenseInfo":{
			"modules":[
				{
					"name":"Foundation",
					"amount":100000000
				}
			],
			"networkTechs":[
				{
					"name":"Amazon AWS",
					"amount":10
				}
			]
		}

        
Response:
    
            "Add domain failed! - 
                {"statusCode":795011,
				"statusDescription":"Foundation nodes amount 100000000 is out of range 100000000 - 19000\r\nChange Management nodes amount 100000000 is out of range 100000000 - 25333\r\nApplication Assurance nodes amount 100000083 is out of range 100000083 - 623832\r\nIntent Based Automation nodes amount 100000010 is out of range 100000010 - 139333\r\n"}

```
