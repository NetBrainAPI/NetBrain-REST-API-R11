
# Tenant API

## ***GET*** /V1/CMDB/Tenants/
This API returns a list of accessible tenants. The returned tenants list varies according to the user privileges. To retrieve a full list of all available tenants, users must log in with System Admin role. 

## Detail Information

> **Title** : Get All Accessible Tenants API

> **Version** : 03/07/2022

> **API Server URL** : http(s):// < NetBrain Web API Server Address > /ServicesAPI/API/V1/CMDB/Tenants

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|Bearer Authentication| Parameters | Authentication token | 

## Request body(****required***)

>No request body.

 ## Parameters(****required***)

> No parameters required

 ## Headers

> **Data Format Headers**

|**Name**|**Type**|**Description**|
|------|------|------|
| Content-Type | string  | support "application/json" |
| Accept | string  | support "application/json" |

> **Authorization Headers**

|**Name**|**Type**|**Description**|
|------|------|------|
| token* | string  | Authentication token, get from login API. |


 ## Response

|**Name**|**Type**|**Description**|
|------|------|------|
| tenants | Array of objects | A list of all accessible tenants |
| tenants.tenantId | String | Tenant ID.  |
| tenants.tenantName | String | Tenant name. |
| tenants.description | String | Tenant description |
| tenants.licenseInfo | Object | Tenant license information |
| tenants.licenseInfo.module | Array of objects | Module list|
| tenants.licenseInfo.module.name | String | Module name |
| tenants.licenseInfo.module.amount | Integer | Assigned module license amount |
| tenants.licenseInfo.module.min_amount | Integer | Minimum module license allowed of this tenant |
| tenants.licenseInfo.module.max_amount | Integer | Maximum module license allowed of this tenant |
| tenants.licenseInfo.networkTechs | Array of objects | Network technology list |
| tenants.licenseInfo.networkTechs.name | String | Network technology name |
| tenants.licenseInfo.networkTechs.amount | Integer | Assigned network technology license amount |
| tenants.licenseInfo.networkTechs.min_amount | Integer | Minimum network technology license allowed of this tenant |
| tenants.licenseInfo.networkTechs.max_amount | Integer | Maximum network technology license allowed of this tenant |
| statusCode | Integer | Status code |
| statusDescription | String | Status description |


## Response Code
|**Code**|**Message**|**Description**|
|------|------|------|
| 790200 | OK |  |
| 793001 | InternalServerError | System framework level error |

> ***Example*** :


```python
{
    "tenants": [
        {
            "tenantId": "74f04b73-7368-e833-e4be-0a2bc6d44781",
            "tenantName": "Initial Tenant",
            "licenseInfo": {
                "networkTechs": [
                    {
                        "name": "Cisco ACI",
                        "max_amount": 200000,
                        "min_amount": 1000,
                        "amount": 20000
                    },
                    {
                        "name": "WAP",
                        "max_amount": 200000,
                        "min_amount": 1000,
                        "amount": 20000
                    },
                    {
                        "name": "vCenter",
                        "max_amount": 200000,
                        "min_amount": 1000,
                        "amount": 20000
                    },
                    {
                        "name": "NSX-v",
                        "max_amount": 200000,
                        "min_amount": 1000,
                        "amount": 20000
                    },
                    {
                        "name": "Amazon AWS",
                        "max_amount": 200000,
                        "min_amount": 1000,
                        "amount": 20000
                    },
                    {
                        "name": "Microsoft Azure",
                        "max_amount": 200000,
                        "min_amount": 1000,
                        "amount": 20000
                    },
                    {
                        "name": "Google Cloud Platform",
                        "max_amount": 200000,
                        "min_amount": 1000,
                        "amount": 20000
                    }
                ],
                "modules": [
                    {
                        "name": "Foundation",
                        "max_amount": 199000,
                        "min_amount": 1000,
                        "amount": 20000
                    },
                    {
                        "name": "Change Management",
                        "max_amount": 265660,
                        "min_amount": 1333,
                        "amount": 26666
                    },
                    {
                        "name": "Application Assurance",
                        "max_amount": 6565640,
                        "min_amount": 32832,
                        "amount": 656664
                    },
                    {
                        "name": "Intent Based Automation",
                        "max_amount": 1465660,
                        "min_amount": 7333,
                        "amount": 146666
                    }
                ]
            },
            "description": "This is the initial tenant"
        }
    ],
    "statusCode": 790200,
    "statusDescription": "Success."
}
```

## Full Example : 


```python
# import python modules 
import requests

# Set the request inputs
token = "460af44a-0737-437d-9814-563a9808vd5a"
tenantId = "74f04b73-7368-e833-e4be-0a2bc6d44781"
full_url = "https://integrationLab.netbraintech.com/ServicesAPI/API/V1/CMDB/Tenants"

# Set proper headers
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

try:
    # Do the HTTP request
    response = requests.get(full_url, headers=headers, verify=False)
    # Check for HTTP codes other than 200
    if response.status_code == 200:
        # Decode the JSON response into a dictionary and use the data
        result = response.json()
        print (result)
    else:
        print ("Get domains failed! - " + str(response.text))

except Exception as e: print (str(e))
```

```python
{'tenants': [{'tenantId': '74f04b73-7368-e833-e4be-0a2bc6d44780', 'tenantName': 'Initial Tenant', 'licenseInfo': {'networkTechs': [{'name': 'Cisco ACI', 'max_amount': 200000, 'min_amount': 1000, 'amount': 20000}, {'name': 'WAP', 'max_amount': 200000, 'min_amount': 1000, 'amount': 20000}, {'name': 'vCenter', 'max_amount': 200000, 'min_amount': 1000, 'amount': 20000}, {'name': 'NSX-v', 'max_amount': 200000, 'min_amount': 1000, 'amount': 20000}, {'name': 'Amazon AWS', 'max_amount': 200000, 'min_amount': 1000, 'amount': 20000}, {'name': 'Microsoft Azure', 'max_amount': 200000, 'min_amount': 1000, 'amount': 20000}, {'name': 'Google Cloud Platform', 'max_amount': 200000, 'min_amount': 1000, 'amount': 20000}], 'modules': [{'name': 'Foundation', 'max_amount': 199000, 'min_amount': 1000, 'amount': 20000}, {'name': 'Change Management', 'max_amount': 265660, 'min_amount': 1333, 'amount': 26666}, {'name': 'Application Assurance', 'max_amount': 6565640, 'min_amount': 32832, 'amount': 656664}, {'name': 'Intent Based Automation', 'max_amount': 1465660, 'min_amount': 7333, 'amount': 146666}]}, 'description': 'This is the initial tenant'}], 'description': ''}], 'statusCode': 790200, 'statusDescription': 'Success.'}
```

# cURL Code from Postman


```python
curl --location --request GET 'https://IntegrationLab.netbraintech.com/ServicesAPI/API/V1/CMDB/Tenants' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'token: 460af44a-0737-437d-9814-563a9808dd5a'
```

## Error Example : 


```python
###################################################################################################################    

"""Error 1: Empty URL/Wrong URL"""

Input:
    token = "828a4561-5ee5-40ac-bf98-01788be48330" 
    
    full_url = ""  

Response:
    { "statusCode": 793404, "statusDescription": "No resource"}

###################################################################################################################     

"""Error 2: Empty Token/Wrong Token"""

Input:
    token = "" 
    
    full_url = "http://192.168.28.79/ServicesAPI/API/V1/CMDB/Tenants"  

Response:
    { "statusCode": 795005, "statusDescription": "Invalid token. }
     
```
