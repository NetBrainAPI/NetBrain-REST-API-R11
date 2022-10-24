
# System License REST API Design

GET /V3/System/nodeinfo
-----------------------

Get system license information.
Support both Separate and Universal Modes.

Detail Information
------------------

> Title: System License API

> Version: 03/07/2022

> API Server URL: http(s)://IP Address of NetBrain Web API Server/ServicesAPI/API/V3/System/nodeinfo

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
| licenseInfo | Object | System license information |
| licenseInfo.module         | Array of objects | Module list |
| licenseInfo.module.name    | String | Module name |
| licenseInfo.module.max_amount | Integer | Maximum license amount |
| licenseInfo.module.available_amount | Integer | Available license amount |
| licenseInfo.module.status | String | Module license status |
| licenseInfo.networkTechs | Array of objects | Network technology list |
| licenseInfo.networkTechs.name | String | Network technology name |
| licenseInfo.networkTechs.max_amount | Integer | Network technology maximum amount |
| licenseInfo.networkTechs.available_amount | Integer | Network technology available amount |
| licenseInfo.networkTechs.status | String | Network technology license status |
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
                "max_amount": 200000,
                "status": "In Use",
                "available_max_amount": 180000
            },
            {
                "name": "WAP",
                "max_amount": 200000,
                "status": "In Use",
                "available_max_amount": 180000
            },
            {
                "name": "Amazon AWS",
                "max_amount": 200000,
                "status": "In Use",
                "available_max_amount": 180000
            }
        ],
        "modules": [
            {
                "name": "Foundation",
                "max_amount": 200000,
                "status": "In Use",
                "available_max_amount": 178945
            },
            {
                "name": "Change Management",
                "max_amount": 266660,
                "status": "In Use",
                "available_max_amount": 238939
            },
            {
                "name": "Application Assurance",
                "max_amount": 6566640,
                "status": "In Use",
                "available_max_amount": 5908921
            },
            {
                "name": "Intent Based Automation",
                "max_amount": 1466660,
                "status": "In Use",
                "available_max_amount": 1318939
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
full_url = "https://unicorn-new.netbraintech.com/ServicesAPI/API/V3/System/nodeinfo"

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
        print ("Get License failed! - " + str(response.text))

except Exception as e: print (str(e))

``` 

# cURL Code from Postman

```python
curl --location --request GET 'https://unicorn-new.netbraintech.com/ServicesAPI/API/V3/System/nodeinfo' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'token: 0f93390b-9b11-41b5-9d89-3fc0b1e8af10' \
--data-raw ''
```
