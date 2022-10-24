

# Path Browser Management Design

## ***GET*** /V1/CMDB/PathBrowser/Paths
Using this API call to get saved paths from Path Browser.

## Detail Information

> **Title** : Get Saved Paths API<br>

> **Version** : 07/12/2022

> **API Server URL** : http(s):// IP address of your NetBrain Web API Server /ServicesAPI/V1/CMDB/PathBrowser/Paths

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
|application|string|Application Name. Return the saved path of the specified application if this parameter is used.|
|skip*|integer|The amount of records to be skipped. The value must not be negative.|
|limit*|integer|The up limit amount of device records to return per API call. The value must not be negative. The range is 10 to 100.|
|fullattr*|integer|Default is 0.<br>0: return basic path attributes. (applicationName, pathName)<br>1: return all path attributes.|


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
|paths.applicationName| string |The application name that the path belongs to.|
|paths.pathName| string |Path name.|
|paths.sourceIP| string |Source IP.|
|paths.destinationIP| string |Destination IP.|
|paths.group| string |Multicast group.|
|paths.protocol| string |Protocol.|
|paths.lastResult| string |Last path execution status.|
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code. |
