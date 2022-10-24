
# Tenant License Template API

GET /V3/CMDB/Tenants/LicenseTemplate
-----------------------

Obtain tenant license template to be used for creating new tenant or updating existing tenant. System Management privilege is required.

Detail Information
------------------

> Title: Get tenant license template

> Version: 03/07/2022

> API Server URL: http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V3/CMDB/Tenants/LicenseTemplate

> Authentication:

| **Type**              | **In**  | **Name**             |
|-----------------------|---------|----------------------|
| Bearer Authentication | Headers | Authentication token |

Request body (\*required)
-------------------------

> No parameters required.

Query Parameters (\*required)
-----------------------------

> No parameters required.

Path Parameters (\*required)
-----------------------------

> No parameters required.

Headers
-------

> Data Format Headers

| **Name**     | **Type** | **Description**            |
|--------------|----------|----------------------------|
| Content-Type | String   | Support “application/json” |
| Accept       | String   | Support “application/json” |

> Authorization Headers

| **Name** | **Type** | **Description**                           |
|----------|----------|-------------------------------------------|
| Token    | String   | Authentication token, get from login API. |

Response
--------

| **Name**       | **Type**         | **Description**                        |
|----------------|------------------|----------------------------------------|
| licenseInfo    | Object | Tenant license information |
| licenseInfo.module         | Array of objects | Module list |
| licenseInfo.module.name    | String | Module name |
| licenseInfo.module.amount | Integer | Module license amount to be assigned. Editable. |
| licenseInfo.module.enable | Boolean | Whether or not to enable this module in the tenant. Editable. |
| licenseInfo.networkTechs | Array of objects | Network technology list |
| licenseInfo.networkTechs.name | String | Network technology name |
| licenseInfo.networkTechs.amount | Integer | Network technology license amount to be assigned. Editable. |
| statusCode | Integer | Status code |
| statusDescription | String | Status description |

## Response Codes

|**Code**|**Message**|**Description**|
|------|------|------|
| 790200 | OK |  |
| 793001 | InternalServerError | System framework level error |


***Example***
```python
{
    "licenseInfo": {
        "networkTechs": [
            {
                "name": "Cisco ACI",
                "amount": 0
            },
            {
                "name": "WAP",
                "amount": 0
            },
            {
                "name": "vCenter",
                "amount": 0
            },
            {
                "name": "NSX-v",
                "amount": 0
            },
            {
                "name": "Amazon AWS",
                "amount": 0
            },
            {
                "name": "Microsoft Azure",
                "amount": 0
            },
            {
                "name": "Google Cloud Platform",
                "amount": 0
            }
        ],
        "modules": [
            {
                "name": "Foundation",
                "amount": 0
            }
        ]
    },
    "statusCode": 790200,
    "statusDescription": "Success."
}
```

# Full Example
```python
# import python modules 
import requests
import json

# Set the request inputs
token = "0f93390b-9b11-41b5-9d89-3fc0b1e8af10"
full_url = "https://unicorn-new.netbraintech.com/ServicesAPI/API/V3/CMDB/Tenants/LicenseTemplate"

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
        print ("Get Tenant License failed! - " + str(response.text))

except Exception as e: print (str(e))

``` 

# cURL Code from Postman

```python
curl --location --request GET 'https://unicorn-new.netbraintech.com/ServicesAPI/API/V3/CMDB/Tenants/LicenseTemplate' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'token: 0f93390b-9b11-41b5-9d89-3fc0b1e8af10'
```
