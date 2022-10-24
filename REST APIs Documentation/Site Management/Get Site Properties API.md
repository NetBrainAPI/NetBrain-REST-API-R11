
# Site API Design

## ***GET*** /V1/CMDB/Sites/SiteInfo
Calling this API to get the basic information of a site by site path or ID.

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
|sitePath^ | string  | Full path name of a site. For example, 'My Network/Site1/Boston/Dev'. |
|siteId^ | string  |  The unique id of specified site. |
|property | boolean | The boolean switch to decide whether return the site detail information |
>>**Note :** ^ required if the other parameter is null.

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
|siteInfo | object | An object with the basic information of a site.  |
|siteInfo.sitePath | string | Full path of site.  |
|siteInfo.siteId| string | Id of site. This is the only way to get the id of root site. |
|siteInfo.siteType| integer | Type of this site, 0 root site, 1 container site, 2 leaf site.  |
|siteInfo.properties| object | site detail information. |
|siteInfo.properties.name| string | site name. |
|siteInfo.properties.region| string | site region. |
|siteInfo.properties.locAdr| string | site location or address infromation. |
|siteInfo.properties.employeeNum| int | site employee number. |
|siteInfo.properties.deviceNum| int | device number inside current site. |
|siteInfo.properties.contactName| string | site admin contact name. |
|siteInfo.properties.phone| string | site admin phone number. |
|siteInfo.properties.email| string | site admin email. |
|siteInfo.properties.siteType| string | site type. (Headquarter, Data Center, Regional Office, Disaster Recovery) |
|siteInfo.properties.description| string | site description. |
|siteInfo.properties.customizedInfo| object | site customized information. |


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