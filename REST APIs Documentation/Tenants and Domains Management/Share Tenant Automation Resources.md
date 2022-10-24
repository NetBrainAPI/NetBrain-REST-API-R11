

# Automation Resources API

## ***POST*** /V1/CMDB/Tenants/AutomationResources
Use this API to share NetBrain automation resources, such as Runbook Templates, Qapps, Data View Templates, and Parsers, from the current tenant to other tenants.<br><br>
This API shares the resources by implementing an exporting and importing process from the source tenant to the target tenants. The post-share resource status aligns with the system behavior.<br><br>
Required system privileges:
1. Domain access of the source resource allocated domain.
2. ShareResourceManagement privilege to any domain/domains of the target tenants.

## Detail Information

> **Title** : Share Automation Resources API

> **Version** : 07/15/2022

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Tenants/AutomationResources

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body (\*required)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
| resources* | Array | Resource objects. |
|resources.type*|String|Resource type.|
|resources.sourcePath*|String|Resource full path, i.e., "Shared Parsers in Tenant/system". All the resources under this path and all the resources of the sub-folders under this path are all included. |
|resources.sourceIsFolder|Boolean|Whether or not the path indicates a folder or a single file.<br>Value options:<br>true: the path is a folder<br>false: the path is not a folder<br>null(default): search both folders and files (Note: null could be considered as null value or parameter not provided.)|
|resources.destinationFolder|String|The destination full path to be copied to. <br>Note:<br>If this parameter is not provided, the resources will be saved to the same path as sourcePath. <br>The path can only be allocated under resource shared folder.|
|resources.overwrite|Boolean|Whether or not to overwrite the existing resources in the destination path if conflicts found.<br>true(default): overwrite<br>false: not overwrite (Note: if conflicts found on runbook template, the API returns error. For the rest of resource types, the API will ignore the conflicts.)|
|resources.importRelatedResources|Boolean|Whether or not to import the resource related resources. For example, import the parsers being used by a Qapp. <br>true: import<br>false(default): not import|
|tenants|Array|Target tenants.|


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
|resources| Array |Resource objects.|
|resources.sourcePath|String|Resource full path|
|resources.tenants|Object|Target tenant import status object.|
|resources.tenants.{TenantName}|String|Target tenant import status.|
|statusCode| Integer | Status code. |
|statusDescription| String | Status description. |
