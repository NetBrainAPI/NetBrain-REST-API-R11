
# Azure Account Management Design

## ***PATCH*** /V1/CMDB/ApiServers/AzureAccounts
Using this API call to update parameters for an Azure account in API Server Manager.

## Detail Information

> **Title** : Patch Azure Account API<br>

> **Version** : 07/12/2022

> **API Server URL** : http(s):// IP address of your NetBrain Web API Server /ServicesAPI/V1/CMDB/ApiServers/AzureAccounts

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|id* | string  |  The API server id |
|EXCLUDED_VIRTUAL_NETWORKS|string|The virtual networks to be excluded during discovery.|
|INCLUDED_VIRTUAL_NETWORKS|string|The only virtual networks to be included during discovery.|

## Parameters(****required***)

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
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code. |

> ***Example***
```python
{
	'statusCode': 790200, 
	'statusDescription': 'Success.'
}

```
## Response Codes
|**Code**|**Message**|**Description**|
|------|------|------|
| 790200 | OK |  |
| 791000 | ParameterNull | API Server id is missing|
| 793404 | NotFound | Not found|