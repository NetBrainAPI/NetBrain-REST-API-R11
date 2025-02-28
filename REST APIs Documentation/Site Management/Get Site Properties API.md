
# Site API Design

## ***GET*** /V1/CMDB/Sites/SiteInfo
Call this API to get the basic information of a site by site path or ID, as well as the information of site propeerties (if set as True).

## Detail Information

> **Title** : Get Site Info and properties API<br>

> **Version** : 02/07/2020.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Sites/SiteInfo

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

>No request body.

## Query Parameters(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|sitePath^ | string  | Full path name of the site. e.g. 'My Network/Site1/Boston/Dev'. |
|siteId^ | string  |  The unique ID of the specified site. |
|property | boolean | The boolean switch to decide whether to return the site detail information or not |
>**Note :** ^ required if the other parameter is null.

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
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code.  |
|siteInfo | object | An object with the basic information of the site.  |
|siteInfo.sitePath | string | Full path of the site.  |
|siteInfo.siteId| string | ID of the site. This is the only way to get the id of root site. |
|siteInfo.siteType| integer | Type of this site; 0 root site, 1 container site, 2 leaf site.  |
|siteInfo.properties| object | Site detail information. |
|siteInfo.properties.name| string | Site name. |
|siteInfo.properties.region| string | Site region. |
|siteInfo.properties.locAdr| string | Site location or address infromation. |
|siteInfo.properties.employeeNum| int | Site employee number. |
|siteInfo.properties.deviceNum| int | Device number inside the current site. |
|siteInfo.properties.contactName| string | Site admin contact name. |
|siteInfo.properties.phone| string | Site admin phone number. |
|siteInfo.properties.email| string | Site admin email. |
|siteInfo.properties.siteType| string | Site type; Headquarter, Data Center, Regional Office, Disaster Recovery |
|siteInfo.properties.description| string | Site description. |
|siteInfo.properties.customizedInfo| object | Site customized information. |


> ***Example***


```python
{
    "siteInfo": [
        {
            "siteId": "1da4fda8-5d04-491b-8bb0-2e9abb989a60",
            "sitePath": "My Network/NA/US",
            "isContainer": true,
            "siteType": 0,
            "properties": {
                "name" : "site1",
                "region" : "XXXX",
                "locAdr" : "Boston",
                "employeeNum" : 1,
                "deviceNum" : 50,
                "contactName" : "XXXXX",
                "phone" : "123456789",
                "email" : "XXXX@.com",
                "siteType" : "Headquarter",
                "description" : "random example",
                "customizedInfo" : [
                    "Field1" : "XXXXXXXXXXXXXXXXXXXX",
                    .
                    .
                    .
                    ]          
              }
        },
        .
        .
        .
    ]
}
```
```python

{
  "siteInfo": {
    "properties": {
      "name": "My Network",
      "region": null,
      "locAdr": null,
      "employeeNum": 0,
      "deviceNum": 8,
      "contactName": null,
      "phone": null,
      "email": null,
      "siteType": null,
      "description": null,
      "customizedInfo": null
    },
    "siteId": "732e8ab6-6b69-417d-ad03-2cc447100166",
    "sitePath": "My Network",
    "isContainer": true,
    "children": null,
    "siteType": 0
  },
  "statusCode": 790200,
  "statusDescription": "Success."
}
```
# Full Example：


```python
# import python modules 
import requests
import time
import urllib3
import pprint
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the request inputs
token = "9603ce1d-8271-4f77-a2df-0b748ef32084"
nb_url = "http://192.168.32.17"
full_url = nb_url + "/ServicesAPI/API/V1/CMDB/Sites/SiteInfo"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

sitePath = "My Network/Site2"
siteId = ""
property = True

data = {
           "sitePath" : sitePath,
            #"siteId": siteId
            "property" : property
        } 

try:
    response = requests.get(full_url, params = data, headers = headers, verify = False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Failed to get Site Info! - " + str(response.text))
    
except Exception as e:
    print (str(e)) 
```
    Failed to get Site Info! - {"statusCode":791006,"statusDescription":"site with path My Network/Site2 does not exist."}


# cURL Code from Postman: 


```python
curl -X GET \
  'http://192.168.32.17/ServicesAPI/API/V1/CMDB/Sites/SiteInfo' \
  -H 'cache-control: no-cache' \
  -H 'token: 5cbfbefc-b190-4fcb-9bc0-8460a31a1f73' \
  --get --data-urlencode "sitePath=My Network/" \
  --data-urlencode "property=true"
```

# Error Examples：
See API _Delete Site API_ for error examples.
