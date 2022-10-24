
# Azure Account Management Design

## ***GET*** /V1/CMDB/ApiServers/AzureAccounts
Using this API call to get Azure accounts in API Server Manager. The encrypted field are not returned.

## Detail Information

> **Title** : Get Azure Accounts API<br>

> **Version** : 07/12/2022

> **API Server URL** : http(s):// IP address of your NetBrain Web API Server /ServicesAPI/V1/CMDB/ApiServers/AzureAccounts

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

> No parameters required.

## Parameters(****required***)  
|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|accountId|string|The account ID(Endpoint) of Azure |
|name|string|API Server Name |

> **Note** : The API call will return all Azure accounts if not specify any accountId or name in parameters. If both parameters are provided in the request, NetBrain primarily picks accountId.

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
|id| string | The API Server ID.|
|accountId | string  |Endpoint (Client/VM ID)|
|name|string|API Server Name|
|desc|string|Description of API Server|
|AccessMethod|string|Access Method of Azure account.|
|AZURE_TENANT_ID|string|Directory (Tenant) ID.|
|EXCLUDED_VIRTUAL_NETWORKS|string|The virtual networks to be excluded during discovery.|
|INCLUDED_VIRTUAL_NETWORKS|string|The only virtual networks to be included during discovery.|
|frontServerAndGroupId|string|Front Server name|
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code. |