
# Domain API

## ***GET*** /V1/CMDB/Domains/{?tenantId}
This API returns a list of accessible domains of a specific tenant. The returned accessible domains list varies according to the user privileges. To retrieve a full list of domains in the specified tenant, the user must have full access to all domains of the tenant. 

## Detail Information

> **Title** : Get all accessible domains of a tenants API

> **Version** : 03/02/2022

> **API Server URL** : http(s):// IP address of your NetBrain Web API Server /ServicesAPI/API/V1/CMDB/Domains

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|Bearer Authentication| Parameters | Authentication token | 

 ## Request body(****required***)

>No request body.

 ## Query Parameters(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
| tenantId* | String | Tenant ID |

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
| domains | Array of objects | A list of all accessible domains |
| domains.tenantId | String | Tenant ID of a domain |
| domains.domainId | String | Domain ID.  |
| domains.domainName | String | Domain name. |
| domains.description | String | Domain description |
| domains.licenseInfo | Object | Tenant license information |
| domains.licenseInfo.module | Array of objects | Module list|
| domains.licenseInfo.module.name | String | Module name |
| domains.licenseInfo.module.amount | Integer | Assigned module license amount |
| domains.licenseInfo.module.min_amount | Integer | Minimum module license allowed of this domain |
| domains.licenseInfo.module.max_amount | Integer | Maximum module license allowed of this domain |
| domains.licenseInfo.networkTechs | Array of objects | Network technology list |
| domains.licenseInfo.networkTechs.name | String | Network technology name |
| domains.licenseInfo.networkTechs.amount | Integer | Assigned network technology license amount |
| domains.licenseInfo.networkTechs.min_amount | Integer | Minimum network technology license allowed of this domain |
| domains.licenseInfo.networkTechs.max_amount | Integer | Maximum network technology license allowed of this domain |
| statusCode | Integer | Status code |
| statusDescription | String | Status description |

## Response Codes
|**Code**|**Message**|**Description**|
|------|------|------|
| 790200 | OK |  |
| 795012 | InvalidLicense | Please activate your IE system first! |
| 793001 | InternalServerError | System framework level error |

> ***Example***


```python
{
    "domains": [
        {
            "domainId": "9791c406-5135-40e2-bd61-3a7903d6b752",
            "tenantId": "74f04b73-7368-e833-e4be-0a2bc6d44780",
            "domainName": "Demo-Lab",
            "licenseInfo": {
                "networkTechs": [
                    {
                        "name": "Cisco ACI",
                        "max_amount": 20000,
                        "min_amount": 288,
                        "amount": 1000
                    },
                    {
                        "name": "WAP",
                        "max_amount": 20000,
                        "min_amount": 3,
                        "amount": 1000
                    },
                    {
                        "name": "vCenter",
                        "max_amount": 20000,
                        "min_amount": 8,
                        "amount": 1000
                    },
                    {
                        "name": "NSX-v",
                        "max_amount": 20000,
                        "min_amount": 8,
                        "amount": 1000
                    },
                    {
                        "name": "Amazon AWS",
                        "max_amount": 20000,
                        "min_amount": 55,
                        "amount": 1000
                    },
                    {
                        "name": "Microsoft Azure",
                        "max_amount": 20000,
                        "min_amount": 39,
                        "amount": 1000
                    },
                    {
                        "name": "Google Cloud Platform",
                        "max_amount": 20000,
                        "min_amount": 372,
                        "amount": 1000
                    }
                ],
                "modules": [
                    {
                        "name": "Foundation",
                        "max_amount": 20000,
                        "min_amount": 226,
                        "amount": 1000
                    },
                    {
                        "name": "Change Management",
                        "max_amount": 26666,
                        "min_amount": 227,
                        "amount": 1333
                    },
                    {
                        "name": "Application Assurance",
                        "max_amount": 656664,
                        "min_amount": 4302,
                        "amount": 32832
                    },
                    {
                        "name": "Intent Based Automation",
                        "max_amount": 146666,
                        "min_amount": 997,
                        "amount": 7333
                    }
                ]
            },
            "description": ""
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
token = "85fb5789-1f00-4179-b78d-dd9dc0530fb2"
tenantId = "74f04b73-7368-e833-e4be-0a2bc6d44080"
full_url = "https://netbraintechLab.com/ServicesAPI/API/V1/CMDB/Domains"

# Set proper headers
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

data = {"tenantId": tenantId}

try:
    # Do the HTTP request
    response = requests.get(full_url, params=data, headers=headers, verify=False)
    # Check for HTTP codes other than 200
    if response.status_code == 200:
        # Decode the JSON response into a dictionary and use the data
        result = response.json()
        print (result)
    else:
        print ("Get domains failed! - " + str(response.text))

except Exception as e: print (str(e))
```

    {'domains': [{'domainId': '9791c406-5135-40e2-bd61-3a7903d6b752', 'tenantId': '74f04b73-7368-e833-e4be-0a2bc6d44780', 'domainName': 'Demo-Lab', 'licenseInfo': {'networkTechs': [{'name': 'Cisco ACI', 'max_amount': 20000, 'min_amount': 288, 'amount': 1000}, {'name': 'WAP', 'max_amount': 20000, 'min_amount': 3, 'amount': 1000}, {'name': 'vCenter', 'max_amount': 20000, 'min_amount': 8, 'amount': 1000},{'name': 'NSX-v', 'max_amount': 20000, 'min_amount': 8, 'amount': 1000}, {'name': 'Amazon AWS', 'max_amount': 20000, 'min_amount': 55, 'amount': 1000}, {'name': 'Microsoft Azure', 'max_amount': 20000,'min_amount': 39, 'amount': 1000}, {'name': 'Google Cloud Platform', 'max_amount': 20000, 'min_amount': 372, 'amount': 1000}], 'modules': [{'name': 'Foundation', 'max_amount': 20000, 'min_amount': 226, 'amount': 1000}, {'name': 'Change Management', 'max_amount': 26666, 'min_amount': 227, 'amount': 1333}, {'name': 'Application Assurance', 'max_amount': 656664, 'min_amount': 4302, 'amount': 32832}, {'name': 'Intent Based Automation', 'max_amount': 146666, 'min_amount': 997, 'amount': 7333}]}, 'description': ''}], 'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman


```python
curl --location --request GET 'https://netbraintechLab.com/ServicesAPI/API/V1/CMDB/Domains?tenantId=74f04b73-7368-e833-e4be-0a2bc6d44880' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'token: 85fb5789-1f00-4179-b78d-dd9dc0530fa2'
```

## Error Examples


```python
###################################################################################################################    

"""Error 1: empty tenantId"""

Input:
    token = "4f257785-d5f9-42d4-b896-d21f0cb62e6f"
    tenantId = ""
    full_url = "http://IP address of your NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Domains"

Response:
    "{
    "statusCode": 793001,
    "statusDescription": "Inner exception. please check system log(default location: log/NgThirdAPI.log)"
}"

###################################################################################################################    

"""Error 2: wrong tenantId"""

Input:
    token = "4f257785-d5f9-42d4-b896-d21f0cb62e6f"
    tenantId = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    full_url = "http://IP address of your NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Domains"

Response:
    "{
    "statusCode": 791006,
    "statusDescription": "tenant with id aaaaaaaaaaaaaaaaaaaaaaaaaa does not exist."
}"
```
